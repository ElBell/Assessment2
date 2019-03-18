from collections import Iterable, Collection
from unittest import TestCase

from src.main.generics import *


class ShelterAddRemoveContainsTest(TestCase):
    def test_person(self):
        number_of_person = 10
        supplier = Person
        shelter = Shelter()
        self.util(number_of_person, supplier, shelter)

    def test_dog(self):
        number_of_person = 10
        supplier = Dog
        shelter = Shelter()
        self.util(number_of_person, supplier, shelter)

    def test_cat(self):
        number_of_person = 10
        supplier = Cat
        shelter = Shelter()
        self.util(number_of_person, supplier, shelter)

    def util(self, number_of_elements, supplier, shelter):
        for i in range(number_of_elements):
            ageable = supplier()
            shelter.add(ageable)
            self.assertTrue(shelter.contains(ageable))
            shelter.remove(ageable)
            self.assertFalse(shelter.contains(ageable))


class ShelterGetIndexOfTest(TestCase):
    def test_person(self):
        number_of_person = 10
        supplier = Person
        shelter = Shelter()
        self.util(number_of_person, supplier, shelter)

    def test_dog(self):
        number_of_person = 10
        supplier = Dog
        shelter = Shelter()
        self.util(number_of_person, supplier, shelter)

    def test_cat(self):
        number_of_person = 10
        supplier = Cat
        shelter = Shelter()
        self.util(number_of_person, supplier, shelter)

    def util(self, number_of_elements, supplier, shelter):
        for expected in range(number_of_elements):
            ageable = supplier()
            shelter.add(ageable)
            actual = shelter.get_index_of(ageable)
            self.assertEqual(expected, actual)


class ShelterGetTest(TestCase):
    def test_person(self):
        shelter = Shelter()
        ageable = Person()
        self.util(shelter, ageable)

    def test_dog(self):
        shelter = Shelter()
        ageable = Dog()
        self.util(shelter, ageable)

    def test_cat(self):
        shelter = Shelter()
        ageable = Cat()
        self.util(shelter, ageable)

    def util(self, shelter, expected):
        shelter.add(expected)
        actual = shelter.get(0)
        self.assertEqual(expected, actual)


class ShelterPolymorphismTest(TestCase):
    def test1(self):
        shelter = Shelter()
        self.assertFalse(isinstance(shelter, Collection))

    def test2(self):
        shelter = Shelter()
        self.assertTrue(isinstance(shelter, Iterable))


class ShelterSizeTest(TestCase):
    def test_person(self):
        number_of_person = 10
        supplier = Person
        self.util(number_of_person, supplier)

    def test_dog(self):
        number_of_person = 10
        supplier = Dog
        self.util(number_of_person, supplier)

    def test_cat(self):
        number_of_person = 10
        supplier = Cat
        self.util(number_of_person, supplier)

    def util(self, expected, supplier):
        shelter = Shelter()
        for i in range(expected):
            ageable = supplier()
            shelter.add(ageable)
        actual = shelter.size()
        self.assertEqual(expected, actual)
