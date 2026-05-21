from __future__ import annotations

from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field

from operations1_sdk.models.common import AssignedEntity, ClassCharacteristic


class OrderDocumentAssignment(BaseModel):
    """Document assignment within an order."""

    id: int = Field(..., description="Order document assignment ID")
    position: int = Field(..., ge=0)
    quantity: int = Field(..., ge=1)
    subAssigneeId: Optional[int] = Field(
        None,
        deprecated=True,
        description="Deprecated. Use top-level order assignedUsers or dedicated order-document-assignment endpoints.",
    )
    subAssigneeUserName: Optional[str] = Field(
        None,
        deprecated=True,
        description="Deprecated. Use top-level order assignedUsers or dedicated order-document-assignment endpoints.",
    )
    assignedUsers: Optional[list[AssignedEntity]] = Field(
        None,
        deprecated=True,
        description="Deprecated. Use top-level order assignedUsers or dedicated order-document-assignment endpoints.",
    )
    assignedGroups: Optional[list[AssignedEntity]] = Field(
        None,
        deprecated=True,
        description="Deprecated. Use top-level order assignedGroups or dedicated order-document-assignment endpoints.",
    )
    documentBaseId: Optional[int] = None
    documentId: int
    useLatestDocument: bool
    reportName: Optional[str] = None
    classCharacteristics: list[ClassCharacteristic]


class Order(BaseModel):
    """Operations1 order resource."""

    id: Optional[int] = None
    ruleId: Optional[int] = None
    customId: Optional[str] = None
    name: str
    description: str
    additionalData: str
    priority: int = Field(..., ge=1, le=10)
    state: Literal[
        "in-edit",
        "not-started",
        "in-progress",
        "cancelled",
        "paused",
        "problem",
        "done",
        "scheduled",
    ]
    startDate: Optional[datetime] = None
    dueDate: Optional[datetime] = None
    assignedGroups: list[AssignedEntity]
    assignedUsers: list[AssignedEntity]
    canBeTakenOver: bool
    orderDocumentAssignments: Optional[list[OrderDocumentAssignment]] = None
    reportIds: Optional[list[int]] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[int] = None
    createdByUserName: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[int] = None
    updatedByUserName: Optional[str] = None
    archived: bool
    automaticCompletion: bool
    executionMode: Literal["parallel", "sequence"]
    variables: Optional[dict[str, Optional[str]]] = None
    classCharacteristics: Optional[list[ClassCharacteristic]] = None


class ListOrdersResponse(BaseModel):
    """Paginated list of orders."""

    totalItemCount: int = Field(..., ge=0)
    pageIndex: int = Field(..., ge=0)
    pageSize: int = Field(default=10, ge=10, le=200)
    items: list[Order]
