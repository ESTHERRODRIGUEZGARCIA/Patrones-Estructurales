#funciones para manejar la lectura y escritura de datos de clientes en un archivo CSV llamado "datos_clientes.csv".

import csv
from pizza_customer import Pizza



def save_customer_data(filename, customer):
    try:
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Escribe los datos del cliente en el archivo CSV
            writer.writerow([
                customer.id,
                customer.pizza_masa,
                customer.salsa_base,
                customer.ingredientes,
                customer.tecnica_coccion,
                customer.presentacion,
                customer.bebida,
                customer.extras
            ])
    except Exception as e:
        print(f"Error al guardar datos del cliente: {str(e)}")

def load_customer_data(filename):
    customers = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                customer = {
                    "id": int(row[0]),
                    "pizza_masa": row[1],
                    "salsa_base": row[2],
                    "ingredientes": row[3],
                    "tecnica_coccion": row[4],
                    "presentacion": row[5],
                    "bebida": row[6],
                    "extras": row[7]
                }
                customers.append(customer)
        Pizza.update_last_id(customers)
    except Exception as e:
        print(f"Error al cargar datos de clientes: {str(e)}")
    return customers


# define funciones para leer el menú desde el archivo CSV "pizza_types.csv". 
# Esto te ayudará a mostrar las opciones disponibles al cliente.


def load_pizza_menu(filename):
    menu = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, 1):
                pizza_name = row['name']
                print(f"{i}. {pizza_name}")
                menu.append(pizza_name)
    except Exception as e:
        print(f"Error al cargar el menú de pizzas: {str(e)}")
    return menu
