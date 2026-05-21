from typing import Literal, NotRequired, TypedDict, Union


class PaginationParams(TypedDict, total=False):
    pageSize: NotRequired[int]
    pageIndex: NotRequired[Union[int, Literal["last"]]]
