from proxy import ProxyAcceso
from composite import Documento, Carpeta, Enlace
import random
from cargar_json import cargar_desde_json, cargar_elemento

def mostrar_contenido(elemento):
    print(f"Contenido de '{elemento.nombre}':")
    for idx, subelemento in enumerate(elemento.contenido, 1):
        print(f"{idx}. {subelemento.nombre} ({subelemento.tipo})")


def acceder_a_elemento(elemento, usuario):
    while True:
        print(f"\n¿Desea acceder a '{elemento.nombre}'? (Sí/No): ")
        respuesta = input().lower()

        if respuesta == 'si':
            mostrar_contenido(elemento)
            nombre_elegido = input("Seleccione el elemento por nombre: ")

            if nombre_elegido.isdigit():
                idx_elegido = int(nombre_elegido)
                if 1 <= idx_elegido <= len(elemento.contenido):
                    elemento_elegido = elemento.contenido[idx_elegido - 1]

                    if isinstance(elemento_elegido, Documento):
                        proxy_acceso = ProxyAcceso(usuario)
                        proxy_acceso.acceder_documento(elemento_elegido)
                    elif isinstance(elemento_elegido, Carpeta):
                        acceder_a_elemento(elemento_elegido, usuario)
                    elif isinstance(elemento_elegido, Enlace):
                        acceder_a_elemento(elemento_elegido.destino, usuario)
                    break
                else:
                    print("Número no válido. Inténtelo de nuevo.")
            elif nombre_elegido.lower() == 'n':
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

        elif respuesta == 'no':
            print(f"No hay más carpetas disponibles para acceder. Cerrando el programa.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

def añadir_elemento_aleatorio(carpeta_actual):
    nombre = input("Ingrese el nombre del nuevo elemento: ")
    tipo_elemento = input("Ingrese el tipo del nuevo elemento (Documento/Enlace/Carpeta): ")

    if tipo_elemento.lower() == 'documento':
        tipo = input("Ingrese el tipo del documento (Texto/Imagen/Video/Audio): ")
        tamaño = int(input("Ingrese el tamaño del documento en KB: "))
        sensible = input("¿El documento es sensible? (Sí/No): ").lower() == 'si'
        nuevo_documento = Documento(nombre, tipo, tamaño, sensible)
        carpeta_actual.agregar(nuevo_documento)
        print(f"Nuevo documento '{nombre}' añadido a '{carpeta_actual.nombre}'.")
    elif tipo_elemento.lower() == 'enlace':
        destino_nombre = input("Ingrese el nombre del destino del enlace: ")
        destino = cargar_elemento(destino_nombre, carpeta_actual)  # Puedes ajustar esta función según sea necesario
        nuevo_enlace = Enlace(nombre, destino)
        carpeta_actual.agregar(nuevo_enlace)
        print(f"Nuevo enlace '{nombre}' añadido a '{carpeta_actual.nombre}'.")
    elif tipo_elemento.lower() == 'carpeta':
        nueva_carpeta = Carpeta(nombre)
        carpeta_actual.agregar(nueva_carpeta)
        print(f"Nueva carpeta '{nombre}' añadida a '{carpeta_actual.nombre}'.")
    else:
        print("Tipo de elemento no válido.")


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