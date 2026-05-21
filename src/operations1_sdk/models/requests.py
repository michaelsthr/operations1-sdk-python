from __future__ import annotations

from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field


class CreateOrderDocumentAssignment(BaseModel):
    """Document assignment for creating an order."""

    documentId: int = Field(..., ge=1)
    subAssigneeId: Optional[int] = Field(
        None,
        deprecated=True,
        description="Deprecated. Use assignedUserIds and assignedGroupIds instead.",
    )
    assignedUserIds: Optional[list[int]] = Field(default=None, min_length=0)
    assignedGroupIds: Optional[list[int]] = Field(default=None, min_length=0)
    useLatestDocument: bool = Field(default=True)
    reportName: Optional[str] = Field(None, min_length=1)
    classCharacteristicIds: Optional[list[int]] = Field(default=None, min_length=0)


class CreateOrderRequest(BaseModel):
    """Request body for creating an order."""

    name: str = Field(..., min_length=1)
    description: str = Field(default="")
    additionalData: Optional[str] = None
    priority: int = Field(
        default=5,
        ge=1,
        le=10,
        description="""
      . Very low priority: Represented by 3 or below
      . Low priority: Represented by 4
      . Normal priority: Represented by 5
      . High priority: Represented by 6
      . Very high priority: Represented by 7 or higher
      . Default Priority is Normal: Represented by 5""",
    )
    startDate: datetime
    dueDate: datetime
    assignedUserIds: Optional[list[int]] = Field(default=None, min_length=0)
    assignedGroupIds: Optional[list[int]] = Field(default=None, min_length=0)
    canBeTakenOver: bool = Field(default=True)
    automaticCompletion: bool = Field(default=True)
    customOrderId: Optional[str] = Field(None, min_length=1)
    classCharacteristicIds: Optional[list[int]] = Field(default=None, min_length=0)
    inheritDocumentsClassCharacteristics: bool = Field(default=True)
    executionMode: Literal["parallel", "sequence"] = Field(default="parallel")
    orderDocumentAssignments: list[CreateOrderDocumentAssignment]
    variables: Optional[dict[str, Optional[str]]] = None
