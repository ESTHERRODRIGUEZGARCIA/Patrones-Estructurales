#implementa la lógica principal de tu programa, incluida la bienvenida, 
# la presentación del menú, 
# la construcción de pizzas 
# y la personalización. 
# SOLID: cada clase o módulo tenga una sola razón para cambiar.

# main.py
import time
import csv
from menu_personalizada import *
from builder import PizzaBuilder, CustomerBuilder
from combo_composite import *

def display_pizza_menu(menu):
    print("Menú de pizzas:")
    for i, pizza in enumerate(menu, 1):
        print(f"{i}. {pizza['name']}")

def get_selected_pizza_info(menu, choice):
    try:
        index = int(choice) - 1
        if 0 <= index < len(menu):
            selected_pizza = menu[index]
            print(f"Nombre: {selected_pizza['name']}")
        else:
            print("Selección no válida.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def display_recommendations():
    recommendations = (
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
        "Si prefieres refresco, disponemos de gran variedad."
    )
    print(recommendations)

def main():
    
    print("Cargando menú de pizzas...")
    pizza_menu = load_pizza_menu("PIZZERIA/datos/pizza_types.csv")
    customer_counter = 0

    print("\n¡Bienvenido a Delizioso Pizzeria!\n")
    print("¿Qué deseas hacer?")
    print("1. Elegir una pizza del menú")
    print("2. Personalizar tu pizza")
    print("0. Salir\n")

    while True:
        choice = input("\nIngresa el número de tu elección: ")

        if choice == "1":
            display_pizza_menu(pizza_menu)
            pizza_choice = input("Elige el número de la pizza que deseas: ")
            
            if pizza_choice == "0":
                print("Gracias por visitar Delizioso Pizzeria. ¡Hasta la próxima!")
                break

            if not pizza_choice.isnumeric() or int(pizza_choice) < 1 or int(pizza_choice) > len(pizza_menu):
                print("Selección no válida. Inténtalo de nuevo.")
                continue

            # Mostrar detalles de la pizza seleccionada
            get_selected_pizza_info(pizza_menu, pizza_choice)

            # Construir la pizza elegida del menú
            pizza_builder = PizzaBuilder()
            pizza_builder.set_name(pizza_menu[int(pizza_choice) - 1]['name'])
            pizza_to_serve = pizza_builder.build()

        elif choice == "2":
            display_recommendations()  # Mostrar recomendaciones al personalizar la pizza
            customer_counter += 1
            customer_builder = CustomerBuilder()

            customer_builder.set_pizza_masa(input("Tipo de masa (fina o gruesa): "))
            customer_builder.set_salsa_base(input("Salsa base (tomate, soja, genovesa): "))
            customer_builder.set_ingredientes(input("Ingredientes separados por comas: "))
            customer_builder.set_tecnica_coccion(input("Técnica de cocción (horno de piedra o sartén): "))
            customer_builder.set_presentacion(input("Presentación (en caja de cartón o en un plato de metal): "))
            customer_builder.set_bebida(input("Bebida (vino blanco, vino tinto, cocacola, agua, nada): "))
            customer_builder.set_extras(input("Extras (helado, regalo, patatas fritas): "))
            pizza_to_serve = customer_builder.build()

            print("\nHas elegido tu pizza con las siguientes indicaciones:")
            print(pizza_to_serve)

            # Preguntar al cliente si desea realizar alguna modificación
            modify_choice = input("¿Quieres modificar algo? (Sí/No): ").lower()
            if modify_choice == "si" or modify_choice == "s":
                # Permitir modificaciones
                customer_builder.set_pizza_masa(input("Nuevo tipo de masa (fina o gruesa): "))
                customer_builder.set_salsa_base(input("Nueva salsa base (tomate, soja, genovesa): "))
                customer_builder.set_ingredientes(input("Nuevos ingredientes separados por comas: "))
                customer_builder.set_tecnica_coccion(input("Nueva técnica de cocción (horno de piedra o sartén): "))
                customer_builder.set_presentacion(input("Nueva presentación (en caja de cartón o en un plato de metal): "))
                customer_builder.set_bebida(input("Nueva bebida (vino blanco, vino tinto, cocacola, agua, nada): "))
                customer_builder.set_extras(input("Nuevos extras (helado, regalo, patatas fritas): "))
                pizza_to_serve = customer_builder.build()

                print("\nTu pizza modificada:")
                print(pizza_to_serve)

        elif choice == "0":
            print("Gracias por visitar Delizioso Pizzeria. ¡Hasta la próxima!")
            break

        else:
            print("Selección no válida. Inténtalo de nuevo.")
            continue

        print("Construyendo tu pizza...")
        time.sleep(2)
        print("Tu pizza está lista para ser recogida.")

        # Guardar los datos del cliente en el archivo CSV
        save_customer_data("PIZZERIA/datos/datos_clientes.csv", pizza_to_serve)

if __name__ == "__main__":
    main()
