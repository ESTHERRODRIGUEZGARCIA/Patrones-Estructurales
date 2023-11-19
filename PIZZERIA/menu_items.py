from combo_composite import ComboItem

class Entrante(ComboItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        return self.name

    def get_price(self):
        return self.price

class Pizza(ComboItem):
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