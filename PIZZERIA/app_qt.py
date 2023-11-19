import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog

class PizzaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.pizza_menu = [
            {"name": "The Barbecue Pizza"},
            {"name": "The Pesto Pizza"},
            {"name": "The Hawaiian Pizza"},
            {"name": "The Brie Carre Pizza"},
            {"name": "The Calabrese Pizza"},
            {"name": "The Italian Supreme Pizza"},
            {"name": "The Soppressata Pizza"},
            {"name": "The Spicy Italian Pizza"},
            {"name": "The Five Cheese Pizza"},
            {"name": "The Vegetables Pizza"}
        ]

        self.customer_counter = 0

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Delizioso Pizzeria')
        self.setGeometry(300, 300, 400, 300)

        self.layout = QVBoxLayout()

        self.label = QLabel('¡Bienvenido a Delizioso Pizzeria!', self)
        self.layout.addWidget(self.label)

        recommendations_label = QLabel(
            "\nRECOMENDACIÓN:\n\nTop 5 mejores pizzas servidas por 'Delizioso Pizzeria':\n"
            "1. Pizza con setas, queso fresco, jamón ibérico, trufa\n"
            "2. Pizza con ricota, jamón, pesto de cebollino\n"
            "3. Pizza de verduras (sin tomate), aguacate, jamón ibérico\n"
            "4. Pizza de berenjena, kale, jamón\n"
            "5. Pizza de calabaza, queso, jamón\n\n"
            "En cuanto a vinos:\n"
            "1. Borsao Joven Selección 2021\n"
            "2. Marqués de Cáceres Verdejo 2022\n"
            "3. Viña Zorzal Rosado Garnacha 2022\n\n"
            "Si prefieres refresco, disponemos de gran variedad.",
            self
        )
        self.layout.addWidget(recommendations_label)

        menu_button = QPushButton('Elegir una pizza del menú', self)
        menu_button.clicked.connect(self.display_pizza_menu)
        self.layout.addWidget(menu_button)

        customize_button = QPushButton('Personalizar tu pizza', self)
        customize_button.clicked.connect(self.customize_pizza)
        self.layout.addWidget(customize_button)

        exit_button = QPushButton('Salir', self)
        exit_button.clicked.connect(self.close)
        self.layout.addWidget(exit_button)

        self.setLayout(self.layout)

    def display_pizza_menu(self):
        items = [f"{i + 1}. {pizza['name']}" for i, pizza in enumerate(self.pizza_menu)]
        item, ok_pressed = QInputDialog.getItem(self, "Elegir una pizza", "Selecciona una pizza:", items, 0, False)
        if ok_pressed and item:
            pizza_number = int(item.split(".")[0])
            print(f"Has elegido la pizza {pizza_number}: {self.pizza_menu[pizza_number - 1]['name']}")

    def customize_pizza(self):
        self.customer_counter += 1
        custom_pizza_builder = CustomPizzaBuilder(self.customer_counter)

        custom_pizza_builder.set_pizza_masa(self.get_input("Tipo de masa (fina o gruesa): "))
        custom_pizza_builder.set_salsa_base(self.get_input("Salsa base (tomate, soja, genovesa): "))
        custom_pizza_builder.set_ingredientes(self.get_input("Ingredientes separados por comas: "))
        custom_pizza_builder.set_tecnica_coccion(self.get_input("Técnica de cocción (horno de piedra o sartén): "))
        custom_pizza_builder.set_presentacion(self.get_input("Presentación (en caja de cartón o en un plato de metal): "))
        custom_pizza_builder.set_bebida(self.get_input("Bebida (vino blanco, vino tinto, cocacola, agua, nada): "))
        custom_pizza_builder.set_extras(self.get_input("Extras (helado, regalo, patatas fritas): "))

        pizza_to_serve = custom_pizza_builder.build()

        print("\nHas elegido tu pizza con las siguientes indicaciones:")
        print(pizza_to_serve)

        # Guardar los datos del cliente en el archivo CSV
        save_customer_data("EJERCICIO2/datos/datos_clientes.csv", pizza_to_serve)

    def get_input(self, label):
        text, ok_pressed = QInputDialog.getText(self, "Personalizar pizza", label)
        return text if ok_pressed else ""

def save_customer_data(file_path, pizza_info):
    try:
        with open(file_path, 'a', newline='') as csvfile:
            fieldnames = pizza_info.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Si el archivo está vacío, escribe los encabezados
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(pizza_info)
    except Exception as e:
        print(f"Error al guardar datos del cliente: {e}")

class CustomPizzaBuilder:
    def __init__(self, customer_number):
        self.customer_number = customer_number
        self.pizza_info = {}

    def set_pizza_masa(self, masa):
        self.pizza_info['masa'] = masa

    def set_salsa_base(self, salsa_base):
        self.pizza_info['salsa_base'] = salsa_base

    def set_ingredientes(self, ingredientes):
        self.pizza_info['ingredientes'] = ingredientes

    def set_tecnica_coccion(self, tecnica_coccion):
        self.pizza_info['tecnica_coccion'] = tecnica_coccion

    def set_presentacion(self, presentacion):
        self.pizza_info['presentacion'] = presentacion

    def set_bebida(self, bebida):
        self.pizza_info['bebida'] = bebida

    def set_extras(self, extras):
        self.pizza_info['extras'] = extras

    def build(self):
        return self.pizza_info

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pizza_app = PizzaApp()
    pizza_app.show()
    sys.exit(app.exec_())
