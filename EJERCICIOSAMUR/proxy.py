from datetime import datetime

# Proxy para controlar y registrar el acceso a documentos específicos
class ProxyDocumento:
    def __init__(self, real_documento):
        self._real_documento = real_documento

    def request(self):
        if self.check_access():
            self._real_documento.request()
            self.log_access()

    def check_access(self):
        print("ProxyDocumento: Checking access prior to firing a real request.")
        # Agrega tu lógica de verificación de acceso aquí
        return True

    def log_access(self):
        print("ProxyDocumento: Logging the time of request.", end="")


class ProxyEnlace:
    def __init__(self, real_enlace):
        self._real_enlace = real_enlace

    def request(self):
        if self.check_access():
            self._real_enlace.request()
            self.log_access()

    def check_access(self):
        print("ProxyEnlace: Checking access prior to firing a real request.")
        # Agrega tu lógica de verificación de acceso aquí
        return True

    def log_access(self):
        print("ProxyEnlace: Logging the time of request.", end="")



class ProxyCarpeta:
    def __init__(self, real_carpeta):
        self._real_carpeta = real_carpeta

    def mostrar(self, nivel=0):
        if self.check_access():
            self._real_carpeta.mostrar(nivel)
            self.log_access()

    def check_access(self):
        print("ProxyCarpeta: Checking access prior to firing a real request.")
        # Agrega tu lógica de verificación de acceso aquí
        return True

    def log_access(self):
        print("ProxyCarpeta: Logging the time of request.", end="")