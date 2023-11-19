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
couple = Combo("Couple")
trio = Combo("Trio")
family = Combo("Family")
super_combo = Combo("Super")

def display_combos(combos):
    print("Opciones de combos:")
    for i, combo in enumerate(combos, 1):
        print(f"{i}. {combo.get_description()}")

def display_options(options, num_choices):
    print("\nOpciones disponibles:")
    for category, category_items in options.items():
        print(f"\n{category.capitalize()}:")
        for i, option in enumerate(category_items, 1):
            print(f"  {i}. {option.get_description()} - {option.get_price()} euros")

def choose_items(category, num_choices):
    selected_items = []

    print(f"\nElige {category[0].__class__.__name__}s:")
    for i, item in enumerate(category, 1):
        print(f"  {i}. {item.get_description()} - {item.get_price()} euros")

    for _ in range(num_choices):
        item_choice = int(input(f"Ingrese el número del {category[0].__class__.__name__} que desea ({len(selected_items) + 1}/{num_choices}): "))

        # Verificamos que la opción ingresada esté dentro del rango
        if 1 <= item_choice <= len(category):
            selected_item = category[item_choice - 1]
            selected_items.append(selected_item)
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            return choose_items(category, num_choices)  # Llamada recursiva si la opción no es válida

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


def main():
    # Crear listas con las instancias de pizzas, entrantes, bebidas, postres y combos...

    combos = [individual, couple, trio, family, super_combo]
    entrantes = [croquetas, tequeños, patatas]
    bebidas = [refresco, agua, vino]
    pizzas = [barbacoa, pesto, hawaiana, brie_carre, calabresa, italiana_suprema, soppressata, italiana_picante, cinco_quesos, vegetariana]
    postres = [tarta_queso, tarta_abuela, helado, mus_limon, tarta_chocolate]

    print("Bienvenido a la Pizzería Deliciosa!\n")

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

if __name__ == "__main__":
    main()