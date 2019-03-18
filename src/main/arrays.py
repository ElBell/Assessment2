from typing import Any, List


class IntegerArrayUtils:
    @staticmethod
    def add(list_input1: List[Any], value: Any) -> List[Any]:
        list_input1.append(value)
        return list_input1

    @staticmethod
    def decrement_odd(list_input: List[int]) -> List[int]:
        return [n-1 if n % 2 != 0 else n for n in list_input]

    @staticmethod
    def increment_even(list_input: List[int]) -> List[int]:
        return [n+1 if n % 2 == 0 else n for n in list_input]

    @staticmethod
    def increment_even_decrement_odd(list_input: List[int]) -> List[int]:
        return [n+1 if n % 2 == 0 else n - 1 for n in list_input]

    @staticmethod
    def get(list_input: List[Any], index: int) -> Any:
        return list_input[index]

    @staticmethod
    def replace(list_input: List[Any], index: int, value: Any) -> List[Any]:
        list_input[index] = value
        return list_input


class StringArrayUtils:
    @staticmethod
    def get_sub_array(list_input: List[Any], start: int, end: int) -> List[Any]:
        if start > len(list_input) or start < 0:
            raise IndexError
        return list_input[start: end]

    @staticmethod
    def get_ending_array(list_input: List[Any], start: int):
        if start > len(list_input) or start < 0:
            raise IndexError
        return list_input[start:]
