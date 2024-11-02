import argparse
import math
from pprint import pprint
from typing import List

parser = argparse.ArgumentParser()
parser.add_argument("-dataType",
                    default="word",
                    choices=["word","line","long"])
parser.add_argument("-sortIntegers", action="store_true")

def check_numbers(numbers: List[int]):
    print(f"Total numbers: {len(numbers)}.")
    max_no = max(numbers)
    count_max = numbers.count(max_no)
    percent = math.floor(count_max / len(numbers) * 100)
    print(f"The greatest number: {max_no} ({count_max} time(s), {percent}%).")


def check_word(words: List[str]):
    print(f"Total words: {len(words)}.")
    words.sort(key=lambda x: len(x), reverse=True)
    longest = words[0]
    count = words.count(longest)
    percent = math.floor(count / len(words) * 100)
    print(f"The longest word: {longest} ({count} time(s), {percent:.0f}%).")


def check_lines(_lines: List[str]):
    print(f"Total lines: {len(_lines)}.")
    _lines.sort(key=lambda x: len(x), reverse=True)
    longest = _lines[0]
    count = _lines.count(longest)
    percent = math.floor(count / len(_lines) * 100)
    print(f"The longest line:\n{longest}\n({count} time(s), {percent:.0f}%).")


def sort_integers(numbers: List[int]):
    print(f"Total numbers: {len(numbers)}.")
    numbers.sort()
    print_ready = " ".join(map(str, numbers))
    print(f"Sorted data: {print_ready}")


def as_int_list(_lines: List[str]) -> List[int]:
    numbers = []
    for line in _lines:
        numbers.extend(int(date) for date in line.split())
    return numbers


def as_word_list(_lines):
    words = []
    for line in _lines:
        words.extend(line.split())
    return words


def get_input() -> List[str]:
    line_list = []
    while True:
        try:
            line_list.append(input())
        except EOFError:
            break
    return line_list


if __name__ == "__main__":
    lines = get_input()
    if parser.parse_args().sortIntegers:
        sort_integers(as_int_list(lines))
    else:
        match (data_type := parser.parse_args().dataType):
            case "word": check_word(as_word_list(lines))
            case "line": check_lines(lines)
            case "long": check_numbers(as_int_list(lines))

