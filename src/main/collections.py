from typing import List


class Inventory:
    def __init__(self, *items: str):
        self.list: List[str] = []
        for item in items:
            self.list.append(item)

    def get_item_quantity(self, item: str) -> int:
        return self.list.count(item)

    def add_item_to_inventory(self, item: str):
        self.list.append(item)

    def remove_item_from_inventory(self, item: str):
        self.list.remove(item)


class MonthConversion:
    def __init__(self):
        self.map = {}

    def add(self, month: int, name: str):
        self.map[month] = name

    def size(self):
        return len(self.map)

    def get_name(self, month: int) -> str or None:
        if month not in self.map:
            return None
        return self.map[month]

    def get_number(self, name_lookup: str) -> int or None:
        for month in self.map:
            if self.map[month] == name_lookup:
                return month
        return None

    def update(self, month: int, name: str):
        self.map[month] = name

    def is_valid_number(self, month: int) -> bool:
        return month in self.map

    def is_valid_month(self, name_check: str) -> bool:
        for month in self.map:
            if self.map[month] == name_check:
                return True
        return False
