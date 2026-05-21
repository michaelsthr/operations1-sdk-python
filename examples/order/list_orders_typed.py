"""
Example usage of Operations1 SDK with typed returns.
"""

from operations1_sdk import Operations1Client

client = Operations1Client(
    tenant_id="your-tenant", api_token="your-api-token", version="2026-05-18"
)

response = client.orders.list(pageSize=50, states=["in-progress", "not-started"])

print(f"Total orders: {response.totalItemCount}")
print(f"Page {response.pageIndex + 1}, showing {response.pageSize} items")

for order in response.items:
    print(f"Order #{order.id}: {order.name}")
    print(f"State: {order.state}")
    for doc in order.orderDocumentAssignments:
        print(f"Document {doc.documentId}")
