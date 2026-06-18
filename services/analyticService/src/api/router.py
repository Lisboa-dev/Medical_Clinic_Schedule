from typing import Any

from fastapi import APIRouter, Query, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, ConfigDict, Field, field_validator

from src.infra.websocket import events_hub
from src.services import EventIngestionService

router = APIRouter()


class EventWebhookRequest(BaseModel):
    model_config = ConfigDict(extra="allow")

    event: str | None = None
    routing_key: str | None = None
    data: dict[str, Any] = Field(default_factory=dict)

    @field_validator("event", "routing_key")
    @classmethod
    def validate_non_empty(cls, value: str | None) -> str | None:
        if value is None:
            return None
        value = value.strip()
        if not value:
            raise ValueError("value cannot be empty")
        return value


def get_service(request: Request) -> EventIngestionService:
    return request.app.state.event_ingestion_service


@router.get("/analytics/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/analytics/events", tags=["events"])
def list_events(request: Request, limit: int = Query(default=100, ge=1, le=500)) -> list[dict]:
    return jsonable_encoder(get_service(request).list_recent(limit=limit))


@router.get("/analytics/events/summary", tags=["events"])
def summarize_events(request: Request) -> list[dict]:
    return jsonable_encoder(get_service(request).count_by_source())


@router.post("/analytics/webhooks/events", tags=["webhooks"])
@router.post("/analytics/events", tags=["webhooks"])
async def handle_state_event_webhook(payload: EventWebhookRequest, request: Request) -> dict:
    event_payload = payload.model_dump()
    event_payload["data"] = event_payload.get("data") or {
        key: value
        for key, value in event_payload.items()
        if key not in {"event", "routing_key", "data"}
    }
    routing_key = payload.routing_key or payload.event or "analytics.state.changed"
    await get_service(request).ingest(event_payload, str(routing_key))
    return {"status": "accepted", "event": payload.event, "routing_key": routing_key}


@router.websocket("/analytics/ws/events")
async def websocket_events(websocket: WebSocket) -> None:
    await events_hub.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        events_hub.disconnect(websocket)


@router.get("/analytics/metrics", tags=["metrics"])
def metrics(request: Request) -> Response:
    metrics_registry = getattr(request.app.state, "http_metrics", None)
    content = metrics_registry.render() if metrics_registry is not None else ""
    return Response(content, media_type="text/plain; version=0.0.4")
