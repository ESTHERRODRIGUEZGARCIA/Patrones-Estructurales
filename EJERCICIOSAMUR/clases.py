from abc import ABC, abstractmethod
from datetime import datetime

#interfaces
class Componente(ABC):
    @abstractmethod
    def getNombre(self):
        pass

    @abstractmethod
    def getTipo(self):
        pass

    @abstractmethod
    def getTamaño(self):
        pass

#clases concretas
class Documento(Componente):
    def __init__(self, nombre, tipo, tamaño, contenido):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño
        self.contenido = contenido

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo

    def getTamaño(self):
        return self.tamaño

class Enlace(Componente):
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return "Enlace"

    def getTamaño(self):
        return 0

class Carpeta(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return "Carpeta"

    def getTamaño(self):
        return sum(elemento.getTamaño() for elemento in self.elementos)

#proxy
class ProxyAcceso:
    def __init__(self, usuario):
        self.usuario = usuario
        self.registro = {}

    def acceder(self, documento):
        if documento.getTipo() == "Confidencial":
            self.registrar_acceso(documento)
        # Lógica de autorización aquí

    def registrar_acceso(self, documento):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        self.registro[documento.getNombre()] = (self.usuario, timestamp)
