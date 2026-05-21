from __future__ import annotations

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class AssignedEntity(BaseModel):
    """Represents an assigned user or group."""

    id: Optional[int] = None
    name: Optional[str] = None
    displayName: Optional[str] = None


class ClassCharacteristic(BaseModel):
    """Class characteristic associated with orders or documents."""

    id: int
    name: str
    classId: int
    data: dict[str, str]
    createdAt: datetime
    createdBy: Optional[int] = None
    createdByUserName: Optional[str] = Field(None, min_length=1, max_length=255)
    updatedAt: datetime
    updatedBy: Optional[int] = None
    updatedByUserName: Optional[str] = Field(None, min_length=1, max_length=255)
    archived: bool
