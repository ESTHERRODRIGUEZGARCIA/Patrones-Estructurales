from datetime import datetime
import csv
import json

# Componente base del patrón Composite
class Componente:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def mostrar(self, nivel=0):
        indentacion = " "*nivel
        resultado = f"{indentacion}{self.nombre}/ (Tipo: {self.tipo})\n"
        return resultado

# Hoja del Composite - representa un documento
class Documento(Componente):
    def __init__(self, nombre, tipo, tamanio, sensible):
        super().__init__(nombre)
        self.tipo = tipo
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
        self.registro_acceso.append(info_acceso)
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

# Proxy para controlar y registrar el acceso a documentos específicos
class ProxyAcceso:
    def __init__(self, usuario):
        self.usuario = usuario

    def acceder_documento(self, documento):
        print(f"Acceso a {documento.nombre} registrado para el usuario {self.usuario}.")
        documento.accesos.append((self.usuario, str(datetime.now())))



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



def acceder_a_carpeta_o_enlace(carpeta_personal):
    while True:
        print("Seleccione una opción:")
        print("1. Ver carpetas")
        print("2. Ver enlaces")
        print("3. Salir")

        opcion = input("Ingrese su elección: ")

        if opcion == '1':
            print("Carpetas disponibles:")
            for i, elemento in enumerate(carpeta_personal.contenido, start=1):
                if isinstance(elemento, Carpeta):
                    print(f"{i}. {elemento.nombre}")

            eleccion = input("Seleccione una carpeta: ")
            try:
                indice_carpeta = int(eleccion) - 1
                carpeta_seleccionada = carpeta_personal.contenido[indice_carpeta]
                if isinstance(carpeta_seleccionada, Carpeta):
                    return carpeta_seleccionada
                else:
                    print("La selección no es una carpeta válida.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
            except IndexError:
                print("Índice fuera de rango. Inténtelo de nuevo.")

        elif opcion == '2':
            print("Enlaces disponibles:")
            for i, elemento in enumerate(carpeta_personal.contenido, start=1):
                if isinstance(elemento, Enlace):
                    print(f"{i}. {elemento.nombre} -> {elemento.destino.nombre}")

            eleccion = input("Seleccione un enlace: ")
            try:
                indice_enlace = int(eleccion) - 1
                enlace_seleccionado = carpeta_personal.contenido[indice_enlace]
                if isinstance(enlace_seleccionado, Enlace):
                    return enlace_seleccionado.destino
                else:
                    print("La selección no es un enlace válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
            except IndexError:
                print("Índice fuera de rango. Inténtelo de nuevo.")

        elif opcion == '3':
            exit()

        else:
            print("Opción no válida. Inténtelo de nuevo.")

def cargar_desde_json(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        data = json.load(file)
        return cargar_elemento(data)

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



def main():
    autenticacion = AutenticacionUsuarios()

    autenticacion.cargar_usuarios_csv()
    carpeta_personal = None

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
                    carpeta_personal = cargar_desde_json('estructura_usuario.json')
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
            carpeta_actual = carpeta_personal
            while True:
                if isinstance(carpeta_actual, Carpeta):  # Verifica que carpeta_actual sea una instancia de Carpeta
                    print("Carpeta actual:", carpeta_actual.nombre)
                    carpeta_o_enlace = acceder_a_carpeta_o_enlace(carpeta_actual)
                    if isinstance(carpeta_o_enlace, Documento):
                        proxy.acceder_documento(carpeta_o_enlace)
                        print("Interacción ficticia para el documento.")
                    elif isinstance(carpeta_o_enlace, Carpeta):
                        carpeta_actual = carpeta_o_enlace
                    else:
                        print("Error desconocido al acceder a carpeta/enlace.")
                else:
                    print("La carpeta actual no es válida.")
                    break
        elif opcion == '2':
            exit()
        else:
            print("Opción no válida. Inténtelo de nuevo.\n")

if __name__ == "__main__":
    main()