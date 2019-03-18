from unittest import TestCase

from src.main.collections import Inventory, MonthConversion


class AddItemToInventroy(TestCase):
    def test0(self):
        self.util("")

    def test1(self):
        self.util("Lamp", "Lamp", "Shade", "Lightbulb")

    def test2(self):
        self.util("Lamp", "Lamp", "Shade", "Lightbulb", "Lightbulb")

    def test3(self):
        self.util("Lamp", "Lamp", "Shade", "Shade")

    def util(self, *items_to_add):
        inventory = Inventory()
        for item in items_to_add:
            pre_add_quantity = inventory.get_item_quantity(item)
            post_add_quantity = pre_add_quantity + 1
            expected = post_add_quantity
            inventory.add_item_to_inventory(item)
            actual = inventory.get_item_quantity(item)
            self.assertEqual(expected, actual)


class RemoveItemFrom(TestCase):
    def test1(self):
        item_to_be_removed = "Football"
        # items_tobe_added = "Baseball", "Baseball", "Basketball", item_to_be_removed
        self.util(item_to_be_removed, "Baseball", "Baseball", "Basketball", item_to_be_removed)

    def test2(self):
        item_to_be_removed = "Baseball"
        # items_tobe_added = item_to_be_removed, item_to_be_removed, "Basketball", "Football"
        self.util(item_to_be_removed, item_to_be_removed, item_to_be_removed, "Basketball", "Football")

    def test3(self):
        item_to_be_removed = "Basketball"
        # items_tobe_added = "Baseball", "Baseball", item_to_be_removed, "Football"
        self.util(item_to_be_removed, "Baseball", "Baseball", item_to_be_removed, "Football")

    def util(self, item_to_remove, *items_to_add):
        inventory = Inventory(*items_to_add)
        pre_removal_quantity = inventory.get_item_quantity(item_to_remove)
        expected_post_removal_quantity = pre_removal_quantity - 1
        inventory.remove_item_from_inventory(item_to_remove)
        actual_post_removal_quantity = inventory.get_item_quantity(item_to_remove)
        self.assertEqual(expected_post_removal_quantity, actual_post_removal_quantity)


class MonthConversionAddTest(TestCase):
    def testAdd1(self):
        conversion = MonthConversion()
        expected = 1
        conversion.add(1, "January")
        actual = conversion.size()
        self.assertEqual(expected, actual)

    def testAddMultiples(self):
        conversion = MonthConversion()
        expected = 4
        conversion.add(1, "January")
        conversion.add(2, "February")
        conversion.add(3, "March")
        conversion.add(4, "April")
        actual = conversion.size()
        self.assertEqual(expected, actual)


class MonthConversionGetNameNumberTest(TestCase):
    def testGetName_whenExist(self):
        conversion = MonthConversion()
        expected_month = "March"
        number = 3
        conversion.add(number, expected_month)
        actual_name = conversion.get_name(number)
        self.assertEqual(expected_month, actual_name)

    def testGetName_whenMultipleExist(self):
        conversion = MonthConversion()
        expected_month = "May"
        number = 5
        conversion.add(4, "April")
        conversion.add(number, expected_month)
        conversion.add(6, "June")
        actual_name = conversion.get_name(number)
        self.assertEqual(expected_month, actual_name)

    def testGetName_whenNotInThere(self):
        conversion = MonthConversion()
        conversion.add(4, "April")
        conversion.add(6, "June")
        actual_name = conversion.get_name(10)
        self.assertIsNone(actual_name)

    def testGetNumber_whenExist(self):
        conversion = MonthConversion()
        month = "March"
        expected_number = 3
        conversion.add(expected_number, month)
        actual_number = conversion.get_number(month)
        self.assertEqual(expected_number, actual_number)

    def testGetNumber_whenMultipleExist(self):
        conversion = MonthConversion()
        month = "May"
        expected_number = 5
        conversion.add(4, "April")
        conversion.add(expected_number, month)
        conversion.add(6, "June")
        actual_number = conversion.get_number(month)
        self.assertEqual(expected_number, actual_number)

    def test_get_number_when_not_in_there(self):
        conversion = MonthConversion()
        conversion.add(4, "April")
        conversion.add(6, "June")
        actual_number = conversion.get_number("aa")
        self.assertIsNone(actual_number)


class MonthConversionUpdateTest(TestCase):
    def testIsValidMonth_whenNotExist(self):
        conversion = MonthConversion()
        month = 5
        conversion.add(5, "April")
        expected_month = "May"
        conversion.update(month, expected_month)
        actual_month = conversion.get_name(month)
        self.assertEqual(expected_month, actual_month)


class MonthConversionValidTest(TestCase):
    def testIsValidNumber_whenExist(self):
        conversion = MonthConversion()
        expected_month = "March"
        number = 3
        conversion.add(number, expected_month)
        actual = conversion.is_valid_number(number)
        self.assertTrue(actual)

    def testIsValidNumber_whenNotExist(self):
        conversion = MonthConversion()
        expected_month = "March"
        number = 3
        conversion.add(number, expected_month)
        actual = conversion.is_valid_number(10)
        self.assertFalse(actual)

    def testIsValidMonth_whenExist(self):
        conversion = MonthConversion()
        month = "May"
        expected_number = 5
        conversion.add(4, "April")
        conversion.add(expected_number, month)
        conversion.add(6, "June")
        actual = conversion.is_valid_month(month)
        self.assertTrue(actual)

    def testIsValidMonth_whenNotExist(self):
        conversion = MonthConversion()
        conversion.add(4, "April")
        actual = conversion.is_valid_month("aa")
        self.assertFalse(actual)
