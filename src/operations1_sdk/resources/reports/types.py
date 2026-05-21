from typing import Literal, NotRequired, Union
from datetime import datetime

from operations1_sdk.types.params import PaginationParams


class GetReportsParams(PaginationParams, total=False):
    states: NotRequired[
        list[Literal["not-started", "in-progress", "paused", "problem", "done"]]
    ]
    updatedAtMin: NotRequired[Union[datetime, str]]
    updatedAtMax: NotRequired[Union[datetime, str]]
    orderBy: NotRequired[Literal["updatedAt", "id"]]
    direction: NotRequired[Literal["ASC", "DESC"]]
    archived: NotRequired[bool]
    classCharacteristicIds: NotRequired[list[int]]
    orderIds: NotRequired[list[int]]
    search: NotRequired[str]
