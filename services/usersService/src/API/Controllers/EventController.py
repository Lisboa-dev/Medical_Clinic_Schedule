from typing import Any

from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, ConfigDict, Field, field_validator

from src.api.provider import UserFactory
from src.infra.adapters.EventBus import BroadcastEventBus
from src.infra.websocket import events_hub


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


routerEvents = APIRouter(tags=["events"])


def event_bus_factory() -> BroadcastEventBus:
    return UserFactory.event_bus_factory()


@routerEvents.websocket("/users/ws/events")
@routerEvents.websocket("/ws/events")
async def websocket_events(websocket: WebSocket) -> None:
    await events_hub.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        events_hub.disconnect(websocket)


@routerEvents.post("/users/infra/webhooks/events")
@routerEvents.post("/users/infra/events")
async def handle_state_event_webhook(
    payload: EventWebhookRequest,
    event_bus: BroadcastEventBus = Depends(event_bus_factory),
) -> dict:
    event_payload = payload.model_dump()
    published = await event_bus.publish_payload(event_payload, payload.routing_key)
    return {"status": "accepted", **published}
