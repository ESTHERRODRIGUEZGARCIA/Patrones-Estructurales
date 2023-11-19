import time
import csv
import uuid
import os
from menu_personalizada import *
from builder import PizzaBuilder, CustomerBuilder
from combo_composite import *

#creo las instancias de las pizzas:

barbacoa = PizzaMenu("Barbacoa", ["Pollo Asado, Pimientos Rojos, Pimientos Verdes, Tomates, Cebollas Moradas, Salsa Barbacoa"], 12)
pesto = PizzaMenu("Pesto", ["Pollo, Tomate, Pimientos Rojos, Espinacas, Ajo, Salsa Pesto"], 13)
hawaiana = PizzaMenu("Hawaiana", ["Jamón lonchas, piña, queso mozzarella"], 10)
brie_carre = PizzaMenu("Brie Carré", ["Queso Brie Carré, Prosciutto, Cebolla Caramelizada, Peras, Tomillo, Ajo"], 15)
calabresa = PizzaMenu("Calabresa", ["Salami Nduja, Pancetta, Tomates, Cebollas Rojas, Pimientos Friggitello, Ajo"], 13)
italiana_suprema = PizzaMenu("Italiana Suprema", ["Salami Calabrese, Capocollo, Tomates, Cebollas Rojas, Aceitunas Verdes, Ajo"], 20)
soppressata = PizzaMenu("Soppressata", ["Salami Soppressata, Queso Fontina, Queso Mozzarella, Champiñones, Ajo"], 15)
italiana_picante = PizzaMenu("Italiana Picante", ["Capocollo, Tomates, Queso De Cabra, Alcachofas, Peperoncini Verdi, Ajo"], 17)
cinco_quesos = PizzaMenu("Cinco Quesos", ["Queso Mozzarella, Queso Provolone, Queso Gouda Ahumado, Queso Romano, Queso Azul, Ajo"], 15)
vegetariana = PizzaMenu("Vegetariana", ["Champiñones, Tomates, Pimientos Rojos, Pimientos Verdes, Cebollas Rojas, Calabacines, Espinacas, Ajo"], 13)

#creo las instancias de los entrantes:
croquetas = Entrante("Croquetas", ["jamón, queso"], 1)
tequeños = Entrante("Tequeños", ["queso"], 2)
patatas = Entrante("Patatas Fritas", ["patatas fritas"], 3)

#creo las instancias de las bebidas:
refresco = Bebida("Refresco", 3)
agua = Bebida("Agua", 2)
vino = Bebida("Vino", 5)

#creo las instancias de los postres:
tarta_queso = Postre("Tarta de Queso", 7)
tarta_abuela = Postre("Tarta de la Abuela", 5)
helado = Postre("Helado", 4)
mus_limon = Postre("Mus de Limon", 5)
tarta_chocolate = Postre("Tarta 3 Chocolates", 7)

#creo las instancias de los combos:
individual = Combo("Individual")
couple = Combo("Couple (5% de descuento)")
trio = Combo("Trio (10% de descuento)")
family = Combo("Family (15% de descuento)")
super_combo = Combo("Super (20% de descuento)")


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

def display_combos(combos):
    print("Opciones de combos:")
    for i, combo in enumerate(combos, 1):
        print(f"{i}. {combo.get_description()}")

def choose_combo(combos):
    while True:
        combo_choice = input("\nElige el número del combo que deseas: ")

        if combo_choice.isdigit():
            combo_choice = int(combo_choice)

            if 1 <= combo_choice <= len(combos):
                return combos[combo_choice - 1]
            else:
                print("Error: El número de combo ingresado no es válido.")
        else:
            print("Error: Ingresa un valor numérico.")

        retry = input("¿Quieres volver a intentarlo? (si/no): ").lower()
        if retry != 'si':
            print("Hasta pronto!! ")
            exit()

def choose_items(category, num_choices):
    selected_items = []

    print(f"\nElige {category[0].__class__.__name__}s:")
    for i, item in enumerate(category, 1):
        print(f"  {i}. {item.get_description()} - {item.get_price()} euros")

    for _ in range(num_choices):
        while True:
            item_choice = input(f"Ingrese el número del {category[0].__class__.__name__} que desea ({len(selected_items) + 1}/{num_choices}): ")

            if item_choice.isdigit():
                item_choice = int(item_choice)

                if 1 <= item_choice <= len(category):
                    selected_item = category[item_choice - 1]
                    selected_items.append(selected_item)
                    break
                else:
                    print("Error: El número de opción ingresado no es válido.")
            else:
                print("Error: Ingresa un valor numérico.")

    return selected_items

def get_num_choices(combo_name):
    combo_name_lower = combo_name.lower()

    if "individual" in combo_name_lower:
        return 1
    elif "couple" in combo_name_lower:
        return 2
    elif "trio" in combo_name_lower:
        return 3
    elif "family" in combo_name_lower:
        return 4
    elif "super" in combo_name_lower:
        return 5
    else:
        print("Hasta pronto!! ")  # Opción predeterminada si no coincide con ninguno de los combos conocidos

def save_order_to_csv(order_id, combo_type, total_price):
    file_path = "PIZZERIA/datos/combos.csv"

    # Verificar si el archivo CSV ya existe
    file_exists = os.path.exists(file_path)

    with open(file_path, mode='a', newline='') as csv_file:
        fieldnames = ['OrderID', 'ComboType', 'TotalPrice']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Escribir encabezados solo si es un nuevo archivo
        if not file_exists:
            writer.writeheader()

        # Escribir la información del pedido
        writer.writerow({'OrderID': order_id, 'ComboType': combo_type, 'TotalPrice': total_price})

def main():
    customer_counter = 0

    combos = [individual, couple, trio, family, super_combo]
    entrantes = [croquetas, tequeños, patatas]
    bebidas = [refresco, agua, vino]
    pizzas = [barbacoa, pesto, hawaiana, brie_carre, calabresa, italiana_suprema, soppressata, italiana_picante, cinco_quesos, vegetariana]
    postres = [tarta_queso, tarta_abuela, helado, mus_limon, tarta_chocolate]
    
    print("\n¡Bienvenido a Delizioso Pizzeria!\n")

    print("¿Qué deseas hacer?")
    print("1. Personalizar tu pizza")
    print("2. Elegir un combo")
    print("0. Salir\n")

    while True:
        choice = input("\nIngresa el número de tu elección: ")


        if choice == "1":
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
            
            print("Construyendo tu pizza...")
            time.sleep(2)
            print("Tu pizza está lista para ser recogida.")

            # Guardar los datos del cliente en el archivo CSV
            save_customer_data("PIZZERIA/datos/datos_clientes.csv", pizza_to_serve)

        elif choice == "2":
            # Mostrar opciones de combos
            display_combos(combos)

            # Elegir un combo
            combo_choice = int(input("\nElige el número del combo que deseas: "))
            selected_combo = combos[combo_choice - 1]

            # Obtener el número de opciones que el usuario debe elegir
            num_choices = get_num_choices(selected_combo.get_name())


            # Aplicar descuento según el tipo de combo
            selected_combo.apply_discount()

            # Elegir entrantes
            entrantes_seleccionados = choose_items(entrantes, num_choices)
            selected_combo.add_item(entrantes_seleccionados, 'entrantes')

            # Elegir pizzas
            pizzas_seleccionadas = choose_items(pizzas, num_choices)
            selected_combo.add_item(pizzas_seleccionadas, 'pizzas')

            # Elegir bebidas
            bebidas_seleccionadas = choose_items(bebidas, num_choices)
            selected_combo.add_item(bebidas_seleccionadas, 'bebidas')

            # Elegir postres
            postres_seleccionados = choose_items(postres, num_choices)
            selected_combo.add_item(postres_seleccionados, 'postres')

            # Calcular precio del combo y mostrar resultados
            combo_price = selected_combo.get_price()
            print("\nResumen final del pedido:")
            print(f"Combo seleccionado: {selected_combo.get_description()}")
            print("Elementos:")
            
            # Mostrar resumen detallado
            for category, items in selected_combo.items.items():
                print(f"\n{category.capitalize()}:")
                for item in items:
                    print(f"  - {item.get_description()} - {item.get_price()} euros")

            print(f"\nPrecio total: {combo_price} euros")

            # Generar un ID único para el pedido
            order_id = str(uuid.uuid4())

            # Guardar el pedido en el archivo CSV
            save_order_to_csv(order_id, selected_combo.get_name(), combo_price)



        elif choice == "0":
            print("Gracias por visitar Delizioso Pizzeria. ¡Hasta la próxima!")
            break

        else:
            print("Selección no válida. Inténtalo de nuevo.")
            continue



if __name__ == "__main__":
    main()