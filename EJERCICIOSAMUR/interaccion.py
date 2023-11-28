from proxy import ProxyAcceso
from composite import Documento, Carpeta, Enlace
import random
from cargar_json import cargar_desde_json

def mostrar_contenido(elemento):
    print(f"Contenido de '{elemento.nombre}':")
    for idx, subelemento in enumerate(elemento.contenido, 1):
        print(f"{idx}. {subelemento.nombre} ({subelemento.tipo})")


def acceder_a_elemento(elemento):
    while True:
        print(f"\n¿Desea acceder a '{elemento.nombre}'? (Sí/No): ")
        respuesta = input().lower()

        if respuesta == 'si':
            mostrar_contenido(elemento)
            nombre_elegido = input("Seleccione el elemento por nombre: ")
            elemento_elegido = None

            for subelemento in elemento.contenido:
                if subelemento.nombre == nombre_elegido:
                    elemento_elegido = subelemento
                    break

            if elemento_elegido:
                if isinstance(elemento_elegido, Documento):
                    print(f"Usuario: {usuario}, ha tenido acceso al archivo {elemento_elegido.nombre}, tipo {elemento_elegido.tipo}, tamaño {elemento_elegido.tamaño}.")
                elif isinstance(elemento_elegido, Carpeta):
                    acceder_a_elemento(elemento_elegido)
                elif isinstance(elemento_elegido, Enlace):
                    acceder_a_elemento(elemento_elegido.destino)
                break
            else:
                print("Elemento no encontrado. Inténtelo de nuevo.")

        elif respuesta == 'no':
            print(f"No hay más carpetas disponibles para acceder. Cerrando el programa.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

def añadir_elemento_aleatorio(carpeta_actual):
    nombre = input("Ingrese el nombre del nuevo elemento: ")

    # Seleccionar aleatoriamente el tipo de elemento (Documento o Carpeta)
    tipo_elemento = random.choice(['Documento', 'Carpeta'])

    # Generar características aleatorias
    tipo = random.choice(['Texto', 'Imagen', 'Video', 'Audio'])
    tamaño = random.randint(1, 200)
    sensible = random.choice([True, False])

    if tipo_elemento == 'Documento':
        nuevo_documento = Documento(nombre, tipo, tamaño, sensible, [])
        carpeta_actual.agregar_elemento(nuevo_documento)
        print(f"Nuevo documento '{nombre}' añadido a '{carpeta_actual.nombre}'.")
    elif tipo_elemento == 'Carpeta':
        nueva_carpeta = Carpeta(nombre, [])
        carpeta_actual.agregar_elemento(nueva_carpeta)
        print(f"Nueva carpeta '{nombre}' añadida a '{carpeta_actual.nombre}'.")
    else:
        print("Error al añadir el elemento. Tipo desconocido.")


def eliminar_elemento(carpeta_actual):
    while True:
        mostrar_contenido(carpeta_actual)
        nombre_eliminar = input("Seleccione el número del elemento a eliminar o 'n' para cancelar: ")
        if nombre_eliminar.isdigit():
            idx_eliminar = int(nombre_eliminar)
            if 1 <= idx_eliminar <= len(carpeta_actual.contenido):
                elemento_eliminar = carpeta_actual.contenido[idx_eliminar - 1]
                carpeta_actual.eliminar_elemento(elemento_eliminar)
                print(f"Elemento '{elemento_eliminar.nombre}' eliminado.")
                break
            else:
                print("Número no válido. Inténtelo de nuevo.")
        elif nombre_eliminar.lower() == 'n':
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Función principal para interactuar con el sistema
def interactuar_con_sistema(usuario, carpeta_raiz):
    print(f"Bienvenido, {usuario}.\n")
    acceder_a_elemento(carpeta_raiz)