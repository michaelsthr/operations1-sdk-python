"""
Example: Create a new order with typed models.
"""

from datetime import datetime, timezone
from operations1_sdk import (
    Operations1Client,
    CreateOrderRequest,
    CreateOrderDocumentAssignment,
)

client = Operations1Client(
    tenant_id="your-tenant", api_token="your-api-token", version="2026-05-18"
)

# --- Create order with Pydantic model (recommended) ---

order_request = CreateOrderRequest(
    name="Production Order #1234",
    description="Urgent production order for customer ABC",
    priority=8,
    startDate=datetime(2025, 5, 21, 8, 0, tzinfo=timezone.utc),
    dueDate=datetime(2025, 5, 25, 17, 0, tzinfo=timezone.utc),
    assignedUserIds=[1299],
    canBeTakenOver=True,
    automaticCompletion=True,
    executionMode="sequence",
    orderDocumentAssignments=[
        CreateOrderDocumentAssignment(
            documentId=5203,
            useLatestDocument=True,
            reportName="Quality Check Report",
        )
    ],
    variables={"customer_id": "ABC-001", "batch_number": "B2025-001"},
)

created_order = client.orders.create(order_request)
print(f"Created order #{created_order.id}: {created_order.name}")
print(f"State: {created_order.state}")
print(f"Priority: {created_order.priority}")
