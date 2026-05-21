from __future__ import annotations

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from datetime import datetime, timezone
from typing import Any, Generator

from operations1_sdk.resources.orders import Order, ListOrdersResponse
from operations1_sdk.resources import OrdersAPI, ReportsAPI


class Operations1Client:
    """Operations1 API client."""

    def __init__(
        self,
        tenant_id: str,
        api_token: str,
        version: str = "latest",
        retry_strategy: Retry = Retry(3, backoff_factor=0.1),
    ):
        """
        Initialize Operations1 API client.

        Args:
            tenant_id: Tenant subdomain (e.g., "company" for company.operations1.app)
            api_token: API authentication token
            version: API version (default: "latest", recommended: use date like "2025-04-21")
            retry_strategy: urllib3 Retry strategy for failed requests
        """
        self.api_url = f"https://api.operations1.app/tenants/{tenant_id}"
        self.version = version
        self.api_key = api_token
        self.retry_strategy = retry_strategy

        headers = {
            "accept-version": self.version,
            "accept": "application/json",
            "authorization": f"Bearer {self.api_key}",
        }

        self.session = requests.Session()
        self.session.mount("https://", HTTPAdapter(max_retries=self.retry_strategy))
        self.session.headers.update(headers)

        # API resources
        self.orders = OrdersAPI(self)
        self.reports = ReportsAPI(self)

    def get(self, path: str, params: dict | None = None) -> requests.Response:
        """Make GET request to API."""
        response = self.session.get(
            f"{self.api_url}{path}", params=self._params(**(params or {}))
        )
        response.raise_for_status()
        return response

    def post(self, path: str, json: dict | None = None) -> requests.Response:
        """Make POST request to API."""
        response = self.session.post(f"{self.api_url}{path}", json=json)
        response.raise_for_status()
        return response

    def _params(self, **kwargs: Any) -> dict:
        """Filter out None values from parameters."""
        # TODO: Implement date formatting for DATE_FIELDS
        DATE_FIELDS = {"updatedAtMin", "updatedAtMax"}
        return {k: v for k, v in kwargs.items() if v is not None}

    def _format_date(self, value: datetime | str | None) -> str | None:
        """Format datetime to API-compatible string."""
        if value is None:
            return None
        if isinstance(value, str):
            return value
        if value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)
        else:
            value = value.astimezone(timezone.utc)
        return value.strftime("%Y-%m-%dT00:00:00.000Z")

    def _paginate(
        self, path: str, params: dict, limit_pages: int | None = None, raw: bool = False
    ) -> Generator[Order | dict, None, None]:
        """Paginate through API results, yielding individual items."""
        page_index = params.get("pageIndex", 0)
        page_size = params.get("pageSize", 10)
        pages_fetched = 0

        while True:
            if limit_pages is not None and pages_fetched >= limit_pages:
                break
            page_params = {**params, "pageIndex": page_index, "pageSize": page_size}
            response = self.get(path, params=page_params)
            json_data = response.json()
            if raw:
                items = json_data.get("items", [])
            else:
                data = ListOrdersResponse(**json_data)
                items = data.items
            if not items:
                break
            for item in items:
                yield item
            pages_fetched += 1
            total_count = json_data["totalItemCount"]
            total_pages = (total_count + page_size - 1) // page_size
            if page_index + 1 >= total_pages:
                break

            page_index += 1
