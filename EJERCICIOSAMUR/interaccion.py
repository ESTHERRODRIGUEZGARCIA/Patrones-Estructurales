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

def crear_documento(carpeta_personal):
    while True:
        nombre_documento = input("Nombre del documento: ")
        tipo_documento = input("Tipo del documento: ")
        tamanio_documento = input("Tamaño del documento (en KB): ")
        sensible_documento = input("¿Es sensible? (s/n): ")
        if sensible_documento == 's':
            sensible_documento = True
        elif sensible_documento == 'n':
            sensible_documento = False
        else:
            print("Opción no válida. Inténtelo de nuevo.\n")
            continue
        documento = Documento(nombre_documento, tipo_documento, tamanio_documento, sensible_documento)
        carpeta_personal.agregar(documento)
        return carpeta_personal

def eliminar_documento(carpeta_personal):
    while True:
        nombre_documento = input("Nombre del documento: ")
        for documento in carpeta_personal.contenido:
            if isinstance(documento, Documento) and documento.nombre == nombre_documento:
                carpeta_personal.eliminar(documento)
                return carpeta_personal
        print("No se encontró el documento. Inténtelo de nuevo.\n")
