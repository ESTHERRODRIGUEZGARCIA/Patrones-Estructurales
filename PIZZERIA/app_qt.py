import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog

class PizzaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.customer_counter = 0

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Delizioso Pizzeria')
        self.setGeometry(300, 300, 400, 300)

        self.layout = QVBoxLayout()

        self.label = QLabel('¡Bienvenido a Delizioso Pizzeria!', self)
        self.layout.addWidget(self.label)


        menu_button = QPushButton('Elegir un Combo', self)
        menu_button.clicked.connect(self.display_combo)
        self.layout.addWidget(menu_button)

        customize_button = QPushButton('Personalizar tu pizza', self)
        customize_button.clicked.connect(self.customize_pizza)
        self.layout.addWidget(customize_button)

        exit_button = QPushButton('Salir', self)
        exit_button.clicked.connect(self.close)
        self.layout.addWidget(exit_button)

        self.setLayout(self.layout)
    
    def display_combo(self):
        self.combo_window = ComboWindow()
        self.combo_window.show()


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

class ComboWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Elegir Combo')
        self.setGeometry(300, 300, 400, 300)

        self.layout = QVBoxLayout()

        self.label = QLabel('Opciones de combos', self)
        self.layout.addWidget(self.label)

        couple_button = QPushButton('Couple', self)
        couple_button.clicked.connect(self.choose_combo)
        self.layout.addWidget(couple_button)

        trio_button = QPushButton('Trio', self)
        trio_button.clicked.connect(self.choose_combo)
        self.layout.addWidget(trio_button)

        family_button = QPushButton('Family', self)
        family_button.clicked.connect(self.choose_combo)
        self.layout.addWidget(family_button)

        super_button = QPushButton('Super', self)
        super_button.clicked.connect(self.choose_combo)
        self.layout.addWidget(super_button)

        self.setLayout(self.layout)
    
    def choose_combo(self):
        sender = self.sender()
        combo_name = sender.text()

        combo = Combo(combo_name)
        combo.get_items()

        print(f"\nHas elegido el combo {combo.get_name()} con los siguientes productos:")
        for category, items in combo.get_items().items():
            print(f"{category}:")
            for item in items:
                print(f"  - {item.get_description()}")

        print(f"\nEl precio total es de {combo.get_price()}€")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PizzaApp()
    sys.exit(app.exec_())
