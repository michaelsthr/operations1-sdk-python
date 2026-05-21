from typing import Literal, NotRequired, Union
from datetime import datetime

from operations1_sdk.types.params import PaginationParams


class GetOrdersParams(PaginationParams, total=False):
    direction: NotRequired[Literal["ASC", "DESC"]]
    states: NotRequired[
        list[
            Literal[
                "in-edit",
                "not-started",
                "in-progress",
                "cancelled",
                "paused",
                "problem",
                "done",
                "scheduled",
            ]
        ]
    ]
    updatedAtMin: NotRequired[Union[datetime, str]]
    updatedAtMax: NotRequired[str]
    orderBy: NotRequired[Literal["updatedAt", "id"]]
    archived: NotRequired[bool]
    customOrderIds: NotRequired[list[str]]
    orderIds: NotRequired[list[int]]
    search: NotRequired[str]
    classCharacteristicIds: NotRequired[list[int]]
    ruleId: NotRequired[list[int]]
