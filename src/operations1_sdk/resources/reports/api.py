from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Unpack, overload

from .models import ListReportsResponse, Report
from .types import GetReportsParams

if TYPE_CHECKING:
    from operations1_sdk.client import Operations1Client


class ReportsAPI:
    """Operations1 Reports API resource."""

    endpoint = "/reports"

    def __init__(self, client: Operations1Client):
        self.client = client

    @overload
    def list(
        self, *, raw: Literal[False] = False, **params: Unpack[GetReportsParams]
    ) -> ListReportsResponse: ...

    @overload
    def list(
        self, *, raw: Literal[True], **params: Unpack[GetReportsParams]
    ) -> dict: ...

    def list(
        self, *, raw: bool = False, **params: Unpack[GetReportsParams]
    ) -> ListReportsResponse | dict:
        """
        List reports with pagination.

        Args:
            raw: If True, return raw dict. If False (default), return typed ListReportsResponse.
            **params: Query parameters for filtering/pagination.

        Returns:
            ListReportsResponse or dict depending on raw parameter.
        """
        self._validate_params(params)
        response = self.client.get(self.endpoint, params=params)
        data = response.json()
        return data if raw else ListReportsResponse(**data)

    @overload
    def list_all(
        self,
        *,
        limit_pages: int | None = None,
        raw: Literal[False] = False,
        **params: Unpack[GetReportsParams],
    ) -> list[Report]: ...

    @overload
    def list_all(
        self,
        *,
        limit_pages: int | None = None,
        raw: Literal[True],
        **params: Unpack[GetReportsParams],
    ) -> list[dict]: ...

    def list_all(
        self,
        *,
        limit_pages: int | None = None,
        raw: bool = False,
        **params: Unpack[GetReportsParams],
    ) -> list[Report] | list[dict]:
        """
        Fetch all reports across pages.

        Args:
            limit_pages: Optional limit on number of pages to fetch.
            raw: If True, return list of dicts. If False (default), return list of Report objects.
            **params: Query parameters for filtering/pagination.

        Returns:
            list[Report] or list[dict] depending on raw parameter.
        """
        self._validate_params(params)
        return list(
            self.client._paginate(
                self.endpoint, params=params, limit_pages=limit_pages, raw=raw
            )
        )

    @overload
    def get(self, report_id: int, *, raw: Literal[False] = False) -> Report: ...

    @overload
    def get(self, report_id: int, *, raw: Literal[True]) -> dict: ...

    def get(self, report_id: int, *, raw: bool = False) -> Report | dict:
        """
        Get a report by ID.

        Args:
            report_id: Report ID to fetch.
            raw: If True, return raw dict. If False (default), return typed Report.

        Returns:
            Report or dict depending on raw parameter.
        """
        response = self.client.get(f"{self.endpoint}/{report_id}")
        data = response.json()
        return data if raw else Report(**data)

    def _validate_params(self, params: dict):
        search = params.get("search")

        if search is not None and len(search) < 3:
            raise ValueError("search must be at least 3 characters")
