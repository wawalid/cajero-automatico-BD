from funciones import *


repetir = True


def menu_admin():
    while repetir:
        print("Bienvenido al panel de administrador")
        print("A- Crear usuario \nB- Borrar usuario \nC- Consultar usuarios \nD- Salir")
        opcion_1_1 = input("¿Que desea hacer?: ")
        if opcion_1_1.lower() == "a":
            crear_usuarios()
        elif opcion_1_1.lower() == "b":
            borrar_usuarios()
        elif opcion_1_1.lower() == "c":
            consulta_user()
        elif opcion_1_1.lower() == "d":
            repetir = False
            print("Hasta la proxima")
        else:
            print("Ópcion no válida")





def menu_cliente():
    print("menu cliente")





def consulta_user(usuario, contraseña):
    host = 'localhost'
    port = '3307'
    dataBase = 'cajero'
    user = 'root'
    pss = 'walid00'

    try:
        conexion = mysql.connector.connect(
            host=host,
            port=port,
            database=dataBase,
            user=user,
            password=pss
        )

        if conexion.is_connected():
            mysql_cursor = conexion.cursor(dictionary=True) 
            miConsulta=f"""

                        select * from Usuario where dni = "{usuario}" and contraseña = "{contraseña}";
                        
                        """
            
            mysql_cursor.execute(miConsulta)
            
            mysql_lista = mysql_cursor.fetchall()
            conexion.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return mysql_lista

print("Iniciar sesion")
dni_user = input("Introduzca dni: ")
pass_user = input("Introduzca contraseña: ")
mysql_lista = consulta_user(dni_user, pass_user)

if mysql_lista:
    for usuario in mysql_lista:
        if usuario['dni'] == "admin":
            menu_admin()
        else:
            menu_cliente()
else:
    print("Usuario no encontrado o error en la consulta.")








