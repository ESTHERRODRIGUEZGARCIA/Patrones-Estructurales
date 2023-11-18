#class Pizza que represente una pizza, aquí estaran las 7 cosas que lleva cada pizza
import uuid

class Pizza:

    def __init__(self):
        self.name = None
        self.category = None
        self.ingredients = None
        self.id = str(uuid.uuid4())


    def __str__(self):
        return f"Nombre: {self.name}, Categoría: {self.category}, Ingredientes: {self.ingredients}"


class Customer:

    def __init__(self):
        self.customer_number = None
        self.pizza_masa = None
        self.salsa_base = None
        self.ingredientes = None
        self.tecnica_coccion = None
        self.presentacion = None
        self.bebida = None
        self.extras = None
        self.id = str(uuid.uuid4())


    def __str__(self):
        return f"Cliente {self.customer_number} - Pizza con Masa: {self.pizza_masa}, Salsa: {self.salsa_base}, Ingredientes: {self.ingredientes}, Técnica: {self.tecnica_coccion}, Presentación: {self.presentacion}, Bebida: {self.bebida}, Extras: {self.extras}"

