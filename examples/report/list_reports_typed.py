"""Example: List reports with typed response."""

from operations1_sdk import Operations1Client

client = Operations1Client(
    tenant_id="your-tenant",
    api_token="your-api-token",
    version="2025-04-21",
)

response = client.reports.list(
    pageSize=20,
    pageIndex=0,
    states=["in-progress", "done"],
)

print(f"Total reports: {response.totalItemCount}")
print(f"Page {response.pageIndex} (size {response.pageSize})")

for report in response.items:
    print(f"- Report #{report.id}: {report.name} (state: {report.state})")
    print(f"  Progress: {report.numFinishedSteps}/{report.numOfSteps} steps")
    if report.assignment:
        print(f"  Can start: {report.assignment.canBeStarted}")
