#class Pizza que represente una pizza, aquí estaran las 7 cosas que lleva cada pizza
class Pizza:
    last_id = 0



    @classmethod
    def update_last_id(cls, loaded_data):
        if loaded_data:
            cls.last_id = max(customer['id'] for customer in loaded_data)

    def __init__(self):
        self.name = None
        self.category = None
        self.ingredients = None
        self.id = Pizza.get_next_id()

    @classmethod
    def get_next_id(cls):
        cls.last_id += 1
        return cls.last_id

    def __str__(self):
        return f"Nombre: {self.name}, Categoría: {self.category}, Ingredientes: {self.ingredients}"

#class customer que representa un cliente y sus elecciones
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

    def __str__(self):
        return f"Cliente {self.customer_number} - Pizza con Masa: {self.pizza_masa}, Salsa: {self.salsa_base}, Ingredientes: {self.ingredientes}, Técnica: {self.tecnica_coccion}, Presentación: {self.presentacion}, Bebida: {self.bebida}, Extras: {self.extras}"
