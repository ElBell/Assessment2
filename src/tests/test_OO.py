from unittest import TestCase

from src.main.OO import Address, Person, Animal, Dog, Woofer


class AddressConstructorTest(TestCase):
    def testNullaryConstructor(self):
        expected_line1 = ""
        expected_line2 = ""
        expected_city = ""
        expected_state = ""
        expected_zipcode = ""
        address = Address()
        self.assertEqual(expected_line1, address.address_line1)
        self.assertEqual(expected_line2, address.address_line2)
        self.assertEqual(expected_city, address.city)
        self.assertEqual(expected_state, address.state)
        self.assertEqual(expected_zipcode, address.zipcode)

    def testNonNullaryConstructor(self):
        expected_line1 = "123 Gitlabs"
        expected_line2 = ""
        expected_city = "New Castle"
        expected_state = "Delaware"
        expected_zipcode = "19720"
        address = Address(expected_line1, expected_line2, expected_city, expected_state, expected_zipcode)
        self.assertEqual(expected_line1, address.address_line1)
        self.assertEqual(expected_line2, address.address_line2)
        self.assertEqual(expected_city, address.city)
        self.assertEqual(expected_state, address.state)
        self.assertEqual(expected_zipcode, address.zipcode)


class AddressEqualsTest(TestCase):
    def checkDefaultAddressEquivalence(self):
        address1 = Address()
        address2 = Address()
        outcome = address1 == address2
        self.assertTrue(outcome)

    def checkNonDefaultAddressEquivalence(self):
        provided_line1 = "123 Gitlabs"
        provided_line2 = ""
        provided_city = "New Castle"
        provided_state = "Delaware"
        provided_zipcode = "19720"
        address1 = Address(provided_line1, provided_line2, provided_city, provided_state, provided_zipcode)
        address2 = Address(provided_line1, provided_line2, provided_city, provided_state, provided_zipcode)
        outcome = address1 == address2
        self.assertTrue(outcome)

    def checkNonDefaultAddressNonEquivalence(self):
        provided_line1 = "123 Gitlabs"
        provided_line2 = ""
        provided_city = "New Castle"
        provided_state = "Delaware"
        provided_zipcode = "19720"
        address1 = Address(provided_line1, provided_line2, provided_city, provided_state, provided_zipcode)
        address2 = Address(provided_line1, provided_line2, provided_city, provided_state, "Different Zip")
        outcome = address1 == address2
        self.assertFalse(outcome)


class AddressToStringTest(TestCase):
    def testNullaryConstructor(self):
        expected = "Address{addressLine1='', addressLine2='', city='', state='', zipcode=''}"
        address = Address()
        actual = str(address)
        self.assertEqual(expected, actual)

    def testNonNullaryConstructor(self):
        provided_line1 = "123 Gitlabs"
        provided_line2 = ""
        provided_city = "New Castle"
        provided_state = "Delaware"
        provided_zipcode = "19720"
        address = Address(provided_line1, provided_line2, provided_city, provided_state, provided_zipcode)
        expected = "Address{addressLine1='123 Gitlabs', addressLine2='', city='New Castle', state='Delaware', " \
                   "zipcode='19720'}"
        actual = str(address)
        self.assertEqual(expected, actual)


class SetAddressLine1(TestCase):
    def test1(self):
        address = Address()
        expected = "123 Cool Street"
        address.address_line1 = expected
        actual = address.address_line1
        self.assertEqual(expected, actual)

    def test2(self):
        address = Address()
        expected = "587 The Lane"
        address.address_line1 = expected
        actual = address.address_line1
        self.assertEqual(expected, actual)


class SetAddressLine2(TestCase):
    def test1(self):
        address = Address()
        expected = "123 Cool Street"
        address.address_line2 = expected
        actual = address.address_line2
        self.assertEqual(expected, actual)

    def test2(self):
        address = Address()
        expected = "587 The Lane"
        address.address_line2 = expected
        actual = address.address_line2
        self.assertEqual(expected, actual)


class SetCityTest(TestCase):
    def test1(self):
        address = Address()
        expected = "Philadelphia"
        address.city = expected
        actual = address.city
        self.assertEqual(expected, actual)

    def test2(self):
        address = Address()
        expected = "New York"
        address.city = expected
        actual = address.city
        self.assertEqual(expected, actual)


class SetStateTest(TestCase):
    def test1(self):
        address = Address()
        expected = "Pennsylvania"
        address.state = expected
        actual = address.state
        self.assertEqual(expected, actual)

    def test2(self):
        address = Address()
        expected = "Maryland"
        address.state = expected
        actual = address.state
        self.assertEqual(expected, actual)


class SetZipCodeTest(TestCase):
    def test1(self):
        address = Address()
        expected = "19720"
        address.zipcode = expected
        actual = address.zipcode
        self.assertEqual(expected, actual)

    def test2(self):
        address = Address()
        expected = "18713"
        address.zipcode = expected
        actual = address.zipcode
        self.assertEqual(expected, actual)


class AnimalConstructorTest(TestCase):
    def NonearyConstructor(self):
        expected_owner = Person()
        expected = expected_owner.address
        expected_id = None
        animal = Animal()
        actual_owner = animal.owner
        actual = animal.owner.address
        actual_id = animal.id
        self.assertEqual(expected_id, actual_id)
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected, actual)

    def nonNullaryConstructor(self):
        expected_owner = Person(None, None, Address())
        expected = expected_owner.address
        expected_id = None
        animal = Animal(expected_id, expected_owner)
        actual_owner = animal.owner
        actual = animal.owner.address
        actual_id = animal.id
        self.assertEqual(expected_id, actual_id)
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected, actual)


class SetOwnerTest(TestCase):
    def setOwnerTest1(self):
        animal = Animal()
        expected = Address("123 MyAddress", "", "", "DE", "")
        expected_owner = Person(0, "", expected)
        animal.owner = expected_owner
        actual_owner = animal.owner
        actual = animal.owner.address
        self.assertEqual(expected, actual)
        self.assertEqual(expected_owner, actual_owner)

    def setOwnerTest2(self):
        animal = Animal()
        expected = Address("789 MyAddress", "", "", "AZ", "")
        expected_owner = Person(10, "", expected)
        animal.owner = expected_owner
        actual_owner = animal.owner
        actual = animal.owner.address
        self.assertEqual(expected, actual)
        self.assertEqual(expected_owner, actual_owner)


class DogTest(TestCase):
    def testInheritance(self):
        dog = Dog()
        self.assertTrue(isinstance(dog, Animal))

    def test_implementation(self):
        dog = Dog()
        self.assertTrue(isinstance(dog, Woofer))

    def testSpeak(self):
        dog = Dog()
        expected = "Woof!\nWoof!"
        actual = dog.speak()
        self.assertEqual(expected, actual)


class PersonConstructorTest(TestCase):
    def testNullaryConstructor(self):
        person = Person()
        expected_id = -99999
        expected_name = ""
        expected = Address()
        actual_id = person.id
        actual_name = person.name
        actual = person.address
        self.assertEqual(expected_id, actual_id)
        self.assertEqual(expected_name, actual_name)
        self.assertEqual(str(expected), str(actual))

    def testConstructor(self):
        expected_id = 99999
        expected_name = "PersonName"
        expected = Address("line1", "line2", "city", "state", "99999")
        person = Person(expected_id, expected_name, expected)
        actual_id = person.id
        actual_name = person.name
        actual = person.address
        self.assertEqual(expected_id, actual_id)
        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected, actual)


class PersonEqualsTest(TestCase):
    def checkDefaultPersonEquivalence(self):
        person1 = Person()
        person2 = Person()
        outcome = person1 == person2
        self.assertTrue(outcome)

    def checkDefaultPersonNonEquivalence(self):
        person1 = Person(None, "PersonName", None)
        person2 = Person()
        outcome = person1 == person2
        self.assertFalse(outcome)

    def checkNonDefaultPersonEquivalence(self):
        person1 = Person(None, "PersonName", None)
        person2 = Person(None, "PersonName", None)
        outcome = person1 == person2
        self.assertTrue(outcome)


class PersonToStringTest(TestCase):
    def testNullaryConstructor(self):
        person = Person()
        expected = "Person{id=-99999, name='', address=Address{addressLine1='', addressLine2='', " \
                   "city='', state='', zipcode=''}"
        actual = str(person)
        self.assertEqual(expected, actual)

    def testConstructor(self):
        id = 99999
        name = "PersonName"
        address = Address("line1", "line2", "city", "state", "99999")
        expected = "Person{id=99999, name='PersonName', address=Address{addressLine1='line1', " \
                   "addressLine2='line2', city='city', state='state', zipcode='99999'}"
        person = Person(id, name, address)
        actual = str(person)
        self.assertEqual(expected, actual)


class SetAddressTest(TestCase):
    def test1(self):
        person = Person()
        expected = Address()
        person.address = expected
        actual = person.address
        self.assertEqual(expected, actual)

    class SetIdTest(TestCase):
        def test1(self):
            person = Person()
            expected = 99999
            person.id = expected
            actual = person.id
            self.assertEqual(expected, actual)

        def test2(self):
            person = Person()
            expected = -99999
            person.id = expected
            actual = person.id
            self.assertEqual(expected, actual)


class SetNameTest(TestCase):
    def test1(self):
        person = Person()
        expected = "My Name"
        person.name = expected
        actual = person.name
        self.assertEqual(expected, actual)

    def test2(self):
        person = Person()
        expected = "My Namee"
        person.name = expected
        actual = person.name
        self.assertEqual(expected, actual)
