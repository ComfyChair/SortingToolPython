import argparse
from typing import List

from data_type import DataType
from sorting_type import SortingType

parser = argparse.ArgumentParser()
parser.add_argument("-dataType",
                    choices=["word","line","long"],
                    default="word")
parser.add_argument("-sortingType",
                    choices=["natural","byCount"],
                    default="natural")


def get_input() -> List[str]:
    line_list = []
    while True:
        try:
            line_list.append(input())
        except EOFError:
            break
    return line_list


if __name__ == "__main__":
    data_type = DataType[parser.parse_args().dataType.upper()]
    sort_type = SortingType[parser.parse_args().sortingType.upper()]
    raw_data = get_input()

    sort_type.value["fct"](raw_data, data_type)

