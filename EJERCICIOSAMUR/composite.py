from datetime import datetime
from abc import ABC, abstractmethod

# Componente base del patrón Composite
class Componente(ABC):
    @abstractmethod
    def __init__(self, nombre, tipo, **kwargs):
        self.nombre = nombre
        self.tipo = tipo

    def mostrar(self, nivel=0):
        indentacion = " "*nivel
        resultado = f"{indentacion}{self.nombre}/ (Tipo: {self.tipo})\n"
        return resultado

# Hoja del Composite - representa un documento
class Documento(Componente):
    def __init__(self, nombre, tipo, tamanio, sensible):
        super().__init__(nombre, tipo)
        self.tamanio = tamanio
        self.sensible = sensible
        self.accesos = []

    def mostrar(self, nivel=0):
        indentacion = " " * nivel
        resultado = f"{indentacion}{self.nombre} (Tipo: {self.tipo}, Tamaño: {self.tamanio} KB)\n"
        return resultado
    
    def acceder(self, usuario):
        timestamp = datetime.now()
        info_acceso = f"{usuario} accedió a {self.nombre} en {timestamp}"
        self.accesos.append(info_acceso)
        print(info_acceso)

# Hoja del Composite - representa un enlace
class Enlace(Componente):
    def __init__(self, nombre, destino):
        super().__init__(nombre, "Enlace")
        self.destino = destino

    def mostrar(self, nivel=0):
        indentacion = " "*nivel
        resultado = f"{indentacion}{self.nombre} -> {self.destino.nombre} (Tipo: {self.tipo})\n"
        return resultado
    
# Composite - representa una carpeta
class Carpeta(Componente):
    def __init__(self, nombre):
        super().__init__(nombre, "Carpeta")
        self.contenido = []

    def agregar(self, componente):
        self.contenido.append(componente)

    def eliminar(self, componente):
        self.contenido.remove(componente)

    def mostrar(self, nivel=0):
        indentacion = " "*nivel
        resultado = super().mostrar(nivel)
        for elemento in self.contenido:
            resultado += elemento.mostrar(nivel + 1)
        return resultado