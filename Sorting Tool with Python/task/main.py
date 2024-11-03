from typing import List

from arg_parser import ArgParser
from data import DataType, DataWrapper
from sorting_type import SortingType

parser = ArgParser()


def get_input() -> List[str]:
    line_list = []
    while True:
        try:
            line_list.append(input())
        except EOFError:
            break
    return line_list


if __name__ == "__main__":
    args = parser.parse_args()
    data_type = DataType[args.dataType.upper()]
    sort_type = SortingType(args.sortingType)
    raw_data = get_input()

    data_wrapper = DataWrapper(raw_data, data_type, sort_type)
    data_wrapper.print()
