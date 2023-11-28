from datetime import datetime

# Proxy para controlar y registrar el acceso a documentos específicos
class ProxyAcceso:
    def __init__(self, usuario):
        self.usuario = usuario

    def acceder_documento(self, documento):
        print(f"Acceso a {documento.nombre} registrado para el usuario {self.usuario}.")
        documento.accesos.append((self.usuario, str(datetime.now())))
