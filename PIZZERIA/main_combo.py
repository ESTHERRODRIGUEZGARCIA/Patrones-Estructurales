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

def display_options(options):
    print("Opciones disponibles:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option.get_description()} - {option.get_price()} euros")

def main():
    # Crear listas con las instancias de pizzas, entrantes, bebidas, postres y combos

    # ... Código previo ...

    combos = [individual, couple, trio, family, super_combo]

    print("Bienvenido a la Pizzería Deliciosa!\n")

    # Mostrar opciones de combos
    display_combos(combos)

    # Elegir un combo
    combo_choice = int(input("\nElige el número del combo que deseas: "))
    selected_combo = combos[combo_choice - 1]

    # Aplicar descuento según el tipo de combo
    selected_combo.apply_discount()

    # Mostrar opciones dentro del combo elegido
    display_options(selected_combo.get_items())

    # Elegir opciones dentro del combo
    selected_items = []
    while True:
        item_choice = input("Ingresa el número del elemento que deseas agregar al combo (o '0' para terminar): ")
        if item_choice == '0':
            break
        selected_item = selected_combo.get_items()[int(item_choice) - 1]
        selected_items.append(selected_item)

    # Agregar opciones al combo
    for item in selected_items:
        selected_combo.add_item(item)

    # Calcular precio del combo y mostrar resultados
    combo_price = selected_combo.get_price()
    print("\nResumen del pedido:")
    print(f"Combo seleccionado: {selected_combo.get_name()} Combo")
    print("Elementos:")
    for item in selected_items:
        print(f"  - {item.get_description()} - {item.get_price()} euros")
    print(f"\nPrecio total: {combo_price} euros")

if __name__ == "__main__":
    main()


