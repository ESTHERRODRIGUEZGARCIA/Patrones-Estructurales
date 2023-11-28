import json


def cargar_elemento(nombre, carpeta_personal):
    for documento in carpeta_personal['contenido']:
        if documento['nombre'] == nombre:
            return documento
    return None

def cargar_desde_json(nombre_archivo='archivos.json'):
    # Cargar la estructura de documentos desde el archivo JSON
    with open(nombre_archivo, 'r') as file:
        estructura_documentos = json.load(file)

    return estructura_documentos