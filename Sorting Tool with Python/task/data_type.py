from enum import Enum
from typing import List

def length_order(x):
   len(x)

def natural_order(x):
    return x

def as_int_list(_lines: List[str]) -> List[int]:
    numbers = []
    for line in _lines:
        numbers.extend(int(date) for date in line.split())
    return numbers


def as_word_list(_lines: List[str]) -> List[str]:
    words = []
    for line in _lines:
        words.extend(line.split())
    return words


def as_lines(_lines: List[str]) -> List[str]:
    return _lines

class DataType(Enum):
    LONG = (as_int_list, natural_order)
    WORD = (as_word_list, natural_order)
    LINE = (as_lines, length_order)
