

class Address:
    def __init__(self, address_line1: str = "", address_line2: str = "", city: str = "", state:str = "", zipcode: str = ""):
        self.address_line1: str = address_line1
        self.address_line2: str = address_line2
        self.city: str = city
        self.state: str = state
        self.zipcode: str = zipcode

    def __str__(self):
        return ("Address{" + "addressLine1='" + self.address_line1 + '\'' + ", addressLine2='" + self.address_line2 +
                '\'' +", city='" + self.city + '\'' + ", state='" + self.state + '\'' +
                ", zipcode='" + self.zipcode + '\'' + '}')


class Person:
    def __init__(self, id: int = -99999, name: str = "", address: Address = Address()):
        self.id: int = id
        self.name: str = name
        self.address: Address = address

    def __str__(self):
        return ("Person{" +
                "id=" + str(self.id) +
                ", name='" + self.name + '\'' +
                ", address=" + str(self.address))


class Animal:
    def __init__(self, id: int = None, owner: Person = Person()):
        self.id: int = id
        self.owner: Person = owner


class Woofer(Animal):
    def __init__(self):
        super().__init__()


class Dog(Woofer):
    def __init__(self):
        super().__init__()

    def speak(self) -> str:
        return "Woof!\nWoof!"
