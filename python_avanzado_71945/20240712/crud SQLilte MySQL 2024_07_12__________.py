####################################################################################################
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tEnter para continuar")
    limpiar()
from colorama import *
####################################################################################################
limpiar()
from datetime import datetime, date, time
# ~ nuevo(0,estado='inicio',modulo=4)
import math
import datetime
####################################################################################################
####################################################################################################
#                                                                                                  #
#                                        Bases de datos                                            #
#                                                                                                  #
####################################################################################################

print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    ╔═══════╗            ╦                                   ╦   ╔═══╦═══╗   ║
║    ║                    ║                                   ║       ║       ║
║    ║                    ║                                   ║       ║       ║
║    ║                    ║                                   ║       ║       ║
║    ╠══════╣     ╔═══════╣    ╦       ╦    ╔═══════╗         ║       ║       ║
║    ║            ║       ║    ║       ║    ║                 ║       ║       ║
║    ║            ║       ║    ║       ║    ║          ╔╗     ║       ║       ║
║    ╚═══════╝    ╚═══════╝    ╚═══════╝    ╚═══════╝  ╚╝     ╩       ╩       ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
║                                                                             ║
║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║
║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║  ╔═════╗   ╔╗       ╔╗   ╔═════╗    ╔╗      ╦                               ║
║ ╔╝     ╚╗   ║       ║   ╔╝     ╚╗   ║╚╗     ║                               ║
║ ║       ║   ╚╗     ╔╝   ║       ║   ║ ╚╗    ║                               ║
║ ║       ║    ║     ║    ║       ║   ║  ╚╗   ║                               ║
║ ╠═══════╣    ╚╗   ╔╝    ╠═══════╣   ║   ╚╗  ║  ╠═════╣                      ║
║ ║       ║     ║   ║     ║       ║   ║    ╚╗ ║                               ║
║ ║       ║     ╚╗ ╔╝     ║       ║   ║     ╚╗║                               ║
║ ╩       ╩      ╚═╝      ╩       ╩   ╩      ╚╝                               ║
║                                                                             ║
║                                                                             ║
║                             ╔═══════╗   ╔═════╗  ╔══════╗    ╔═════╗        ║
║                                    ╔╝  ╔╝     ╚╗ ║      ╚╗  ╔╝     ╚╗       ║
║                                   ╔╝   ║       ║ ║       ║  ║       ║       ║
║                                  ╔╝    ║       ║ ║       ║  ║       ║       ║
║                               ╔══╝     ╠═══════╣ ║       ║  ║       ║       ║
║                              ╔╝        ║       ║ ║       ║  ║       ║       ║
║                             ╔╝         ║       ║ ║      ╔╝  ╚╗     ╔╝       ║
║                             ╚═══════╝  ╩       ╩ ╚══════╝    ╚═════╝        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝''')
pausa()
limpiar()

base_de_datos=""

while base_de_datos not in ["S","M"]:
    base_de_datos = input("Seleccione entre:\n\tM) para MySQL\n\tS) para SQLite""").upper()

match (base_de_datos):
    case "S":

        print("""\033[1;37;44m\n
        ╔═════════════════════════════════════════════════════════════════════════════╗
        ║                                                                             ║
        ║      ╔═════╗       ╔═════╗       ╦           ╦   ╔═══╦═══╗   ╔═══════╗      ║
        ║     ╔╝     ╚╗     ╔╝     ╚╗      ║           ║       ║       ║              ║
        ║     ║       ║     ║       ║      ║           ║       ║       ║              ║
        ║     ╚╗            ║       ║      ║           ║       ║       ║              ║
        ║      ╚══════╗     ║       ║      ║           ║       ║       ╠═════╣        ║
        ║             ║     ║       ║      ║           ║       ║       ║              ║
        ║     ╚╗     ╔╝     ╚╗    ╔╦╝      ║           ║       ║       ║              ║
        ║      ╚═════╝       ╚════╝╚═╝     ╚═══════╝   ╩       ╩       ╚═══════╝      ║
        ║                                                                             ║
        ╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
        """);
        import sqlite3
    case "M":

        ####################################################################################################
        print("""\033[1;37;44m\n
        ╔═════════════════════════════════════════════════════════════════════════════╗
        ║                                                                             ║
        ║     ╔╗      ╔╗     ╦       ╦      ╔═════╗       ╔═════╗       ╦             ║
        ║     ║╚╗    ╔╝║     ╚╗     ╔╝     ╔╝     ╚╗     ╔╝     ╚╗      ║             ║
        ║     ║ ╚╗  ╔╝ ║      ╚╗   ╔╝      ║       ║     ║       ║      ║             ║
        ║     ║  ╚╗╔╝  ║       ╚╗ ╔╝       ╚╗            ║       ║      ║             ║
        ║     ║   ╚╝   ║        ╚╦╝         ╚══════╗     ║       ║      ║             ║
        ║     ║        ║         ║                 ║     ║       ║      ║             ║
        ║     ║        ║         ║         ╚╗     ╔╝     ╚╗    ╔╦╝      ║             ║
        ║     ╩        ╩         ╩          ╚═════╝       ╚════╝╚═╝     ╚═══════╝     ║
        ║                                                                             ║
        ╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
        """);
        try:
            import mysql.connector
        except Exception as error_:
            import pip
            pip.main(['install', 'mysql-connector-python'])
        from mysql.connector import Error
        from mysql.connector import errorcode
        # ~ try:
            # ~ import pymysql
            # ~ import pymysql.cursors
        # ~ except Exception as error_:
            # ~ import pip
            # ~ pip.main(['install', 'pymysql'])
            # ~ import pymysql
        # ~ import pymysql.cursors

print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║              Conexión al server SQLite                                      ║
║              Conexión a la base de datos                                    ║
║              Conexión a la coleccion                                        ║
║              CRUD (Create-Read-Update-Delete) en SQLite                     ║
║                              Create Database                                ║
║                              Create Table                                   ║
║                              Insert                                         ║
║                              Select                                         ║
║                              Where                                          ║
║                              Where col like '%xx%'                          ║
║                              Order By     ASC DESC                          ║
║                              Delete                                         ║
║                              Drop Table                                     ║
║                              Update                                         ║
║                              Limit                                          ║
║                              Join                                           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
""");

pausa()
limpiar()
import datetime
hoy = datetime.date.today()
print(hoy)

######################################################################################################
def conectar_base_de_datos():
    global connection
    if base_de_datos == "S":#   SQLite
        connection = sqlite3.connect(f'{nombre_DDBB}.db')
    else:#                      MySQL
        usuario = input ("ingrese el usuario: ¿'root'?:")
        if usuario == "":
            usuario = "root"
        password_de_msql= input ("ingrese el password: ¿'2025'?:")
        if password_de_msql == "":
            password_de_msql = "2025"
        host_= input ("ingrese el donde esta la base de datos (host) ¿'localhost'?:")
        if host_ == "":
            host_ = "localhost"
        connection = mysql.connector.connect(host= host_ ,user= usuario , passwd= password_de_msql )
        print (f"mysql.connector.connect(host= {host_},user= {usuario} , passwd= {password_de_msql})")
        try:
            query = f"USE {nombre_DDBB}"
            cursor=connection.cursor()
            resultado =cursor.execute   (query)
            print (f"conectamos o cambiamos a la base de datos {query} ")
            print (f"desde sql {resultado}")
        except:
            print("método 'use' aun no disponible")
    return connection.cursor()

######################################################################################################
def crear_base():
    limpiar()
    print(f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║       ╔═════╗    ╔══════╗   ╔═══════╗   ╔═════╗   ╔═══╦═══╗   ╔═══════╗     ║
║      ╔╝     ╚╗   ║      ╚╗  ║          ╔╝     ╚╗      ║       ║             ║
║      ║           ║       ║  ║          ║       ║      ║       ║             ║
║      ║           ║      ╔╝  ║          ║       ║      ║       ║             ║
║      ║           ╠════╦═╝   ╠═════╣    ╠═══════╣      ║       ╠═════╣       ║
║      ║           ║    ╚╗    ║          ║       ║      ║       ║             ║
║      ╚╗     ╔╝   ║     ╚╗   ║          ║       ║      ║       ║             ║
║       ╚═════╝    ╩      ╚╝  ╚═══════╝  ╩       ╩      ╩       ╚═══════╝     ║
║                                  (crear)                                    ║
║                                                                             ║
║                   creamos la base de datos si no existe                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
""")

    cursor = conectar_base_de_datos()#           sqlite // mysql
    if base_de_datos == "S":#   SQLite
        print               ("se crea en un archivo al generar la coneccion")
    else:#                      MySQL

        query = f"CREATE DATABASE IF NOT EXISTS {nombre_DDBB}"
        print               (query)
        cursor.execute      (query)
        cursor.close
        connection.close
    cursor.close
    connection.close

    pausa()
######################################################################################################
def crear_tablas():
    limpiar()
    print(f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║       ╔═════╗    ╔══════╗   ╔═══════╗   ╔═════╗   ╔═══╦═══╗   ╔═══════╗     ║
║      ╔╝     ╚╗   ║      ╚╗  ║          ╔╝     ╚╗      ║       ║             ║
║      ║           ║       ║  ║          ║       ║      ║       ║             ║
║      ║           ║      ╔╝  ║          ║       ║      ║       ║             ║
║      ║           ╠════╦═╝   ╠═════╣    ╠═══════╣      ║       ╠═════╣       ║
║      ║           ║    ╚╗    ║          ║       ║      ║       ║             ║
║      ╚╗     ╔╝   ║     ╚╗   ║          ║       ║      ║       ║             ║
║       ╚═════╝    ╩      ╚╝  ╚═══════╝  ╩       ╩      ╩       ╚═══════╝     ║
║                                  (crear)                                    ║
║                      creamos las tablas y columnas                          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    print ("Conectamos con SQLite")
    ######################################################################################################

    print ("CREATE TABLE")
    print ("CREATE COLUMN")
    cursor = conectar_base_de_datos()#           sqlite // mysql




    nombre_DDBB = "Curso_Python_2024"
    nombre_tabla = "Mi_Tabla"

    nombre_columna_1 = "descripcion"
    nombre_columna_2 = "precio"
    nombre_columna_3 = "codigo"
    nombre_columna_4 = "vencimiento"
    nombre_columna_5 = "estado"
    if base_de_datos == "S":#   SQLite
        query= (f"""CREATE TABLE IF NOT EXISTS {nombre_tabla}
                                                            (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                                    {nombre_columna_1} VARCHAR(255) NOT NULL,
                                                                    {nombre_columna_2} FLOAT,
                                                                    {nombre_columna_3} VARCHAR(255),
                                                                    {nombre_columna_4} DATE ) """)
    else:#                      MySQL
        query= (f"""CREATE TABLE IF NOT EXISTS {nombre_tabla}
                                                            (id INT     PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                                                    {nombre_columna_1} VARCHAR(255) NOT NULL,
                                                                    {nombre_columna_2} FLOAT,
                                                                    {nombre_columna_3} VARCHAR(255) ,
                                                                    {nombre_columna_4} DATE ); """)

    """---------------------------------------------------------------------------------------------------------------------
                SQLite                                      (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                MySQL                                       (id INT     PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                                                  ^                     ^
                                                                  |_ INT x INTEGER      |_AUTOINCREMENT x AUTO_INCREMENT
    """

    print               (query)
    cursor.execute      (query)
    cursor.close
    connection.close
    pausa()

######################################################################################################
def insertar_datos():
    limpiar()
    print(f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║      ╦    ╦ ╔═══╗      ╔═════╗     ╔═══════╗    ╔══════╗    ╔═══╦═══╗       ║
║      ║    ╠═╝   ╚═╗   ╔╝     ╚╗    ║            ║      ╚╗       ║           ║
║      ║    ║       ║   ║            ║            ║       ║       ║           ║
║      ║    ║       ║   ╚╗           ║            ║      ╔╝       ║           ║
║      ║    ║       ║    ╚══════╗    ╠═════╣      ╠════╦═╝        ║           ║
║      ║    ║       ║           ║    ║            ║    ╚╗         ║           ║
║      ║    ║       ║   ╚╗     ╔╝    ║            ║     ╚╗        ║           ║
║      ╩    ╩       ╩    ╚═════╝     ╚═══════╝    ╩      ╚╝       ╩           ║
║                                  (insertar)                                 ║
║                                                                             ║
║                      insertamos un dato directamente                        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    print ("Conectamos con SQLite")
    cursor = conectar_base_de_datos()#           sqlite // mysql
    print ("RECORD INSERT")
    query = f"""INSERT INTO  {nombre_tabla}  (descripcion, precio, codigo, vencimiento) VALUES('Galletitas', 222 , 'Titas','2025-01-01')"""
    print           (query)
    cursor.execute  (query)
    connection.commit()
    pausa()
    limpiar()
    print("""\033[1;37;44m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos un dato por intermedio de comodines         ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    #   query=f"""INSERT INTO  {nombre_tabla}  (descripcion, precio, codigo, vencimiento) VALUES(?,?,?,?)"""

    query=f"""INSERT INTO  {nombre_tabla}  (descripcion, precio, codigo, vencimiento) """
    if base_de_datos == "S":#   SQLite
        query +=  "VALUES( ?, ?, ?, ?)"
    else:#                      MySQL
        query +=  "VALUES(%s,%s,%s,%s)"

    """
SQLite         VALUES( ?, ?, ?, ?)"
MySQL          VALUES(%s,%s,%s,%s)"
    """

    proy=('Alfajores', 88 , 'ALF','2025-01-01')
    print           (query,proy)
    cursor.execute  (query,proy)
    connection.commit()

    pausa()
    limpiar()
    ######################################################################################################
    print("""\033[1;37;44m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos varios dato por intermedio de comodines     ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)

    #   query = f"""INSERT INTO  {nombre_tabla}  ({nombre_columna_1}, {nombre_columna_2}, {nombre_columna_3}, {nombre_columna_4}) VALUES(?,?,?,?)"""

    query = f"""INSERT INTO  {nombre_tabla}  ({nombre_columna_1}, {nombre_columna_2}, {nombre_columna_3}, {nombre_columna_4}) """
    if base_de_datos == "S":#   SQLite
        query +=  "VALUES( ?, ?, ?, ?)"
    else:#                      MySQL
        query +=  "VALUES(%s,%s,%s,%s)"
    """
SQLite         VALUES( ?, ?, ?, ?)"
MySQL          VALUES(%s,%s,%s,%s)"
    """
    print   (f'columnas_SQLite = ',query)

    cursor.execute  (query, ("Chocolates", 9999 , "Choc", '2025-06-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute  (query, ("Fideos", 30 , "f1", '2025-06-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query, ("Arroz", 25 , "A1", '2025-08-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query, ("Agua", 20 , "H2O", '2025-09-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query, ("Tomates", 15 , "T1", '2025-02-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query, ("Sal", 10, "S1", '2025-10-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query, ("cacao", 30 , "choco", '2025-11-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query, ("gelatina", 25 , "hl", '2025-12-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query, ("flan", 20 , "flan", '2025-01-15'))
    connection.commit()#     <-------                               No eliminar
    print(cursor.rowcount, "record inserted.")
    pausa()
    limpiar()
    ######################################################################################################
    print("""\033[1;37;44m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos varios dato por intermedio de listas 1 a 1  ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    print   (f'columnas_SQLite = ',query)
    proy= ( ("Chocolates", 99 , "Choc", '2025-06-15'),
            ("Fideos", 300 , "f1", '2025-06-15'),
            ("Arroz", 250 , "A1", '2025-08-15'),
            ("Agua", 200 , "H2O", '2025-09-15'),
            ("Tomates", 105 , "T1", '2025-02-15'),
            ("Sal", 100, "S1", '2025-10-15'),
            ("cacao", 300 , "choco", '2025-11-15'),
            ("gelatina", 205 , "hl", '2025-12-15'),
            ("flan", 200 , "flan", '2025-01-15'))
    for datos in proy:
        cursor.execute(query,datos)
        connection.commit()# <-------------------------------------------------destabular
    print(cursor.rowcount, "record inserted.")
    # ~ cursor.execute(query,proy)
    # ~ connection.commit()

    pausa()
    limpiar()
    print("""\033[1;37;44m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos varios dato por intermedio de lista directa ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)

    proy = [
                ("Tomates", 15 , "T1", '2025-07-15'),
                ("Sal", 10, "S1", '2025-02-15'),
                ("Fideos", 30 , "f1", '2025-01-15'),
                ("Arroz", 25 , "A1", '2025-04-15'),
                ("Agua", 20 , "H2O", '2025-07-15'),
                ("Ajies", 15 , "T1", '2025-02-15'),
                ("Pimienta", 10, "S1", '2025-01-15'),
                ("Cafe", 30 , "f1", '2025-04-15'),
                ("Yerba", 25 , "A1", '2025-07-15'),
                ("Te", 20 , "H2O", '2025-02-25'),
                ("Pan", 15 , "T1", '2025-01-15'),
                ("Queso", 10, "S1", '2025-02-15')
            ]
    print             (query,proy)
    cursor.executemany(query,proy)
    connection.commit()

    print(cursor.rowcount, "record inserted in pool.")
    ###################################################################################################
    pausa()
    limpiar()
    print("""\033[1;37;44m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos manualmente                                 ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)

    while True:
        print("Ingreso de datos a mano ")
        pausa()
        dato_desc=""
        while len(dato_desc)<5:
            dato_desc  = input ("Ingrese la descripcion (+ de 5 caracteres) del producto ('ZZ' para Salir): ").upper()
        if dato_desc=="ZZ":
            break

        dato_precio = ""
        while not dato_precio.replace(".","").isdecimal():
            dato_precio=input("ingrese el precio: ")
        dato_precio=float (dato_precio)


        dato_codigo = ""
        while not dato_codigo.isdecimal():
            dato_codigo=input("ingrese el cod.prod:: ")
        dato_codigo= int (dato_precio)

        dato_fecha = datetime.date.today();

        cursor.execute  (query, (dato_desc, dato_precio , dato_codigo, dato_fecha))
        connection.commit()
        print(cursor.rowcount, "record inserted.")

######################################################################################################
def leer_tabla():
    pausa()
    limpiar()
    print(f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                  ╔══════╗   ╔═══════╗   ╔═════╗   ╔══════╗                  ║
║                  ║      ╚╗  ║          ╔╝     ╚╗  ║      ╚╗                 ║
║                  ║       ║  ║          ║       ║  ║       ║                 ║
║                  ║      ╔╝  ║          ║       ║  ║       ║                 ║
║                  ╠════╦═╝   ╠═════╣    ╠═══════╣  ║       ║                 ║
║                  ║    ╚╗    ║          ║       ║  ║       ║                 ║
║                  ║     ╚╗   ║          ║       ║  ║      ╔╝                 ║
║                  ╩      ╚╝  ╚═══════╝  ╩       ╩  ╚══════╝                  ║
║                                   (leer)                                    ║
║                                                                             ║
║                      leemos todos los datos de Mi_Tabla                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    cursor = conectar_base_de_datos()#           sqlite // mysql
    cursor.execute("SELECT * FROM Mi_Tabla ")
    #print (cursor,type(cursor), dir (cursor))
    for linea in cursor:
        print (linea)
    pausa()
    limpiar()
    '''
    -- WHERE `vencimiento` >= '2025-01-01' AND  `vencimiento` <= '2025-01-01';
    -- WHERE `vencimiento` >= '2025-01-01' OR  `vencimiento` <= '2025-01-01';
    -- WHERE NOT (`vencimiento` >= '2025-01-01' OR  `vencimiento` <= '2025-01-01');
    -- WHERE codigo IN ('H2O','S1','A1');
    -- WHERE precio BETWEEN 10 AND  100;
    -- WHERE precio BETWEEN 10 AND  100;
    -- WHERE descripcion like 'A%';
    -- WHERE descripcion like '%r%';-- #                    % cualquier cantidad de caracteres
    -- WHERE descripcion like 'A___z';-- #Arroz             _ un solo caracter
    -- WHERE descripcion REGEXP  '^A';-- #                  REGULAR EXPRESION ^inicio, fin^, | or, [caracteres] entres estos , [a-h] entre a y h
    -- WHERE descripcion IS NULL;
    -- WHERE descripcion IS NOT NULL;
        '''
    # ~ query ="SELECT * FROM Mi_Tabla "
    # ~ query ="SELECT * FROM Mi_Tabla WHERE precio BETWEEN 10 AND  100 and codigo like '%Z'; "
    # ~ query ="SELECT * FROM Mi_Tabla WHERE codigo IN 'H2O','S1','A1'; "
    # ~ query ="SELECT * FROM Mi_Tabla WHERE codigo like '%H%'; "
    # ~ inicio = input ("INgrese las primeras letras del producto a buscar:")
    # ~ inicio = inicio +"%"
    inicio = "A%"
    query =(f"SELECT * FROM Mi_Tabla WHERE descripcion like '{inicio}'; ")
    print               (query)
    cursor.execute      (query)
    prod = cursor
    for linea in prod:
        print (f"filtrados {linea}")
    pausa()
    limpiar()
    cursor.close
    connection.close
######################################################################################################
def Actualizar_datos():
    limpiar()
    print(f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║     ╦       ╦   ╔══════╗   ╔══════╗      ╔═════╗   ╔═══╦═══╗   ╔═══════╗    ║
║     ║       ║   ║      ╚╗  ║      ╚╗    ╔╝     ╚╗      ║       ║            ║
║     ║       ║   ║       ║  ║       ║    ║       ║      ║       ║            ║
║     ║       ║   ║      ╔╝  ║       ║    ║       ║      ║       ║            ║
║     ║       ║   ╠══════╝   ║       ║    ╠═══════╣      ║       ╠═════╣      ║
║     ║       ║   ║          ║       ║    ║       ║      ║       ║            ║
║     ╚╗     ╔╝   ║          ║      ╔╝    ║       ║      ║       ║            ║
║      ╚═════╝    ╩          ╚══════╝     ╩       ╩      ╩       ╚═══════╝    ║
║                                (actualizar)                                 ║
║                                                                             ║
║                      Actualizamos datos de la Base/tabla                    ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    cursor = conectar_base_de_datos()#           sqlite // mysql

    query = f"UPDATE {nombre_tabla} SET {nombre_columna_3} = 'T_lta' WHERE {nombre_columna_1} = 'Tomates' "
    print (query)
    cursor.execute(query)
    connection.commit()
    print(cursor.rowcount, "record(s) affected")
    pausa()

######################################################################################################
def Borrar_datos():
    limpiar()
    print(f"""\033[1;37;44m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║     ╔══════╗    ╔═══════╗   ╦           ╔═══════╗  ╔═══╦═══╗   ╔═══════╗    ║
    ║     ║      ╚╗   ║           ║           ║              ║       ║            ║
    ║     ║       ║   ║           ║           ║              ║       ║            ║
    ║     ║       ║   ║           ║           ║              ║       ║            ║
    ║     ║       ║   ╠═════╣     ║           ╠═════╣        ║       ╠═════╣      ║
    ║     ║       ║   ║           ║           ║              ║       ║            ║
    ║     ║      ╔╝   ║           ║           ║              ║       ║            ║
    ║     ╚══════╝    ╚═══════╝   ╚═══════╝   ╚═══════╝      ╩       ╚═══════╝    ║
    ║                                  (eliminar)                                 ║
    ║                                                                             ║
    ║                         borramos datos de la base                           ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    cursor = conectar_base_de_datos()#           sqlite // mysql
    query = f"DELETE FROM {nombre_tabla}  WHERE {nombre_columna_1} = 'Sal'"# and {columna2} = '{dato2}'
    cursor.execute(query )
    print(cursor.rowcount, "record(s) affected")
    query = f"DELETE FROM {nombre_tabla}  WHERE {nombre_columna_1} = "

    if base_de_datos == "S":#   SQLite
        query +=  " ? ;"
    else:#                      MySQL
        query +=  "%s ;"
    """
SQLite         ?  ; "
MySQL          %s ; "
    """

    proy = ("Te", ) # VA una coma para generar una lista
    print         (query , proy)
    cursor.execute(query , proy)
    connection.commit()
    print(cursor.rowcount, "record(s) affected")
    pausa()
    #--------------------------------------------------------------------
    proy = ("pizza", ) # VA una coma para generar una lista
    print         (query , proy)
    cursor.execute(query , proy)
    connection.commit()
    print(cursor.rowcount, "record(s) affected")
    pausa()
def Borrar_tablas():
    limpiar()
    cursor = conectar_base_de_datos()#           sqlite // mysql

    print("""\033[1;37;44m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                         borramos la tabla de la base                        ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    try:
        query= f"DROP TABLE IF EXISTS  {nombre_tabla}"
        print                           (query)
        resultado=cursor.execute        (query)

        print ("cursor.execute:",resultado)
        print(cursor.rowcount, "record(s) affected")
        print (f"tabla  {nombre_tabla} eliminada ")
    except Exception as Error:
        print (f"tabla  {nombre_tabla} no se pudo eliminar por la excepcion:\n {Error} ")
    pausa()

def Borrar_base():
    limpiar()
    cursor = conectar_base_de_datos()#           sqlite // mysql
    print(f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                  ╔══════╗  ╔══════╗    ╔═════╗   ╔══════╗                   ║
║                  ║      ╚╗ ║      ╚╗  ╔╝     ╚╗  ║      ╚╗                  ║
║                  ║       ║ ║       ║  ║       ║  ║       ║                  ║
║                  ║       ║ ║      ╔╝  ║       ║  ║      ╔╝                  ║
║                  ║       ║ ╠════╦═╝   ║       ║  ╠══════╝                   ║
║                  ║       ║ ║    ╚╗    ║       ║  ║                          ║
║                  ║      ╔╝ ║     ╚╗   ╚╗     ╔╝  ║                          ║
║                  ╚══════╝  ╩      ╚╝   ╚═════╝   ╩                          ║
║                                  (borrar)                                   ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    """
SQLite        no puede eliminarse desde dentro "
MySQL         se elimina con drop "
    """
    if base_de_datos == "S":#   SQLite
        print ("borramos base por archivos")
        try:
            os.remove(f'{nombre_DDBB}')
        except:
            print("el archivo esta abierto o no existe")
    else:#                      MySQL
        print ("borramos base por puerto 3306")
        try:

            limpiar()
            cursor = conectar_base_de_datos()#           sqlite // mysql
            cursor.execute(f"DROP DATABASE IF EXIST {nombre_DDBB}")
            cursor.close
            connection.close
            print (f"base de datos  {nombre_DDBB} eliminada ")
        except Exception as Error:
            print (f"base de datos  {nombre_DDBB} no se pudo eliminar por la excepcion:\n {Error} ")
    pausa()
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


opcion = ""

nombre_DDBB = "Curso_Python_2024"
nombre_tabla = "Mi_Tabla"

nombre_columna_1 = "descripcion"
nombre_columna_2 = "precio"
nombre_columna_3 = "codigo"
nombre_columna_4 = "vencimiento"



while opcion !="0":
    limpiar()
    print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                 ╔═════╗    ╔══════╗    ╦       ╦    ╔══════╗                ║
║                ╔╝     ╚╗   ║      ╚╗   ║       ║    ║      ╚╗               ║
║                ║           ║       ║   ║       ║    ║       ║               ║
║                ║           ║      ╔╝   ║       ║    ║       ║               ║
║                ║           ╠════╦═╝    ║       ║    ║       ║               ║
║                ║           ║    ╚╗     ║       ║    ║       ║               ║
║                ╚╗     ╔╝   ║     ╚╗    ╚╗     ╔╝    ║      ╔╝               ║
║                 ╚═════╝    ╩      ╚╝    ╚═════╝     ╚══════╝                ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)

# ~ print(cursor.rowcount, "record inserted in pool.")

    print ("\n\n\n");

    print ("1) Create - Crear base");
    print ("2) Create - Crear tablas");
    print ("3) Insert - Insertar datos");
    print ("4) Read   - Leer datos");
    print ("5) Update - Actualizar datos");
    print ("6) Delete - Borrar datos");
    print ("7) Delete - Borrar tablas");
    print ("8) Delete - Borrar BBDD");

    print ("0) Salir del programa")
    opcion=input("Ingrese la opción seleccionada :").upper()
    if opcion == "1":
        crear_base()
    elif opcion == "2":
        crear_tablas()
    elif opcion == "3":
        insertar_datos()
    elif opcion == "4":
        leer_tabla()
    elif opcion == "5":
        Actualizar_datos()
    elif opcion == "6":
        Borrar_datos()
    elif opcion == "7":
        Borrar_tablas()
    elif opcion == "8":
        Borrar_base()
    elif opcion == "0":
        exit()
    else:
        print("opcion incorrecta")
















































