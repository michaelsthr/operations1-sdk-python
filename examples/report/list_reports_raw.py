"""Example: List reports with raw dict response."""

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
    raw=True,
)

print(f"Total reports: {response['totalItemCount']}")
print(f"Page {response['pageIndex']} (size {response['pageSize']})")

for report in response["items"]:
    print(f"- Report #{report['id']}: {report['name']} (state: {report['state']})")
