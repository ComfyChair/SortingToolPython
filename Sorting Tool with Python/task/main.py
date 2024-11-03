import argparse
from typing import List

from data import DataType, DataWrapper
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
    sort_type = SortingType(parser.parse_args().sortingType)
    raw_data = get_input()

    data_wrapper = DataWrapper(raw_data, data_type, sort_type)
    data_wrapper.print()
