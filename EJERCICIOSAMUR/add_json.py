from datetime import datetime
import csv
import json


# Componente base del patrón Composite
class Componente:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        pass

# Hoja del Composite - representa un documento
class Documento(Componente):
    def __init__(self, nombre, tipo_documento, tamaño, sensible=False):
        super().__init__(nombre)
        self.tipo_documento = tipo_documento
        self.tamaño = tamaño
        self.sensible = sensible
        self.registro_acceso = []

    def mostrar(self):
        return f"{self.nombre} ({self.tipo_documento}, {self.tamaño}KB)"

    def acceder(self, usuario):
        timestamp = datetime.now()
        info_acceso = f"{usuario} accedió a {self.nombre} en {timestamp}"
        self.registro_acceso.append(info_acceso)
        print(info_acceso)

# Hoja del Composite - representa un enlace
class Enlace(Componente):
    def __init__(self, nombre, destino):
        super().__init__(nombre)
        self.destino = destino

    def mostrar(self):
        return f"{self.nombre} (Enlace a {self.destino.mostrar()})"

# Composite - representa una carpeta
class Carpeta(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.hijos = []

    def agregar(self, componente):
        self.hijos.append(componente)

    def eliminar(self, componente):
        self.hijos.remove(componente)

    def mostrar(self):
        carpeta_str = f"{self.nombre} (Carpeta)\n"
        for hijo in self.hijos:
            carpeta_str += f"  {hijo.mostrar()}\n"
        return carpeta_str

# Proxy para controlar y registrar el acceso a documentos específicos
class ProxyAcceso:
    def __init__(self, usuario):
        self.usuario = usuario

    def acceder_documento(self, documento):
        if documento.sensible:
            documento.acceder(self.usuario)
        else:
            print(f"{self.usuario} accedió a {documento.nombre}")

# Funciones de utilidad
def crear_estructura_ejemplo():
    doc1 = Documento("Documento1", "Texto", 50, sensible=True)
    doc2 = Documento("Documento2", "Imagen", 100)
    enlace = Enlace("Enlace1", doc1)
    carpeta = Carpeta("Carpeta1")
    carpeta.agregar(doc2)
    carpeta.agregar(enlace)

    return carpeta

# Clase para manejar la autenticación de usuarios
class AutenticacionUsuarios:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, usuario, contraseña):
        self.usuarios.append({'usuario': usuario, 'contraseña': contraseña, 'carpeta_personal': None})
        self.guardar_usuarios_csv()

    def autenticar_usuario(self, usuario, contraseña):
        for user in self.usuarios:
            if user['usuario'] == usuario and user['contraseña'] == contraseña:
                return user
        return None

    def cargar_usuarios_csv(self):
        try:
            with open('usuarios.csv', newline='') as file:
                reader = csv.DictReader(file)
                self.usuarios = list(reader)
        except FileNotFoundError:
            self.usuarios = []

    def guardar_usuarios_csv(self):
        with open('usuarios.csv', mode='w', newline='') as file:
            fieldnames = ['usuario', 'contraseña', 'carpeta_personal']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in self.usuarios:
                writer.writerow(user)

# Función para cargar documentos desde un archivo JSON
def cargar_documentos_desde_json(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        data = json.load(file)
        documentos = data.get('documentos', [])
        return [Documento(doc['nombre'], doc['tipo_documento'], doc['tamaño'], doc.get('sensible', False)) for doc in documentos]

# Clase para manejar la autenticación de usuarios
class AutenticacionUsuarios:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, usuario, contraseña):
        self.usuarios.append({'usuario': usuario, 'contraseña': contraseña, 'carpeta_personal': None})
        self.guardar_usuarios_csv()

    def autenticar_usuario(self, usuario, contraseña):
        for user in self.usuarios:
            if user['usuario'] == usuario and user['contraseña'] == contraseña:
                return user
        return None

    def cargar_usuarios_csv(self):
        try:
            with open('usuarios.csv', newline='') as file:
                reader = csv.DictReader(file)
                self.usuarios = list(reader)
        except FileNotFoundError:
            self.usuarios = []

    def guardar_usuarios_csv(self):
        with open('usuarios.csv', mode='w', newline='') as file:
            fieldnames = ['usuario', 'contraseña', 'carpeta_personal']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in self.usuarios:
                writer.writerow(user)


def main():
    autenticacion = AutenticacionUsuarios()

    autenticacion.cargar_usuarios_csv()

    while True:
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            user_data = autenticacion.autenticar_usuario(usuario, contraseña)
            if user_data:
                usuario_autenticado = user_data['usuario']
                print(f"Bienvenido, {usuario_autenticado}!\n")
                carpeta_personal = user_data['carpeta_personal']
                if carpeta_personal is None:
                    documentos = cargar_documentos_desde_json('documentos.json')
                    carpeta_personal = Carpeta("CarpetaPersonal")
                    for doc in documentos:
                        carpeta_personal.agregar(doc)
                    user_data['carpeta_personal'] = carpeta_personal
                break
            else:
                print("Usuario o contraseña incorrectos. Inténtelo de nuevo.\n")
        elif opcion == '2':
            usuario = input("Nuevo usuario: ")
            contraseña = input("Contraseña: ")
            autenticacion.registrar_usuario(usuario, contraseña)
            print("Usuario registrado exitosamente. Ahora puede iniciar sesión.\n")
        elif opcion == '3':
            exit()
        else:
            print("Opción no válida. Inténtelo de nuevo.\n")

    proxy = ProxyAcceso(usuario_autenticado)

    while True:
        print("1. Acceder a documentos")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            if isinstance(carpeta_personal, Carpeta):  # Verifica si es una instancia de Carpeta
                print(carpeta_personal.mostrar())
                nombre_documento = input("Ingrese el nombre del documento a acceder: ")
                documento_seleccionado = None
                for child in carpeta_personal.hijos:
                    if isinstance(child, Documento) and child.nombre == nombre_documento:
                        documento_seleccionado = child
                        break
                if documento_seleccionado:
                    proxy.acceder_documento(documento_seleccionado)
                else:
                    print("Documento no encontrado.\n")
            else:
                print("La carpeta personal no está correctamente configurada. Asegúrate de cargar los documentos correctamente.\n")
        elif opcion == '2':
            exit()
        else:
            print("Opción no válida. Inténtelo de nuevo.\n")

if __name__ == "__main__":
    main()