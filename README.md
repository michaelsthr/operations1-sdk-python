# Operations1 SDK for Python

A modern, fully-typed Python SDK for the [Operations1 REST API](https://developer.operations1.com).

## Features

- **Fully typed** - Complete type hints with Pydantic models
- **IDE autocomplete** - IntelliSense support for all API methods  
- **Runtime validation** - Automatic validation of requests and responses
- **Flexible responses** - Choose between typed models or raw dicts
- **Auto-pagination** - Fetch all pages with `list_all()`
- **Clean structure** - Per-endpoint organization for maintainability

## Supported Endpoints

- **Orders** - Create, list, paginate orders
- **Reports** - Get report by ID, list reports, paginate

More endpoints coming soon.

## Installation

```bash
pip install operations1-sdk
```

## Quick Start

```python
from operations1_sdk import Operations1Client

client = Operations1Client(
    tenant_id="company",
    api_token="your-api-token",
    version="2025-04-21"  # Recommended: date-based version
)

# List orders
orders = client.orders.list(pageSize=50, states=["in-progress"])
print(f"Found {orders.totalItemCount} orders")

# Get report by ID
report = client.reports.get(report_id=123)
print(f"Report: {report.name} - {report.state}")
```

## Orders API

### List Orders

```python
# Typed response (default, recommended)
response = client.orders.list(
    pageSize=100,
    states=["in-progress", "done"],
    archived=False,
    orderBy="updatedAt",
    direction="DESC"
)

for order in response.items:
    print(f"{order.name}: {order.state}")

# Raw dict response
raw = client.orders.list(raw=True, pageSize=100)
for order in raw["items"]:
    print(f"{order['name']}: {order['state']}")
```

### Fetch All Orders (Auto-paginated)

```python
# Returns list[Order] with all pages fetched
all_orders = client.orders.list_all(
    states=["done"],
    limit_pages=10  # Optional: limit to first 10 pages
)

print(f"Fetched {len(all_orders)} orders total")

# Or get raw dicts
raw_orders = client.orders.list_all(raw=True, states=["done"])
```

### Create Order

```python
from datetime import datetime, timezone
from operations1_sdk import CreateOrderRequest, CreateOrderDocumentAssignment

# Using typed Pydantic models (recommended)
order = CreateOrderRequest(
    name="Production Order #1234",
    description="Urgent production order",
    priority=8,  # 1-10, 5 is normal
    startDate=datetime(2025, 5, 21, 8, 0, tzinfo=timezone.utc),
    dueDate=datetime(2025, 5, 25, 17, 0, tzinfo=timezone.utc),
    assignedUserIds=[100, 101],
    assignedGroupIds=[20],
    executionMode="sequence",
    orderDocumentAssignments=[
        CreateOrderDocumentAssignment(
            documentId=123,
            assignedUserIds=[456],
            reportName="Quality Check"
        )
    ],
    variables={"customer_id": "ABC-001"},
)

created_order = client.orders.create(order)
print(f"Created order #{created_order.id}")

# Or use plain dict
order_dict = {
    "name": "Order #1235",
    "startDate": "2025-05-22T08:00:00Z",
    "dueDate": "2025-05-26T17:00:00Z",
    "orderDocumentAssignments": [{"documentId": 123}],
}
created = client.orders.create(order_dict)
```

## Reports API

### Get Report by ID

```python
# Typed response (default)
report = client.reports.get(report_id=12345)

print(f"Report: {report.name}")
print(f"State: {report.state}")
print(f"Progress: {report.numFinishedSteps}/{report.numOfSteps} steps")

# Raw dict response
report = client.reports.get(report_id=12345, raw=True)
print(report["name"])
```

### List Reports

```python
# Typed response with filters
response = client.reports.list(
    pageSize=100,
    states=["in-progress", "done"],
    orderBy="updatedAt",
    direction="DESC",
)

for report in response.items:
    print(f"{report.name}: {report.numFinishedSteps}/{report.numOfSteps}")

# Auto-paginate all reports
all_reports = client.reports.list_all(
    states=["in-progress"],
    limit_pages=5  # Optional limit
)
print(f"Fetched {len(all_reports)} reports")
```

## Datetime Handling

SDK accepts Python `datetime` objects and converts them automatically:

```python
from datetime import datetime, timezone

orders = client.orders.list(
    updatedAtMin=datetime.now(timezone.utc),
)

# Or pass ISO strings
orders = client.orders.list(
    updatedAtMin="2025-05-01T00:00:00.000Z",
)
```

## Typed vs Raw Responses

All methods support `raw=True` parameter for raw dict responses:

```python
# Typed (default) - Pydantic models with validation
orders = client.orders.list(pageSize=50)
# orders: ListOrdersResponse
# orders.items: list[Order]

# Raw - plain dicts, no validation
orders = client.orders.list(raw=True, pageSize=50)
# orders: dict
# orders["items"]: list[dict]
```

**Use typed when:**
- You want IDE autocomplete
- You want runtime validation  
- You're building production code

**Use raw when:**
- You need exact API response
- Performance is critical (skip validation)
- You're debugging API issues

## Project Structure

```
src/operations1_sdk/
├── __init__.py          # Main exports
├── client.py            # API client
├── models/              # Shared models
│   ├── common.py        # AssignedEntity, ClassCharacteristic
│   └── requests.py      # CreateOrderRequest, etc.
├── resources/           # API endpoints (per-endpoint structure)
│   ├── orders/
│   │   ├── api.py       # OrdersAPI methods
│   │   ├── models.py    # Order, ListOrdersResponse
│   │   └── types.py     # GetOrdersParams
│   └── reports/
│       ├── api.py       # ReportsAPI methods
│       ├── models.py    # Report, ListReportsResponse
│       └── types.py     # GetReportsParams
└── types/               # Shared types
    └── params.py        # PaginationParams
```

Each endpoint has its own directory with models, types, and API logic co-located for maintainability.

## Examples

See [examples/](./examples) directory:

**Orders:**
- `order/list_orders_typed.py` - List orders with typed responses
- `order/list_orders_raw.py` - List orders with raw dicts
- `order/create_order_typed.py` - Create orders with Pydantic models
- `order/create_order_raw.py` - Create orders with plain dicts

**Reports:**
- `report/get_report_by_id.py` - Get single report by ID
- `report/list_reports_typed.py` - List reports with typed responses
- `report/list_reports_raw.py` - List reports with raw dicts
- `report/list_all_reports.py` - Auto-paginated report fetching

## API Versioning

Always specify an API version. Date-based versions recommended:

```python
client = Operations1Client(
    tenant_id="company",
    api_token="token",
    version="2025-04-21"  # Stable, recommended
)
```

Avoid `"latest"` in production - may include breaking changes.

See [API Documentation](https://developer.operations1.com) for version details.

## Development

Clone repository:

```bash
git clone https://github.com/yourname/operations1-sdk-python
cd operations1-sdk-python
```

Install in editable mode:

```bash
pip install -e .
```


### RUFF
[**RUFF**](https://docs.astral.sh/ruff)

Advised to do this before commiting the code to git. (Later Git hooks will be implemented)
U can also use install VSCode extension and configure it on *./vscode* dir.
#### install formatter using PIP
```bash
pip install ruff
```
#### format
```bash
ruff format
```
#### lint
```bash
ruff check --fix
```

## Contributing

Contributions, issues, and feature requests welcome!

## License

MIT
