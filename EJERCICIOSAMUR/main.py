from proxy import ProxyDocumento
from composite import Carpeta
from ver_usuarios import AutenticacionUsuarios
from cargar_json import cargar_desde_json, guardar_json
from interaccion import acceder_a_elemento, añadir_elemento_aleatorio, eliminar_elemento


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
                    carpeta_personal = cargar_desde_json('archivos.json')
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

    proxy = ProxyDocumento(usuario_autenticado)

    while True:
        print("1. Acceder a documentos")
        print("2. Añadir elemento")
        print("3. Eliminar elemento")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            carpeta_actual = carpeta_personal
            while True:
                if isinstance(carpeta_actual, Carpeta):  
                    print("Carpeta actual:", carpeta_actual.nombre)
                    acceder_a_elemento(carpeta_actual, usuario_autenticado)
                else:
                    print("La carpeta actual no es válida.")
                    break
        elif opcion == '2':
            añadir_elemento_aleatorio(carpeta_personal)
            guardar_json('archivos.json', carpeta_personal)
        elif opcion == '3':
            eliminar_elemento(carpeta_personal)
            guardar_json('archivos.json', carpeta_personal)
        elif opcion == '4':
            exit()
        else:
            print("Opción no válida. Inténtelo de nuevo.\n")

if __name__ == "__main__":
    main()