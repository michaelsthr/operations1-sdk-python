"""
Example: Create order using raw dict.
"""

from operations1_sdk import Operations1Client

client = Operations1Client(
    tenant_id="your-tenant", api_token="your-api-token", version="2026-05-18"
)

order_dict = {
    "name": "Production Order #1234",
    "description": "Urgent production order for customer ABC",
    "priority": 8,
    "startDate": "2025-05-21T08:00:00Z",
    "dueDate": "2025-05-25T17:00:00Z",
    "assignedUserIds": [1299],
    "canBeTakenOver": True,
    "automaticCompletion": True,
    "executionMode": "sequence",
    "orderDocumentAssignments": [
        {
            "documentId": 5203,
            "useLatestDocument": True,
            "reportName": "Quality Check Report",
        }
    ],
    "variables": {"customer_id": "ABC-001", "batch_number": "B2025-001"},
}

created_order = client.orders.create(order_dict, raw=True)
print(f"Created order #{created_order['id']}: {created_order['name']}")
print(f"State: {created_order['state']}")
print(f"Priority: {created_order['priority']}")
