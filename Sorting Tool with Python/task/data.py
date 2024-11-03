import math
from enum import Enum
from typing import List, TypeVar

from sorting_type import SortingType


def as_int_list(_lines: List[str]) -> List[int]:
    numbers = []
    for line in _lines:
        for value in line.split():
            try:
                numbers.append(int(value))
            except ValueError:
                print(f'"{value}" is not a long. It will be skipped.')
    return numbers


def as_word_list(_lines: List[str]) -> List[str]:
    words = []
    for line in _lines:
        words.extend(line.split())
    return words


def strip_lines(_lines: List[str]) -> List[str]:
    return [line.strip() for line in _lines]


class DataType(Enum):
    LONG = {"prep": as_int_list, "join_char": " ", "print_name": "numbers"}
    WORD = {"prep": as_word_list, "join_char": " ", "print_name": "words"}
    LINE = {"prep": strip_lines, "join_char": "\n", "print_name": "lines"}


T = TypeVar("T")


class DataWrapper:
    def __init__(self, data: list[str], data_type: DataType, sorting_type: SortingType):
        self.data_type: DataType = data_type
        self.data: List[T] = data_type.value["prep"](data)
        self.sorting_type: SortingType = sorting_type
        self.join_char: str = self.data_type.value["join_char"]
        # pre-order in natural order
        self.data.sort()

    def get_sorted(self) -> str:
        total = f"Total {self.data_type.value['print_name']}: {len(self.data)}"
        match self.sorting_type:
            case SortingType.NATURAL:
                print_ready : str = self.join_char.join(map(str, self.data))
                return f"{total}\nSorted data:{self.join_char}{print_ready}"
            case SortingType.BY_COUNT:
                sorted_by_count = sorted(self.data, key=lambda x: SortingType.count(x, self.data))
                unique_by_count = list(dict.fromkeys(sorted_by_count))
                print_ready : List[str]= [
                    (f"{str(d)}: "
                     f"{self.data.count(d)} time(s), "
                     f"{math.floor(self.data.count(d) / len(self.data) * 100)}%")
                    for d in unique_by_count]
                result = '\n'.join(print_ready)
                return f"{total}\n{result}"
