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


def read_from_file() -> List[str]:
    try:
        with open(args.inputFile, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f'File not found: {args.inputFile}')
    except OSError:
        print(f'"Error while reading file: {args.inputFile}')


def write_to_file(content: str):
    try:
        with open(args.outputFile, 'w') as file:
            file.write(content)
    except OSError:
        print(f'"Error while writing file: {args.inputFile}')


if __name__ == "__main__":
    args = parser.parse_args()
    data_type = DataType[args.dataType.upper()]
    sort_type = SortingType(args.sortingType)

    if args.inputFile:
        raw_data = read_from_file()
    else:
        raw_data = get_input()
    data_wrapper = DataWrapper(raw_data, data_type, sort_type)

    if args.outputFile:
        write_to_file(data_wrapper.get_sorted())
    else:
        print(data_wrapper.get_sorted())

