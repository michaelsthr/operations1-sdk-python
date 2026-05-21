"""
Operations1 Python SDK

Official Python SDK for the Operations1 REST API.
"""

from operations1_sdk.client import Operations1Client
from operations1_sdk.models import (
    AssignedEntity,
    ClassCharacteristic,
    CreateOrderDocumentAssignment,
    CreateOrderRequest,
)
from operations1_sdk.resources.orders import (
    Order,
    OrderDocumentAssignment,
    ListOrdersResponse,
    GetOrdersParams,
)
from operations1_sdk.resources.reports import (
    Report,
    ReportAssignment,
    DocumentNames,
    ListReportsResponse,
    GetReportsParams,
)
from operations1_sdk.types import PaginationParams

__version__ = "0.1.0"

__all__ = [
    # Client
    "Operations1Client",
    # Models - Common
    "AssignedEntity",
    "ClassCharacteristic",
    # Models - Requests
    "CreateOrderRequest",
    "CreateOrderDocumentAssignment",
    # Orders
    "Order",
    "OrderDocumentAssignment",
    "ListOrdersResponse",
    "GetOrdersParams",
    # Reports
    "Report",
    "ReportAssignment",
    "DocumentNames",
    "ListReportsResponse",
    "GetReportsParams",
    # Types
    "PaginationParams",
]
