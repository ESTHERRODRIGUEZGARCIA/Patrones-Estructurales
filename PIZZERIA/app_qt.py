import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog, QDialog, QFormLayout
import uuid

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
        pizza_id = str(uuid.uuid4())

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
        save_customer_data("PIZZERIA/datos/datos_clientes.csv", pizza_id, pizza_to_serve)

    def get_input(self, label):
        text, ok_pressed = QInputDialog.getText(self, "Personalizar pizza", label)
        return text if ok_pressed else ""

def save_customer_data(file_path, pizza_id, pizza_info):
    try:
        with open(file_path, 'a', newline='') as csvfile:
            fieldnames = ['id'] + list(pizza_info.keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Si el archivo está vacío, escribe los encabezados
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'id': pizza_id, **pizza_info})
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
        self.setWindowTitle("Elegir Combo:")
        self.setGeometry(300, 300, 400, 300)

        self.layout = QVBoxLayout()

        self.label = QLabel("Opciones de combos", self)
        self.layout.addWidget(self.label)

        for combo_type in ['Individual', 'Couple', 'Trio', 'Family', 'Super']:
            combo_button = QPushButton(combo_type, self)
            combo_button.clicked.connect(lambda _, combo_type=combo_type: self.select_combo(combo_type))
            self.layout.addWidget(combo_button)


        self.setLayout(self.layout)
        self.selected_items = {'Entrante': [], 'PizzaMenu': [], 'Bebida': [], 'Postre': []}
        self.max_selections = {'Individual': 1, 'Couple': 2, 'Trio': 3, 'Family': 4, 'Super': 5}

    def select_combo(self, combo_type):
        combo_elements_dialog = ComboElementsDialog(combo_type, self.selected_items, self.max_selections[combo_type])
        combo_elements_dialog.exec_()

class ComboElementsDialog(QDialog):
    def __init__(self, combo_type, selected_items, max_selections):
        super().__init__()
        self.combo_type = combo_type
        self.selected_items = selected_items
        self.max_selections = max_selections
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(f"Elegir elementos para el combo {self.combo_type}")
        self.setGeometry(300, 300, 600, 400)

        self.layout = QVBoxLayout()

        self.label = QLabel(f"Elegir elementos para el combo {self.combo_type}", self)
        self.layout.addWidget(self.label)

        for combo_category, options in combo_options.items():
            combo_category_label = QLabel(f'{combo_category} (Elige {self.max_selections} elementos):', self)
            self.layout.addWidget(combo_category_label)

            for idx, option in enumerate(options, start=1):
                option_button = QPushButton(
                    f"{idx}. {option['name']} - {', '.join(option['ingredients'])} - {option['price']} euros", self)
                option_button.clicked.connect(lambda _, cat=combo_category, opt=option: self.select_combo_item(cat, opt))
                self.layout.addWidget(option_button)

        done_button = QPushButton("Finalizar pedido", self)
        done_button.clicked.connect(self.finalize_order)
        self.layout.addWidget(done_button)

        self.setLayout(self.layout)

    def select_combo_item(self, category, option):
        if len(self.selected_items[category]) >= self.max_selections:
            print(f"Ya has elegido {self.max_selections} elementos para la categoría {category}")
            return
        self.selected_items[category].append(option)

    def finalize_order(self):
        total_price = 0
        combo_name = f"{self.combo_type} Combo"
        combo_id = str(uuid.uuid4())

        
        print(f"\nHas elegido el combo {self.combo_type} con los siguientes elementos:")
        for category, items in self.selected_items.items():
            if items:
                for item in items:
                    print(f"{category}: {item['name']} - {', '.join(item['ingredients'])} - {item['price']} euros")
                    total_price += item['price']
            else:
                print(f"No has elegido ningún elemento para la categoría {category}")

        print(f"\nEl precio total es de {total_price} euros")

        # Guardar los datos del cliente en el archivo CSV
        save_customer_data_combo("PIZZERIA/datos/combos.csv", combo_id, combo_name, total_price)

        self.close()
def save_customer_data_combo(file_path, combo_id, combo_name, price):
    try:
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Escribir la información del combo en el formato deseado
            writer.writerow([combo_id, combo_name, price])
    except Exception as e:
        print(f"Error al guardar datos del combo: {e}")

combo_options = {
    'Entrante': [
        {'name': 'Croquetas', 'ingredients': ['jamón', 'queso'], 'price': 1},
        {'name': 'Tequeños', 'ingredients': ['queso'], 'price': 2},
        {'name': 'Patatas Fritas', 'ingredients': ['patatas fritas'], 'price': 3},
    ],
    'PizzaMenu': [
        {'name': 'Barbacoa', 'ingredients': ['Pollo Asado', 'Pimientos Rojos', 'Pimientos Verdes', 'Tomates', 'Cebollas Moradas', 'Salsa Barbacoa'], 'price': 12},
        {'name': 'Pesto', 'ingredients': ['Pollo', 'Tomate', 'Pimientos Rojos', 'Espinacas', 'Ajo', 'Salsa Pesto'], 'price': 13},
        {'name': 'Hawaiana', 'ingredients': ['Jamón lonchas', 'piña', 'queso mozzarella'], 'price': 10},
        {'name': 'Brie Carré', 'ingredients': ['Queso Brie Carré', 'Prosciutto', 'Cebolla Caramelizada', 'Peras', 'Tomillo', 'Ajo'], 'price': 15},
        {'name': 'Calabresa', 'ingredients': ['Salami Nduja', 'Pancetta', 'Tomates', 'Cebollas Rojas', 'Pimientos Friggitello', 'Ajo'], 'price': 13},
        {'name': 'Italiana Suprema', 'ingredients': ['Salami Calabrese', 'Capocollo', 'Tomates', 'Cebollas Rojas', 'Aceitunas Verdes', 'Ajo'], 'price': 20},
        {'name': 'Soppressata', 'ingredients': ['Salami Soppressata', 'Queso Fontina', 'Queso Mozzarella', 'Champiñones', 'Ajo'], 'price': 15},
        {'name': 'Italiana Picante', 'ingredients': ['Capocollo', 'Tomates', 'Queso De Cabra', 'Alcachofas', 'Peperoncini Verdi', 'Ajo'], 'price': 17},
        {'name': 'Cinco Quesos', 'ingredients': ['Queso Mozzarella', 'Queso Provolone', 'Queso Gouda Ahumado', 'Queso Romano', 'Queso Azul', 'Ajo'], 'price': 15},
        {'name': 'Vegetariana', 'ingredients': ['Champiñones', 'Tomates', 'Pimientos Rojos', 'Pimientos Verdes', 'Cebollas Rojas', 'Calabacines', 'Espinacas', 'Ajo'], 'price': 13},
    ],
    'Bebida': [
        {'name': 'Refresco', 'ingredients': [], 'price': 3},
        {'name': 'Agua', 'ingredients': [], 'price': 2},
        {'name': 'Vino', 'ingredients': [], 'price': 5},
    ],
    'Postre': [
        {'name': 'Tarta de Queso', 'ingredients': [], 'price': 7},
        {'name': 'Tarta de la Abuela', 'ingredients': [], 'price': 5},
        {'name': 'Helado', 'ingredients': [], 'price': 4},
        {'name': 'Mus de Limon', 'ingredients': [], 'price': 5},
        {'name': 'Tarta 3 Chocolates', 'ingredients': [], 'price': 7},
    ],
}


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pizza_app = PizzaApp()
    pizza_app.show()
    sys.exit(app.exec_())
