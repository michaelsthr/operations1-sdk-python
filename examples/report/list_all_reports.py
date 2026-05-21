"""Example: List all reports with pagination."""

from operations1_sdk import Operations1Client

client = Operations1Client(
    tenant_id="your-tenant",
    api_token="your-api-token",
    version="2025-04-21",
)

all_reports = client.reports.list_all(
    pageSize=50,
    states=["in-progress"],
    orderBy="updatedAt",
    direction="DESC",
)

print(f"Fetched {len(all_reports)} in-progress reports")

for report in all_reports[:10]:  # Show first 10
    print(f"- {report.name}: {report.numFinishedSteps}/{report.numOfSteps} steps")
