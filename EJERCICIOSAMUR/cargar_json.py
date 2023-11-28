import json
from composite import Carpeta, Documento, Enlace

def cargar_elemento(data):
    tipo = data.get("tipo")
    if tipo == "Carpeta":
        carpeta = Carpeta(data["nombre"])
        for elemento_data in data["contenido"]:
            elemento = cargar_elemento(elemento_data)
            carpeta.agregar(elemento)
        return carpeta
    elif tipo == "Documento":
        return Documento(data["nombre"], data["tipo"], data["tamanio"], data["sensible"])
    elif tipo == "Enlace":
        destino = cargar_elemento(data["destino"])
        return Enlace(data["nombre"], destino)
    else:
        raise ValueError(f"Tipo desconocido: {tipo}")

def cargar_desde_json(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        data = json.load(file)
        return cargar_elemento(data)