from __future__ import annotations

from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field

from operations1_sdk.models.common import AssignedEntity, ClassCharacteristic


class DocumentNames(BaseModel):
    """Localized document names."""

    ar: Optional[str] = None
    bg: Optional[str] = None
    bs: Optional[str] = None
    cs: Optional[str] = None
    da: Optional[str] = None
    de: Optional[str] = None
    el: Optional[str] = None
    en: Optional[str] = None
    es: Optional[str] = None
    et: Optional[str] = None
    fi: Optional[str] = None
    fo: Optional[str] = None
    fr: Optional[str] = None
    hi: Optional[str] = None
    hr: Optional[str] = None
    hu: Optional[str] = None
    id: Optional[str] = None
    is_: Optional[str] = Field(None, alias="is")
    it: Optional[str] = None
    ja: Optional[str] = None
    ka: Optional[str] = None
    lo: Optional[str] = None
    lt: Optional[str] = None
    mn: Optional[str] = None
    ms: Optional[str] = None
    mt: Optional[str] = None
    nl: Optional[str] = None
    nn: Optional[str] = None
    pl: Optional[str] = None
    pt: Optional[str] = None
    ro: Optional[str] = None
    ru: Optional[str] = None
    sk: Optional[str] = None
    sl: Optional[str] = None
    sq: Optional[str] = None
    sr: Optional[str] = None
    sv: Optional[str] = None
    ta: Optional[str] = None
    th: Optional[str] = None
    tr: Optional[str] = None
    uk: Optional[str] = None
    vi: Optional[str] = None
    zh: Optional[str] = None


class ReportAssignment(BaseModel):
    """Report assignment details."""

    id: float
    orderId: float
    reportId: float
    position: float
    canBeStarted: bool
    assignedUsers: Optional[list[AssignedEntity]] = None
    assignedGroups: Optional[list[AssignedEntity]] = None


class Report(BaseModel):
    """Operations1 report resource."""

    id: int = Field(..., ge=1)
    name: Optional[str] = None
    documentId: int = Field(..., ge=1)
    documentName: Optional[str] = None
    documentNames: DocumentNames
    comment: Optional[str] = None
    numOfSteps: int = Field(..., ge=0)
    stepIndex: int = Field(..., ge=0)
    createdAt: datetime
    createdBy: Optional[int] = None
    createdByUserName: Optional[str] = None
    updatedBy: Optional[int] = None
    updatedAt: datetime
    updatedByUserName: Optional[str] = None
    orderId: Optional[int] = None
    state: Literal["not-started", "in-progress", "paused", "problem", "done"]
    offline: bool
    passed: Literal["no-entry", "pass", "unclear", "no-pass", "no-pass-critical"]
    localeCode: Optional[
        Literal[
            "ar",
            "bg",
            "bs",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "et",
            "fi",
            "fo",
            "fr",
            "hi",
            "hr",
            "hu",
            "id",
            "is",
            "it",
            "ja",
            "ka",
            "lo",
            "lt",
            "mn",
            "ms",
            "mt",
            "nl",
            "nn",
            "pl",
            "pt",
            "ro",
            "ru",
            "sk",
            "sl",
            "sq",
            "sr",
            "sv",
            "ta",
            "th",
            "tr",
            "uk",
            "vi",
            "zh",
        ]
    ] = None
    revision: int = Field(..., ge=0)
    availableLocales: list[
        Literal[
            "ar",
            "bg",
            "bs",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "et",
            "fi",
            "fo",
            "fr",
            "hi",
            "hr",
            "hu",
            "id",
            "is",
            "it",
            "ja",
            "ka",
            "lo",
            "lt",
            "mn",
            "ms",
            "mt",
            "nl",
            "nn",
            "pl",
            "pt",
            "ro",
            "ru",
            "sk",
            "sl",
            "sq",
            "sr",
            "sv",
            "ta",
            "th",
            "tr",
            "uk",
            "vi",
            "zh",
        ]
    ]
    archived: bool
    numFinishedSteps: int = Field(..., ge=0)
    firstOpenedAt: Optional[datetime] = None
    cycleTime: Optional[float] = None
    assignment: Optional[ReportAssignment] = None
    orderPosition: Optional[int] = Field(
        None, ge=0, description="Position of report within parent order"
    )
    classCharacteristics: Optional[list[ClassCharacteristic]] = None


class ListReportsResponse(BaseModel):
    """Paginated list of reports."""

    totalItemCount: int = Field(..., ge=0)
    pageIndex: int = Field(..., ge=0)
    pageSize: int = Field(default=10, ge=10, le=200)
    items: list[Report]
