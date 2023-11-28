import csv

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