from proxy import ProxyAcceso
from composite import *

def acceder_a_carpeta(carpeta_personal):
    while True:
        print("1. Acceder a una carpeta")
        print("2. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            nombre_carpeta = input("Nombre de la carpeta: ")
            for carpeta in carpeta_personal.contenido:
                if isinstance(carpeta, Carpeta) and carpeta.nombre == nombre_carpeta:
                    return carpeta
            print("No se encontró la carpeta. Inténtelo de nuevo.\n")
        elif opcion == '2':
            return carpeta_personal
        else:
            print("Opción no válida. Inténtelo de nuevo.\n")

def acceder_a_enlace(carpeta_personal):
    while True:
        print("1. Acceder a un enlace")
        print("2. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            nombre_enlace = input("Nombre del enlace: ")
            for enlace in carpeta_personal.contenido:
                if isinstance(enlace, Enlace) and enlace.nombre == nombre_enlace:
                    return enlace
            print("No se encontró el enlace. Inténtelo de nuevo.\n")
        elif opcion == '2':
            return carpeta_personal
        else:
            print("Opción no válida. Inténtelo de nuevo.\n")

def buscar_documento(nombre, carpeta_actual):
    """
    Busca un documento por nombre en la carpeta actual y sus subcarpetas recursivamente.

    Parameters:
    - nombre (str): El nombre del documento a buscar.
    - carpeta_actual (dict): La carpeta actual en la que se debe realizar la búsqueda.

    Returns:
    - dict or None: Devuelve el documento si se encuentra, o None si no se encuentra.
    """
    for documento in carpeta_actual['contenido']:
        if documento['nombre'] == nombre:
            return documento
        elif documento['tipo'] == 'Carpeta':
            # Si el documento actual es una carpeta, realiza la búsqueda recursiva en esa carpeta.
            resultado_busqueda = buscar_documento(nombre, documento)
            if resultado_busqueda:
                return resultado_busqueda

    # Si no se encuentra el documento en la carpeta actual ni en sus subcarpetas, devuelve None.
    return None


# Función para añadir un nuevo documento a una carpeta
def añadir_documento(nombre, tipo, tamaño, sensible, accesos, carpeta_actual):
    nuevo_documento = {
        "nombre": nombre,
        "tipo": tipo,
        "tamaño": tamaño,
        "sensible": sensible,
        "accesos": accesos
    }
    carpeta_actual['contenido'].append(nuevo_documento)

# Función para eliminar un documento de una carpeta
def eliminar_documento(nombre, carpeta_actual):
    documento = buscar_documento(nombre, carpeta_actual)
    if documento:
        carpeta_actual['contenido'].remove(documento)
        print(f"Documento '{nombre}' eliminado.")
    else:
        print(f"Documento '{nombre}' no encontrado.")


# Función para mostrar el contenido de una carpeta
def mostrar_contenido(carpeta_actual):
    print(f"Contenido de la carpeta '{carpeta_actual['nombre']}':")
    for documento in carpeta_actual['contenido']:
        print(f"- {documento['nombre']} ({documento['tipo']})")