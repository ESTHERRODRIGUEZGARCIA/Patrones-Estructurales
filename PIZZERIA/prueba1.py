import csv
from abc import ABC, abstractmethod

# Clase base para los elementos del combo (Componente)
class ComboItem(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

# Clase para los elementos individuales del combo (Hoja)
class IndividualItem(ComboItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        return self.name

    def get_price(self):
        return self.price

# Clase para el combo (Compuesto)
class Combo(ComboItem):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_description(self):
        return f"{self.name} Combo"

    def get_price(self):
        return sum(item.get_price() for item in self.items)

# Funciones para cargar y guardar datos en CSV
def save_combo_data(filename, combo):
    try:
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                combo.get_description(),
                combo.get_price()
            ])
    except Exception as e:
        print(f"Error al guardar datos del combo: {str(e)}")

def load_combo_data(filename):
    combos = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                combo = Combo(row[0])
                combo_price = float(row[1])
                combo.add_item(IndividualItem("Discount", -combo_price))  # Añadir descuento como elemento
                combos.append(combo)
    except Exception as e:
        print(f"Error al cargar datos de combos: {str(e)}")
    return combos

# Función principal
def main():
    # Crear combos predefinidos
    individual_combo = Combo("Individual")
    couple_combo = Combo("Couple")
    trio_combo = Combo("Trio")
    family_combo = Combo("Family")
    super_combo = Combo("Super")

    # Añadir elementos a los combos
    individual_combo.add_item(IndividualItem("Entrante", 1))
    individual_combo.add_item(IndividualItem("Pizza", 10))
    individual_combo.add_item(IndividualItem("Bebida", 3))
    individual_combo.add_item(IndividualItem("Postre", 7))

    couple_combo.add_item(IndividualItem("Entrante", 2))
    couple_combo.add_item(IndividualItem("Pizza", 10))
    couple_combo.add_item(IndividualItem("Bebida", 3))
    couple_combo.add_item(IndividualItem("Postre", 7))

    trio_combo.add_item(IndividualItem("Entrante", 3))
    trio_combo.add_item(IndividualItem("Pizza", 10))
    trio_combo.add_item(IndividualItem("Bebida", 3))
    trio_combo.add_item(IndividualItem("Postre", 7))

    family_combo.add_item(IndividualItem("Entrante", 4))
    family_combo.add_item(IndividualItem("Pizza", 10))
    family_combo.add_item(IndividualItem("Bebida", 3))
    family_combo.add_item(IndividualItem("Postre", 7))

    super_combo.add_item(IndividualItem("Entrante", 5))
    super_combo.add_item(IndividualItem("Pizza", 10))
    super_combo.add_item(IndividualItem("Bebida", 3))
    super_combo.add_item(IndividualItem("Postre", 7))

    # Mostrar combos disponibles
    print("Combos disponibles:")
    print("1. Individual")
    print("2. Couple")
    print("3. Trio")
    print("4. Family")
    print("5. Super")

    # Elegir un combo
    combo_choice = input("Elige el número del combo que deseas: ")

    # Crear una instancia del combo elegido
    selected_combo = None
    if combo_choice == "1":
        selected_combo = individual_combo
    elif combo_choice == "2":
        selected_combo = couple_combo
    elif combo_choice == "3":
        selected_combo = trio_combo
    elif combo_choice == "4":
        selected_combo = family_combo
    elif combo_choice == "5":
        selected_combo = super_combo
    else:
        print("Selección no válida. Saliendo.")
        return

    # Mostrar detalles del combo
    print("\nDetalles del combo:")
    print(f"Descripción: {selected_combo.get_description()}")
    print(f"Precio: {selected_combo.get_price()} euros")

    # Guardar el combo en el archivo CSV
    save_combo_data("PIZZERIA/datos/combos.csv", selected_combo)

    # Cargar y mostrar combos desde el archivo CSV
    loaded_combos = load_combo_data("PIZZERIA/datos/combos.csv")
    print("\nCombos cargados desde el archivo:")
    for combo in loaded_combos:
        print(f"Descripción: {combo.get_description()}")
        print(f"Precio: {combo.get_price()} euros\n")

if __name__ == "__main__":
    main()
