from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Unpack, overload

from operations1_sdk.models.requests import CreateOrderRequest
from .models import ListOrdersResponse, Order
from .types import GetOrdersParams

if TYPE_CHECKING:
    from operations1_sdk.client import Operations1Client


class OrdersAPI:
    """Operations1 Orders API resource."""

    endpoint = "/orders"

    def __init__(self, client: Operations1Client):
        self.client = client

    @overload
    def list(
        self, *, raw: Literal[False] = False, **params: Unpack[GetOrdersParams]
    ) -> ListOrdersResponse: ...

    @overload
    def list(
        self, *, raw: Literal[True], **params: Unpack[GetOrdersParams]
    ) -> dict: ...

    def list(
        self, *, raw: bool = False, **params: Unpack[GetOrdersParams]
    ) -> ListOrdersResponse | dict:
        """
        List orders with pagination.

        Args:
            raw: If True, return raw dict. If False (default), return typed ListOrdersResponse.
            **params: Query parameters for filtering/pagination.

        Returns:
            ListOrdersResponse or dict depending on raw parameter.
        """
        self._validate_params(params)
        response = self.client.get(self.endpoint, params=params)
        data = response.json()
        return data if raw else ListOrdersResponse(**data)

    @overload
    def list_all(
        self,
        *,
        limit_pages: int | None = None,
        raw: Literal[False] = False,
        **params: Unpack[GetOrdersParams],
    ) -> list[Order]: ...

    @overload
    def list_all(
        self,
        *,
        limit_pages: int | None = None,
        raw: Literal[True],
        **params: Unpack[GetOrdersParams],
    ) -> list[dict]: ...

    def list_all(
        self,
        *,
        limit_pages: int | None = None,
        raw: bool = False,
        **params: Unpack[GetOrdersParams],
    ) -> list[Order] | list[dict]:
        """
        Fetch all orders across pages.

        Args:
            limit_pages: Optional limit on number of pages to fetch.
            raw: If True, return list of dicts. If False (default), return list of Order objects.
            **params: Query parameters for filtering/pagination.

        Returns:
            list[Order] or list[dict] depending on raw parameter.
        """
        self._validate_params(params)
        return list(
            self.client._paginate(
                self.endpoint, params=params, limit_pages=limit_pages, raw=raw
            )
        )

    @overload
    def create(
        self,
        order: CreateOrderRequest | dict,
        *,
        raw: Literal[False] = False,
    ) -> Order: ...

    @overload
    def create(
        self,
        order: CreateOrderRequest | dict,
        *,
        raw: Literal[True],
    ) -> dict: ...

    def create(
        self,
        order: CreateOrderRequest | dict,
        *,
        raw: bool = False,
    ) -> Order | dict:
        """
        Create a new order.

        Args:
            order: CreateOrderRequest object or dict with order data.
            raw: If True, return raw dict. If False (default), return typed Order.

        Returns:
            Order or dict depending on raw parameter.
        """
        # Convert to dict if Pydantic model
        if isinstance(order, CreateOrderRequest):
            payload = order.model_dump(mode="json", exclude_none=True)
        else:
            payload = order

        response = self.client.post(self.endpoint, json=payload)
        data = response.json()
        return data if raw else Order(**data)

    def _validate_params(self, params: dict):
        search = params.get("search")

        if search is not None and len(search) < 3:
            raise ValueError("search must be at least 3 characters")
