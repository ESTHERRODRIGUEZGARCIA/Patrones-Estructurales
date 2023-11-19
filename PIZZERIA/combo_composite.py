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
    def __init__(self, name):
        self.name = name
        self.items = {
            'entrantes': [],
            'pizzas': [],
            'bebidas': [],
            'postres': []
        }
        self.discount = 0

    def add_item(self, item, category):
        self.items[category].append(item)

    def get_description(self):
        return f"{self.name} Combo"
    
    def get_items(self):
        return self.items

    def get_price(self):
        total_price = sum(item.get_price() for item in self.items)
        discounted_price = total_price - (total_price * self.discount)
        return discounted_price

    def apply_discount(self):
        if self.name == "Couple":
            self.discount = 0.05
        elif self.name == "Trio":
            self.discount = 0.1
        elif self.name == "Family":
            self.discount = 0.15
        elif self.name == "Super":
            self.discount = 0.2

class Entrante(ComboItem):
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def get_description(self):
        return f"{self.name} - {', '.join(self.ingredients)}"

    def get_price(self):
        return self.price

class PizzaMenu(ComboItem):
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def get_description(self):
        return f"{self.name} - {', '.join(self.ingredients)}"

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