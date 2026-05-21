"""Example: Get report by ID."""

from operations1_sdk import Operations1Client

client = Operations1Client(
    tenant_id="your-tenant",
    api_token="your-api-token",
    version="2025-04-21",
)

report = client.reports.get(report_id=12345)

print(f"Report #{report.id}: {report.name}")
print(f"Document: {report.documentName}")
print(f"State: {report.state}")
print(f"Progress: {report.numFinishedSteps}/{report.numOfSteps} steps")
print(f"Created: {report.createdAt} by {report.createdByUserName}")
print(f"Updated: {report.updatedAt} by {report.updatedByUserName}")

if report.orderId:
    print(f"Order ID: {report.orderId} (position: {report.orderPosition})")

if report.assignment:
    print("\nAssignment:")
    print(f"  Can be started: {report.assignment.canBeStarted}")
    if report.assignment.assignedUsers:
        print(f"  Assigned users: {[u.name for u in report.assignment.assignedUsers]}")
    if report.assignment.assignedGroups:
        print(
            f"  Assigned groups: {[g.name for g in report.assignment.assignedGroups]}"
        )
