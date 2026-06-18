from typing import Any

from fastapi import APIRouter, Request
from pydantic import BaseModel, ConfigDict, Field, field_validator

from src.services import NotificationDispatcher


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


router = APIRouter(prefix="/webhooks", tags=["webhooks"])


def get_dispatcher(request: Request) -> NotificationDispatcher:
    return request.app.state.notification_dispatcher


@router.post("/events")
async def handle_state_event_webhook(payload: EventWebhookRequest, request: Request) -> dict:
    event_payload = payload.model_dump()
    event_payload["data"] = event_payload.get("data") or {
        key: value
        for key, value in event_payload.items()
        if key not in {"event", "routing_key", "data"}
    }
    routing_key = payload.routing_key or payload.event or "notification.state.changed"
    await get_dispatcher(request).dispatch_event(event_payload, str(routing_key))
    return {"status": "accepted", "event": payload.event, "routing_key": routing_key}
