import mysql.connector


def consultar_usuarios():

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
    if conexion.is_connected():
        mysql_cursor=conexion.cursor()
        miConsulta=f"""

            select * from Usuario;
                    
                    """
            # aqui lo que puedes hacer es que con un input y un if puedes hacer muchas 'mi consultas'
        mysql_cursor.execute(miConsulta)  

        mysql_lista=mysql_cursor.fetchall()
        conexion.close()
        for usuario in mysql_lista:
            print(usuario)

def crear_usuarios():
    usuario = input("Introduzca nombre: ")
    contraseña = input("Introduzca contraseña: ")

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
    if conexion.is_connected():
        mysql_cursor=conexion.cursor()
        miConsulta=f"""

                    insert into Usuario (dni, contraseña, rol) values ("{usuario}", "{contraseña}", 0);
                    
                    """
            # aqui lo que puedes hacer es que con un input y un if puedes hacer muchas 'mi consultas'
        mysql_cursor.execute(miConsulta)
        conexion.commit()  

        mysql_lista=mysql_cursor.fetchall()
        conexion.close()
        print(mysql_lista)



def borrar_usuarios():
    usuario = input("Introduzca nombre: ")
    contraseña = input("Introduzca contraseña: ")

    host = 'localhost'
    port = '3307'
    dataBase = 'cajero'
    user = 'root'
    pss = 'walid00'

    conexion = mysql.connector.connect(host=host, port=port, database=dataBase, user=user, password=pss)

    if conexion.is_connected():
        mysql_cursor = conexion.cursor()

        miConsulta = f"""
            DELETE FROM cajero.Usuario
            WHERE dni = '{usuario}' AND contraseña = '{contraseña}';
        """

        mysql_cursor.execute(miConsulta)
        conexion.commit()

        conexion.close()
        print("Usuario eliminado correctamente.")



