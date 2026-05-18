from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, Field
import uuid


class QR(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    size: int
    content: str
    path: str
    date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        from_attributes = True