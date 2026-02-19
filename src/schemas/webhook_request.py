from pydantic import BaseModel
from typing import Optional


class WebhookRequest(BaseModel):
    id: Optional[int]
    app_name: str
    alert_payload: dict
