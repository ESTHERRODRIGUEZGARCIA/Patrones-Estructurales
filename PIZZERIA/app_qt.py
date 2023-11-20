import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog, QDialog, QFormLayout

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
        save_customer_data("PIZZERIA/datos/datos_clientes.csv", pizza_to_serve)

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
    
    def set_customer_number(self, customer_number):
        self.customer_number = customer_number


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

        # Crear botones para cada tipo de combo
        for combo_type in [individual, couple, trio, family, super_combo]:
            combo_button = QPushButton(combo_type.get_name(), self)
            combo_button.clicked.connect(self.choose_combo_type)
            self.layout.addWidget(combo_button)

        self.setLayout(self.layout)
    
    def choose_combo_type(self):
        sender = self.sender()
        combo_type_name = sender.text()

        # Abrir una nueva ventana o diálogo para elegir elementos según el tipo de combo
        combo_type = Combo(combo_type_name)
        elements_dialog = ComboElementsDialog(combo_type)
        elements_dialog.exec_()  # Ejecutar el diálogo de forma modal

class ComboElementsDialog(QDialog):
    def __init__(self, combo_type):
        super().__init__()

        self.combo_type = combo_type

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(f'Elegir elementos para {self.combo_type.get_name()}')
        self.setGeometry(400, 400, 400, 300)

        self.layout = QVBoxLayout()

        self.label = QLabel(f'Elegir elementos para {self.combo_type.get_name()}', self)
        self.layout.addWidget(self.label)

        # Crear formularios para cada categoría de elementos
        form_layout = QFormLayout()
        for category, items in self.combo_type.get_items().items():
            for item in items:
                item_button = QPushButton(item.get_description(), self)
                item_button.clicked.connect(self.choose_element)
                form_layout.addRow(item.get_description(), item_button)

        self.layout.addLayout(form_layout)

        self.setLayout(self.layout)

    def choose_element(self):
        sender = self.sender()
        element_name = sender.text()

        # Aquí puedes guardar la elección del usuario, calcular el precio, etc.
        print(f"Has elegido {element_name}")

        # Ejemplo: Calcular el precio total y guardar en el CSV
        total_price = self.combo_type.get_price()
        order_id = str(uuid.uuid4())
        save_order_to_csv(order_id, self.combo_type.get_name(), total_price)

        self.accept()  # Cerrar el diálogo después de elegir los elementos




if __name__ == '__main__':
    app = QApplication(sys.argv)
    pizza_app = PizzaApp()
    pizza_app.show()
    sys.exit(app.exec_())
