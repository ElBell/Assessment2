from typing import List, Any


class BasicStringUtils:
    @staticmethod
    def concatenate(str1: str, str2: str) -> str:
        return str1 + str2

    @staticmethod
    def remove_characters(string_input: str, characters: str) -> str:
        for letter in characters:
            string_input = string_input.replace(letter, "")
        return string_input

    @staticmethod
    def remove_characters_then_reverse(string_input: str, characters: str) -> str:
        return BasicStringUtils.remove_characters(string_input, characters)[::-1]

    @staticmethod
    def reverse(string_input: str) -> str:
        return string_input[::-1]

    @staticmethod
    def reverse_then_concatenate(str1: str, str2: str) -> str:
        return BasicStringUtils.reverse(str1) + BasicStringUtils.reverse(str2)


class PredicateUtilities:
    @staticmethod
    def is_even(number: int) -> bool:
        return PredicateUtilities.is_multiple_n(number, 2)

    @staticmethod
    def is_multiple_3(number: int) -> bool:
        return PredicateUtilities.is_multiple_n(number, 3)

    @staticmethod
    def is_multiple_n(number: int, n: int) -> bool:
        return number % n == 0

    @staticmethod
    def is_odd(number: int) -> bool:
        return number % 2 != 0

    @staticmethod
    def starts_with_capital_letter(string: str) -> bool:
        return string[0].isupper()


class StringUtils:
    @staticmethod
    def is_alpha_string(string: str) -> bool:
        return string.isalpha()

    @staticmethod
    def is_numeric_string(string: str) -> bool:
        return string.isnumeric()

    @staticmethod
    def is_special_character_string(string: str) -> bool:
        return string.isalnum()

    @staticmethod
    def pad_left(string: str, pad_num: int) -> str:
        return ("%" + str(pad_num) + "s").format(string)

    @staticmethod
    def pad_right(string: str, pad_num: int) -> str:
        return ("%-" + str(pad_num) + "s").format(string)

    @staticmethod
    def repeat_string(string: str, num_repeat: int) -> str:
        return string * num_repeat
