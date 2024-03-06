import mysql.connector


# funcion para hacer la conexion a la BD y ahorrarme muchas lineas de codigo
def conex_bd():
    host = 'localhost'
    port='3307'
    dataBase='cajero'
    user='root'
    pss='walid00'

    conexion=mysql.connector.connect(host=host,
                                    port=port,
                                    database=dataBase,
                                    user=user,
                                    password=pss
                                    )
    return conexion


# funcion para consultar dni y contraseña y hacer la autenticacion
def autenticacion(conexion, usuario, contraseña):
    try:

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







#funcion para consultar usuarios
def consultar_usuarios(conexion):
    if conexion.is_connected():
        mysql_cursor = conexion.cursor()
        miConsulta = """
            SELECT * FROM Usuario;
        """
        mysql_cursor.execute(miConsulta)
        mysql_lista = mysql_cursor.fetchall()
        conexion.close()
        return mysql_lista
        



# funcion para crear usuarios
def crear_usuarios(conexion):
    dni = input("Introduzca dni: ")
    contraseña = input("Introduzca contraseña: ")

    if conexion.is_connected():
        mysql_cursor=conexion.cursor()
        miConsulta=f"""

                    insert into Usuario (dni, contraseña, rol) 
                    values ("{dni}", "{contraseña}", 0);
                    
                    """
            # aqui lo que puedes hacer es que con un input y un if puedes hacer muchas 'mi consultas'
        mysql_cursor.execute(miConsulta)
        conexion.commit()  

        # mysql_lista=mysql_cursor.fetchall() 
        conexion.close()
        print(f"Usuario '{dni}' creado correctamente.")




# funcion para borrar cualquier usuario
def borrar_usuarios(conexion):
    dni = input("Introduzca dni del usuario a borrar: ")
    contraseña = input("Introduzca contraseña: ")

    if dni.lower() == "admin":
        return print("No puede borrar la cuenta de administrador")

    if conexion.is_connected():
        mysql_cursor = conexion.cursor()

        miConsulta = f"""
            DELETE FROM cajero.Usuario
            WHERE dni = '{dni}' AND contraseña = '{contraseña}';
        """

        mysql_cursor.execute(miConsulta)
        conexion.commit()

        conexion.close()
        print(f"Usuario con dni: '{dni}' eliminado correctamente.")




# modificar usuario pasandole el dni actual del cliente y los nuevos parametros
def modificar_usuario(conexion):
    dni = input("Introduzca dni del usuario que va a modificar: ")
    new_dni = input("Introduzca el nuevo dni que va a tener el usuario: ")
    new_pass = input("Introduzca la nueva contraseña que va a tener el usuario: ")
    

    if conexion.is_connected():
        mysql_cursor = conexion.cursor()

        miConsulta = f"""
            UPDATE cajero.Usuario
            SET dni = '{new_dni}', contraseña = '{new_pass}'
            WHERE dni = '{dni}';
        """

        mysql_cursor.execute(miConsulta)
        conexion.commit()

        conexion.close()

        print("Usuario actualizado correctamente.")




def nueva_sesion(conexion):
    pass
# aqui lo que tengo que hacer es que de una forma coja el identificador del usuario que está activo ahora mismo en esta "sesion" guardarla en una variable y pasarselo a NUEVA_SESION



# funcion para crear consultar saldo del cliente
        
