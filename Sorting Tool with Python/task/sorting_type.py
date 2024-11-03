from enum import Enum
from typing import TypeVar, List

T = TypeVar("T")
class SortingType(Enum):

    @staticmethod
    def count(x: T, data: List[T]):
        return data.count(x)

    NATURAL = "natural"
    BY_COUNT = "byCount"
