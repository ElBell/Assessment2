from unittest import TestCase

from src.main.arrays import IntegerArrayUtils, StringArrayUtils


class AddTest(TestCase):
    def testAdd1(self):
        value_to_be_added = 10
        int_array = [1, 3, 2, 5, 4, 7, 6]
        expected = [1, 3, 2, 5, 4, 7, 6, value_to_be_added]
        actual = IntegerArrayUtils.add(int_array, value_to_be_added)
        self.assertEqual(expected, actual)

    def testAdd2(self):
        first_value_tobe_added = 10
        second_value_tobe_added = 17
        int_array = [1, 3, 2, 5, 4, 7, 6]
        expected = [1, 3, 2, 5, 4, 7, 6, first_value_tobe_added, second_value_tobe_added]
        actual = IntegerArrayUtils.add(int_array, first_value_tobe_added)
        actual = IntegerArrayUtils.add(actual, second_value_tobe_added)
        self.assertEqual(expected, actual)


class DecrementOddTest(TestCase):
    def firstTest(self):
        test_input = [2, 4, 6, 11, 13, 15]
        expected = [2, 4, 6, 10, 12, 14]
        actual = IntegerArrayUtils.decrement_odd(test_input)
        self.assertEqual(expected, actual)

    def secondTest(self):
        test_input = [10, 20, 30, 1, 3, 5]
        expected = [10, 20, 30, 0, 2, 4]
        actual = IntegerArrayUtils.decrement_odd(test_input)
        self.assertEqual(expected, actual)


class GetTest(TestCase):
    def testGet1(self):
        index_to_fetch = 3
        test_input = [1, 2, 5, 178931798]
        expected = 178931798
        actual = IntegerArrayUtils.get(test_input, index_to_fetch)
        self.assertEqual(expected, actual)

    def testGet2(self):
        index_to_fetch = 0
        test_input = [981238912, 2, 5, 8]
        expected = 981238912
        actual = IntegerArrayUtils.get(test_input, index_to_fetch)
        self.assertEqual(expected, actual)


class IncrementEvenDecrementOddTest(TestCase):
    def testOneEvenElement(self):
        test_input3 = [38]
        expected_output3 = [39]
        actual3 = IntegerArrayUtils.increment_even_decrement_odd(test_input3)
        self.assertEqual(expected_output3, actual3)

    def testOneOddElement(self):
        test_input4 = [91]
        expected_output4 = [90]
        actual4 = IntegerArrayUtils.increment_even_decrement_odd(test_input4)
        self.assertEqual(expected_output4, actual4)

    def testOdd(self):
        test_input1 = [101, 25, 11]
        expected_output1 = [100, 24, 10]
        actual1 = IntegerArrayUtils.increment_even_decrement_odd(test_input1)
        self.assertEqual(expected_output1, actual1)

    def testEven(self):
        test_input2 = [34, 18, 700, 128, 110]
        expected_output2 = [35, 19, 701, 129, 111]
        actual2 = IntegerArrayUtils.increment_even_decrement_odd(test_input2)
        self.assertEqual(expected_output2, actual2)


class IncrementEvenTest(TestCase):
    def test1(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = [1, 3, 3, 5, 5, 7, 7, 9]
        actual = IntegerArrayUtils.increment_even(test_input)
        self.assertEqual(expected, actual)

    def test2(self):
        test_input = [10, 20, 30, 1, 3, 5]
        expected = [11, 21, 31, 1, 3, 5]
        actual = IntegerArrayUtils.increment_even(test_input)
        self.assertEqual(expected, actual)


class ReplaceTest(TestCase):
    def testInsert1(self):
        index_to_insert_at = 3
        value_to_be_inserted = 12
        test_input = [1, 2, 5, 8]
        expected = [1, 2, 5, value_to_be_inserted]
        actual = IntegerArrayUtils.replace(test_input, index_to_insert_at, value_to_be_inserted)
        self.assertEqual(expected, actual)

    def testInsert2(self):
        value_to_be_inserted = 82
        index_to_insert_at = 0
        test_input = [1, 2, 5, 8]
        expected = [value_to_be_inserted, 2, 5, 8]
        actual = IntegerArrayUtils.replace(test_input, index_to_insert_at, value_to_be_inserted)
        self.assertEqual(expected, actual)


class GetEndingArrayTest(TestCase):
    def testGetEndingArrayFrom0(self):
        test_input = ["The", "Quick", "Brown", "Fox", "Jumps"]
        expected = ["The", "Quick", "Brown", "Fox", "Jumps"]
        start_index = 0
        actual = StringArrayUtils.get_ending_array(test_input, start_index)
        self.assertEqual(expected, actual)

    def testGetEndingArrayFrom1(self):
        test_input = ["The", "Quick", "Brown", "Fox", "Jumps"]
        expected = ["Quick", "Brown", "Fox", "Jumps"]
        start_index = 1
        actual = StringArrayUtils.get_ending_array(test_input, start_index)
        self.assertEqual(expected, actual)

    def testGetEndingArrayOutOfBounds1(self):
        test_input = ["The", "Quick", "Brown", "Fox", "Jumps"]
        start_index = 98
        with self.assertRaises(IndexError):
            StringArrayUtils.get_ending_array(test_input, start_index)

    def testGetEndingArrayOutOfBounds2(self):
        test_input = ["The", "Quick", "Brown", "Fox", "Jumps"]
        start_index = -1
        with self.assertRaises(IndexError):
            StringArrayUtils.get_ending_array(test_input, start_index)


class GetSubArrayTest(TestCase):

    def testGetSubArrayFrom0To2(self):
        test_input = ["The", "Quick", "Brown", "Fox", "Jumps"]
        expected = ["The", "Quick"]
        start_index = 0
        end_index = 2
        actual = StringArrayUtils.get_sub_array(test_input, start_index, end_index)
        self.assertEqual(expected, actual)

    def testGetSubArrayFrom1To3(self):
        test_input = ["The", "Quick", "Brown", "Fox", "Jumps"]
        expected = ["Quick", "Brown"]
        start_index = 1
        end_index = 3
        actual = StringArrayUtils.get_sub_array(test_input, start_index, end_index)
        self.assertEqual(expected, actual)

    def testGetSubArrayOutOfBounds1(self):
        test_input = ["The", "Quick", "Brown", "Fox", "Jumps"]
        start_index = 98
        end_index = 99
        with self.assertRaises(IndexError):
            StringArrayUtils.get_sub_array(test_input, start_index, end_index)

    def testGetSubArrayOutOfBounds2(self):
        test_input = ["The", "Quick", "Brown", "Fox", "Jumps"]
        start_index = -1
        end_index = -10
        with self.assertRaises(IndexError):
            StringArrayUtils.get_sub_array(test_input, start_index, end_index)
