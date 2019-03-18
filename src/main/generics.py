from collections import Iterable
from typing import List, Generic, TypeVar, Iterator, Any


class Ageable:
    def __init__(self, year_born: int = 2):
        self.year_born = year_born

class Person(Ageable):
    def __init__(self):
        super().__init__()


class Dog(Ageable):
    def __init__(self):
        super().__init__()


class Cat(Ageable):
    def __init__(self):
        super().__init__()


A = TypeVar('A', bound=Ageable)


class Shelter(Generic[A], Iterable):
    def __iter__(self) -> Iterator[Any]:
        return iter(self.list_ageable)

    def __init__(self, ):
        self.list_ageable: List[A] = []

    def size(self) -> int:
        return len(self.list_ageable)

    def add(self, new: A):
        self.list_ageable.append(new)

    def contains(self, check: A) -> bool:
        return check in self.list_ageable

    def remove(self, remove: A):
        self.list_ageable.remove(remove)

    def get(self, index: int) -> A:
        return self.list_ageable[index]

    def get_index_of(self, index_object: A):
        return self.list_ageable.index(index_object)

    def iterator(self) -> iter:
        return iter(self.list_ageable)
