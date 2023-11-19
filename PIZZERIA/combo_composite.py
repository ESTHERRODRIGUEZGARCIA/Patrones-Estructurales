import csv
from abc import ABC, abstractmethod

class ComboItem(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Combo(ComboItem):
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_description(self):
        return f"{self.name} Combo"

    def get_price(self):
        total_price = sum(item.get_price() for item in self.items)
        total_price -= total_price * self.discount
        return total_price

class Entrante(ComboItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        return self.name

    def get_price(self):
        return self.price

class PizzaMenu(ComboItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        return self.name

    def get_price(self):
        return self.price

class Bebida(ComboItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        return self.name

    def get_price(self):
        return self.price

class Postre(ComboItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        return self.name

    def get_price(self):
        return self.price