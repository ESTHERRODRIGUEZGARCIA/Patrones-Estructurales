import json
from composite import Carpeta, Documento, Enlace


# Cargar la estructura de documentos desde el archivo JSON
with open('archivos.json', 'r') as file:
    estructura_documentos = json.load(file)

def cargar_elemento(nombre, carpeta_actual):
    for documento in carpeta_actual['contenido']:
        if documento['nombre'] == nombre:
            return documento
    return None

def cargar_desde_json(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        data = json.load(file)
        return cargar_elemento(data)