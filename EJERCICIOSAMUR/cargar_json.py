import json
from composite import Carpeta, Documento, Enlace

def cargar_elemento(nombre):
    try:
        with open('archivos.json', 'r') as file:
            estructura_documentos = json.load(file)
            return estructura_documentos[nombre]
    except FileNotFoundError:
        print("Error loading")
        return None
    except json.decoder.DecodeError as e:
        print("Error decoding")
        return None
ruta_json = 'EJERCICIOSAMUR/archivos.json'

def cargar_desde_json(nombre):
    # Cargar la estructura de documentos desde el archivo JSON
    datos_json = cargar_elemento(nombre)
    if datos_json is not None:
        estructura_documentos = Carpeta(datos_json['nombre'])
        for elemento in datos_json['contenido']:
            if elemento['tipo'] == 'Documento':
                estructura_documentos.agregar(Documento(elemento['nombre'], elemento['tipo'], elemento['tamaño'], elemento['sensible']))
            elif elemento['tipo'] == 'Enlace':
                estructura_documentos.agregar(Enlace(elemento['nombre'], cargar_elemento(elemento['destino'])))
            elif elemento['tipo'] == 'Carpeta':
                estructura_documentos.agregar(Carpeta(elemento['nombre']))
    else:
        estructura_documentos = Carpeta('root')

def guardar_json(nombre, estructura_documentos):
    # Guardar la estructura de documentos en el archivo JSON
    try:
        with open(nombre, 'w') as file:
            json.dump(estructura_documentos, file, indent=4)
        print("Estructura de documentos guardada exitosamente en el archivo JSON.")
        return estructura_documentos
    except Exception as e:
        print("Error saving")
        return None

def mostrar_json(estructura_documentos):
    # Mostrar la estructura de documentos en la consola
    print("Estructura de documentos:")
    print(estructura_documentos.mostrar())
    return estructura_documentos