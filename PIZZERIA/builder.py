from abc import ABC, abstractmethod
from pizza_customer import Customer, Pizza

# Define una interfaz para el constructor de Pizza
class PizzaBuilderInterface(ABC):
    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def set_category(self, category):
        pass

    @abstractmethod
    def set_ingredients(self, ingredients):
        pass

    @abstractmethod
    def build(self):
        pass

# Implementa el constructor de Pizza utilizando la interfaz
class PizzaBuilder(PizzaBuilderInterface):
    def __init__(self):
        self.pizza = Pizza()

    def set_name(self, name):
        self.pizza.name = name
        return self

    def set_category(self, category):
        self.pizza.category = category
        return self

    def set_ingredients(self, ingredients):
        self.pizza.ingredients = ingredients
        return self

    def build(self):
        return self.pizza

# Define una interfaz para el constructor de Customer
class CustomerBuilderInterface(ABC):
    @abstractmethod
    def set_customer_number(self, customer_number):
        pass

    @abstractmethod
    def set_pizza_masa(self, masa):
        pass

    @abstractmethod
    def set_salsa_base(self, salsa_base):
        pass

    @abstractmethod
    def set_ingredientes(self, ingredientes):
        pass

    @abstractmethod
    def set_tecnica_coccion(self, tecnica_coccion):
        pass

    @abstractmethod
    def set_presentacion(self, presentacion):
        pass

    @abstractmethod
    def set_bebida(self, bebida):
        pass

    @abstractmethod
    def set_extras(self, extras):
        pass

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def get_customer(self):
        pass

# Implementa el constructor de Customer utilizando la interfaz
class CustomerBuilder(CustomerBuilderInterface):
    def __init__(self):
        self.customer = Customer()

    def set_customer_number(self, customer_number):
        self.customer.customer_number = customer_number
        return self

    def set_pizza_masa(self, masa):
        self.customer.pizza_masa = masa
        return self

    def set_salsa_base(self, salsa_base):
        self.customer.salsa_base = salsa_base
        return self

    def set_ingredientes(self, ingredientes):
        self.customer.ingredientes = ingredientes
        return self

    def set_tecnica_coccion(self, tecnica_coccion):
        self.customer.tecnica_coccion = tecnica_coccion
        return self

    def set_presentacion(self, presentacion):
        self.customer.presentacion = presentacion
        return self

    def set_bebida(self, bebida):
        self.customer.bebida = bebida
        return self

    def set_extras(self, extras):
        self.customer.extras = extras
        return self

    def build(self):
        return self.customer

    def get_customer(self):
        return self.customer
