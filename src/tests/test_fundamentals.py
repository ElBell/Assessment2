from unittest import TestCase

from src.main.fundamentals import BasicStringUtils, PredicateUtilities, StringUtils


class ConcatenateTest(TestCase):
    def test1(self):
        self.util("The", "Quick", "TheQuick")

    def test2(self):
        self.util("Brown", "Fox", "BrownFox")

    def test3(self):
        self.util("Jumps", "Over", "JumpsOver")

    def util(self, string1, string2, expected_string):
        actual = BasicStringUtils.concatenate(string1, string2)
        self.assertEqual(expected_string, actual)


class RemoveCharactersTest(TestCase):
    def test1(self):
        self.util("racecar", "r", "aceca")

    def test2(self):
        self.util("basketball", "b", "asketall")

    def test3(self):
        self.util("basketball", "teks", "baball")

    def test4(self):
        self.util("football", "fto", "ball")

    def util(self, string, characters_to_remove, expected_string):
        actual = BasicStringUtils.remove_characters(string, characters_to_remove)
        self.assertEqual(expected_string, actual)


class RemoveCharactersThenReverseTest(TestCase):
    def test1(self):
        self.util("Feelers", "er", "slF")

    def test2(self):
        self.util("Takers", "ers", "kaT")

    def test3(self):
        self.util("Takers", "res", "kaT")

    def test4(self):
        self.util("breaking", "kaer", "gnib")

    def util(self, string_to_manipulate, characters_to_remove, expected):
        actual = BasicStringUtils.remove_characters_then_reverse(string_to_manipulate, characters_to_remove)
        self.assertEqual(expected, actual)


class ReverseTest(TestCase):
    def test1(self):
        self.util("The", "ehT")

    def test2(self):
        self.util("Quick", "kciuQ")

    def test3(self):
        self.util("Brown", "nworB")

    def test4(self):
        self.util("Fox", "xoF")

    def util(self, string, expected_string):
        actual = BasicStringUtils.reverse(string)
        self.assertEqual(expected_string, actual)


class ReverseThenConcatenateTest(TestCase):
    def test1(self):
        self.util("The", "Quick", "ehTkciuQ")

    def test2(self):
        self.util("Brown", "Fox", "nworBxoF")

    def test3(self):
        self.util("Jumps", "Over", "spmuJrevO")

    def util(self, string1, string2, expected_string):
        actual = BasicStringUtils.reverse_then_concatenate(string1, string2)
        self.assertEqual(expected_string, actual)


class IsEvenTest(TestCase):
    def test1(self):
        self.util(0, True)

    def test2(self):
        self.util(1, False)

    def test3(self):
        self.util(2, True)

    def test4(self):
        self.util(3, False)

    def util(self, value, expected_outcome):
        actual_outcome = PredicateUtilities.is_even(value)
        self.assertEqual(actual_outcome, expected_outcome)


class IsMultipleOf3Test(TestCase):
    def test1(self):
        self.util(1, False)

    def test2(self):
        self.util(3, True)

    def test3(self):
        self.util(7, False)

    def test4(self):
        self.util(6, True)

    def test5(self):
        self.util(9, True)

    def util(self, value, expected_outcome):
        actual_outcome = PredicateUtilities.is_multiple_3(value)
        self.assertEqual(actual_outcome, expected_outcome)


class IsMultipleOfNTest(TestCase):
    def test1(self):
        self.util(1, 2, False)

    def test2(self):
        self.util(3, 3, True)

    def test3(self):
        self.util(7, 5, False)

    def test4(self):
        self.util(8, 4, True)

    def test5(self):
        self.util(12, 6, True)

    def util(self, value, multiple, expected_outcome):
        actual_outcome = PredicateUtilities.is_multiple_n(value, multiple)
        self.assertEqual(actual_outcome, expected_outcome)


class IsOddTest(TestCase):
    def test1(self):
        self.util(0, False)

    def test2(self):
        self.util(1, True)

    def test3(self):
        self.util(2, False)

    def test4(self):
        self.util(3, True)

    def util(self, value, expected_outcome):
        actual_outcome = PredicateUtilities.is_odd(value)
        self.assertEqual(actual_outcome, expected_outcome)


class StartsWithCapitalLetterTest(TestCase):
    def test1(self):
        self.util("The", True)

    def test2(self):
        self.util("quick", False)

    def test3(self):
        self.util("%^&*", False)

    def test4(self):
        self.util("fox", False)

    def test5(self):
        self.util("Jumps", True)

    def util(self, value, expected_outcome):
        actual_outcome = PredicateUtilities.starts_with_capital_letter(value)
        self.assertEqual(actual_outcome, expected_outcome)


class IsAlphaTest(TestCase):
    def alpha_stringTest1(self):
        alpha_string = "The quick brown fox jumps"
        outcome = StringUtils.is_alpha_string(alpha_string)
        self.assertTrue(outcome)

    def alpha_stringTest2(self):
        alpha_string = "Over the lazy dog"
        outcome = StringUtils.is_alpha_string(alpha_string)
        self.assertTrue(outcome)

    def numericStringTest1(self):
        alpha_string = "1234"
        outcome = StringUtils.is_alpha_string(alpha_string)
        self.assertFalse(outcome)

    def numericStringTest2(self):
        alpha_string = "Over the lazy dog1"
        outcome = StringUtils.is_alpha_string(alpha_string)
        self.assertFalse(outcome)

    def specialCharacterStringTest1(self):
        alpha_string = "!&*("
        outcome = StringUtils.is_alpha_string(alpha_string)
        self.assertFalse(outcome)

    def specialCharacterStringTest2(self):
        alpha_string = "Over the lazy dog!"
        outcome = StringUtils.is_alpha_string(alpha_string)
        self.assertFalse(outcome)


class IsNumericTest(TestCase):
    def alpha_stringTest1(self):
        alpha_string = "The quick brown fox jumps"
        outcome = StringUtils.is_numeric_string(alpha_string)
        self.assertFalse(outcome)

    def alpha_stringTest2(self):
        alpha_string = "Over the lazy dog"
        outcome = StringUtils.is_numeric_string(alpha_string)
        self.assertFalse(outcome)


class IsSpecialCharacter(TestCase):
    def alpha_stringTest1(self):
        alpha_string = "The quick brown fox jumps"
        outcome = StringUtils.is_special_character_string(alpha_string)
        self.assertFalse(outcome)

    def alpha_stringTest2(self):
        alpha_string = "Over the lazy dog"
        outcome = StringUtils.is_special_character_string(alpha_string)
        self.assertFalse(outcome)

    def numericStringTest1(self):
        alpha_string = "1234"
        outcome = StringUtils.is_special_character_string(alpha_string)
        self.assertFalse(outcome)

    def numericStringTest2(self):
        alpha_string = "Over the lazy dog1"
        outcome = StringUtils.is_special_character_string(alpha_string)
        self.assertFalse(outcome)

    def specialCharacterStringTest1(self):
        alpha_string = "!&*("
        outcome = StringUtils.is_special_character_string(alpha_string)
        self.assertTrue(outcome)

    def specialCharacterStringTest2(self):
        alpha_string = "Over the lazy dog!"
        outcome = StringUtils.is_special_character_string(alpha_string)
        self.assertFalse(outcome)


class PadLeftTest(TestCase):
    def pad_left10Test(self):
        hello = "hello"
        number_of_units_to_pad = 10
        expected = "     hello"
        actual = StringUtils.pad_left(hello, number_of_units_to_pad)
        self.assertEqual(expected, actual)

    def pad_left15Test(self):
        hello = ""
        number_of_units_to_pad = 15
        expected = "               "
        actual = StringUtils.pad_left(hello, number_of_units_to_pad)
        self.assertEqual(expected, actual)

    def pad_left20Test(self):
        hello = "The quick"
        number_of_units_to_pad = 20
        expected = "           The quick"
        actual = StringUtils.pad_left(hello, number_of_units_to_pad)
        self.assertEqual(expected, actual)


class PadRightTest(TestCase):
    def pad_right10Test(self):
        hello = "hello"
        number_of_units_to_pad = 10
        expected = "hello     "
        actual = StringUtils.pad_right(hello, number_of_units_to_pad)
        self.assertEqual(expected, actual)

    def pad_right15Test(self):
        hello = ""
        number_of_units_to_pad = 15
        expected = "               "
        actual = StringUtils.pad_right(hello, number_of_units_to_pad)
        self.assertEqual(expected, actual)

    def pad_right20Test(self):
        hello = "The quick"
        number_of_units_to_pad = 20
        expected = "The quick           "
        actual = StringUtils.pad_right(hello, number_of_units_to_pad)
        self.assertEqual(expected, actual)


class RepeatStringTest(TestCase):
    def testRepeatHello5Times(self):
        string_to_repeat = "Hello"
        number_of_times_to_repeat = 5
        expected = string_to_repeat * number_of_times_to_repeat
        actual = StringUtils.repeat_string(string_to_repeat, number_of_times_to_repeat)
        self.assertEqual(expected, actual)

    def testRepeatQuickBrown6Times(self):
        string_to_repeat = "Quick Brown"
        number_of_times_to_repeat = 6
        expected = string_to_repeat * number_of_times_to_repeat
        actual = StringUtils.repeat_string(string_to_repeat, number_of_times_to_repeat)
        self.assertEqual(expected, actual)
