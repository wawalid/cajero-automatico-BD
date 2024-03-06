from funciones import *


repetir = True


def menu_admin():
    repetir = True
    print("\nBienvenido al panel de administrador")
    while repetir:
        print("\nA- Crear usuario \nB- Borrar usuario \nC- Modificar usuario \nD- Consultar usuarios \nF- Salir")
        opcion_1_1 = input("¿Que desea hacer?: ")
        if opcion_1_1.lower() == "a":
            with conex_bd() as conexion:
                crear_usuarios(conexion)
        elif opcion_1_1.lower() == "b":
            with conex_bd() as conexion:    
                borrar_usuarios(conexion)
        elif opcion_1_1.lower() == "c":
            with conex_bd() as conexion:    
                modificar_usuario(conexion)
        elif opcion_1_1.lower() == "d":
            with conex_bd() as conexion:
                mysql_lista = consultar_usuarios(conexion)
                
                if mysql_lista is not None:
                    for usuario in mysql_lista:
                        print(usuario)
                else:
                    print("Error fetching user data.")
        elif opcion_1_1.lower() == "f":
            repetir = False
            print("Hasta la proxima")
        else:
            print("Opción no válida")


conexion = conex_bd()


def menu_cliente():
    repetir = True
    print(f"Bienvenido cliente con dni '{dni_user}' ")
    while repetir:
        print("A- Crear transacción \nB- Mostrar transacciones ")







print("Iniciar sesion")
dni_user = input("Introduzca dni: ")
pass_user = input("Introduzca contraseña: ")
mysql_lista = autenticacion(conexion , dni_user, pass_user)

if mysql_lista:
    for usuario in mysql_lista:
        if usuario['dni'] == "admin":
            menu_admin()
        else:
            menu_cliente()
else:
    print("Usuario no encontrado o error en la consulta.")








