from enum import Enum

from data_type import DataType


class SortingType(Enum):
    @staticmethod
    def sort_naturally(_raw_data: list, data_type: DataType):
        data = _raw_data
        print(f"raw: {data}")
        data = data_type.value[0](data)
        data.sort(key=data_type.value[1](data))
        print(f"sorted: {data}")
        print_ready = " ".join(map(str, data))
        print(f"Sorted data: {print_ready}")

    @staticmethod
    def sort_by_count(data):
        pass

    NATURAL = {"fct": sort_naturally}
    BY_COUNT = {"fct": sort_by_count}







