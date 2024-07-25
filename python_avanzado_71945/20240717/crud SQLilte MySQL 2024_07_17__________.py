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
    base_de_datos = input("Seleccione entre:\n\tM) para MySQL\n\tS) para SQLite   :""").upper()
limpiar()
match (base_de_datos):
    case "S":
        
        print(f"""{Fore.WHITE+Back.BLUE}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
        import sqlite3
    case "M":

        ####################################################################################################
        print(f"""{Fore.WHITE+Back.BLUE}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
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

print(f"""{Fore.WHITE+Back.BLUE}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")

pausa()
limpiar()
import datetime
hoy = datetime.date.today()
print(hoy)

######################################################################################################
def conectar_base_de_datos():
    global connection
    if base_de_datos == "S":#   SQLite
        #---------------------------------------------------------------------------------------------
        connection = sqlite3.connect(f'{nombre_DDBB}.db')
        #---------------------------------------------------------------------------------------------
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
        #---------------------------------------------------------------------------------------------
        connection = mysql.connector.connect(host= host_ ,user= usuario , passwd= password_de_msql )
        #---------------------------------------------------------------------------------------------
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
    print(f"""{Fore.WHITE+Back.BLUE}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")

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
    print(f"""{Fore.WHITE+Back.BLUE}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    print ("Conectamos con SQLite")
    ######################################################################################################

    print ("CREATE TABLE")
    print ("CREATE COLUMN")
    cursor = conectar_base_de_datos()#           sqlite // mysql




    nombre_DDBB = "Curso_Python_2024_MyV"
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
                                                        {nombre_columna_4} DATE ) """)

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
    print(f"""{Fore.WHITE+Back.BLUE}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    print ("Conectamos con SQLite")
    cursor = conectar_base_de_datos()#           sqlite // mysql
    print ("RECORD INSERT")
    query = f"""INSERT INTO  {nombre_tabla} 
                                        (descripcion, precio, codigo, vencimiento)
                                  VALUES('Galletitas', 222 , 'Titas','2025-01-01')"""
    print           (query)
    cursor.execute  (query)
    connection.commit()
    pausa()
    limpiar()
    print("""\033[13744m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos un dato por intermedio de comodines         ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
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
    print("""\033[13744m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos varios dato por intermedio de comodines     ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")

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
    cursor.execute(query,   ("Arroz", 25 , "A1", '2025-08-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query,   ("Agua", 20 , "H2O", '2025-09-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query,   ("Tomates", 15 , "T1", '2025-02-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query,   ("Sal", 10, "S1", '2025-10-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query,   ("cacao", 30 , "choco", '2025-11-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query,   ("gelatina", 25 , "hl", '2025-12-15'))
    connection.commit()#     <-------  eliminar
    cursor.execute(query,   ("flan", 20 , "flan", '2025-01-15'))
    connection.commit()#     <-------                               No eliminar
    print(cursor.rowcount, "record inserted.")
    pausa()
    limpiar()
    ######################################################################################################
    print(f"""{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos varios dato por intermedio de listas 1 a 1  ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    print   (f'columnas_SQLite = ',query)
    proy= ( ("Chocolates",  99 , "Choc" , '2025-06-15'),
            ("Fideos"    , 300 , "f1"   , '2025-06-15'),
            ("Arroz"     , 250 , "A1"   , '2025-08-15'),
            ("Agua"      , 200 , "H2O"  , '2025-09-15'),
            ("Tomates"   , 105 , "T1"   , '2025-02-15'),
            ("Sal"       , 100 , "S1"   , '2025-10-15'),
            ("cacao"     , 300 , "choco", '2025-11-15'),
            ("gelatina"  , 205 , "hl"   , '2025-12-15'),
            ("flan"      , 200 , "flan" , '2025-01-15'))
    for datos in proy:
        cursor.execute(query,datos)
    connection.commit()# <-------------------------------------------------destabular
    print(cursor.rowcount, "record inserted.")
    # ~ cursor.execute(query,proy)
    # ~ connection.commit()

    pausa()
    limpiar()
    print(f"""{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos varios dato por intermedio de lista directa ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")

    proy = [
                ("Tomates"  , 15 , "T1" , '2025-07-15'),
                ("Sal"      , 10 , "S1" , '2025-02-15'),
                ("Fideos"   , 30 , "f1" , '2025-01-15'),
                ("Arroz"    , 25 , "A1" , '2025-04-15'),
                ("Agua"     , 20 , "H2O", '2025-07-15'),
                ("Ajies"    , 15 , "T1" , '2025-02-15'),
                ("Pimienta" , 10 , "S1" , '2025-01-15'),
                ("Cafe"     , 30 , "f1" , '2025-04-15'),
                ("Yerba"    , 25 , "A1" , '2025-07-15'),
                ("Te"       , 20 , "H2O", '2025-02-25'),
                ("Pan"      , 15 , "T1" , '2025-01-15'),
                ("Queso"    , 10 , "S1" , '2025-02-15')
            ]
    print             (query,proy)
    cursor.executemany(query,proy)# ~ cursor.execute(query,datos)
    connection.commit()

    print(cursor.rowcount, "record inserted in pool.")
    ###################################################################################################
    pausa()
    limpiar()
    print(f"""{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos manualmente                                 ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")

    while True:
        print("Ingreso de datos a mano ")
        pausa()
        dato_desc=""
        while not (5<=len(dato_desc)<=255):
            dato_desc  = input ("Ingrese la descripcion (+ de 5 caracteres) del producto ('ZZ' para Salir): ").upper()
            if dato_desc=="ZZ":
                break

        dato_precio = ""
        while not dato_precio.replace(".","").isdecimal():
            dato_precio=input("ingrese el precio: ")
        dato_precio=float (dato_precio)


        dato_codigo = ""
        while not (dato_codigo.replace(" ","").isalnum() and len(dato_codigo)<=255):
            dato_codigo=input("ingrese el cod.prod (alnum): ")
        dato_codigo= int (dato_precio)
        #from datatime import date, deltatime
        dato_fecha = datetime.date.today()

        cursor.execute  (query, (dato_desc, dato_precio , dato_codigo, dato_fecha))
        connection.commit()
        print(cursor.rowcount, "record inserted.")

######################################################################################################
def leer_tabla():
    pausa()
    limpiar()
    print(f"""{Fore.WHITE+Back.BLUE}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    cursor = conectar_base_de_datos()#           sqlite // mysql
    query = "SELECT * FROM Mi_Tabla "
    cursor.execute(query)
    #print (cursor,type(cursor), dir (cursor))
    datos_desde_sql = cursor.fetchall()
    for linea in datos_desde_sql:
        print (linea)
    for linea in cursor:
        print (linea)

    pausa()
    limpiar()
    
    query = f"SELECT * FROM Mi_Tabla WHERE {nombre_columna_3} == 'A1'"
    cursor.execute(query)
    #print (cursor,type(cursor), dir (cursor))
    datos_desde_sql = cursor.fetchall()

    print(f"{query=}")
    for linea in datos_desde_sql:
        print ("dato: ",linea)
        
        
        
    
    query = f"SELECT * FROM Mi_Tabla WHERE {nombre_columna_3} LIKE 'A%'"
    cursor.execute(query)
    #print (cursor,type(cursor), dir (cursor))
    datos_desde_sql = cursor.fetchall()
    print(f"{query=}")
    print("A.....")
    for linea in datos_desde_sql:
        print ("dato: ",linea)
        

        
    
    query = f"SELECT {nombre_columna_2} FROM Mi_Tabla WHERE {nombre_columna_1} LIKE '%A'"
    cursor.execute(query)
    #print (cursor,type(cursor), dir (cursor))
    datos_desde_sql = cursor.fetchall()
    print(f"{query=}")
    print(".....A")
    for linea in datos_desde_sql:
        print ("dato: ",linea)
    '''    
    nombre_columna_1 = "descripcion"
    nombre_columna_2 = "precio"
    nombre_columna_3 = "codigo"
    nombre_columna_4 = "vencimiento"

    query = "SELECT * FROM Mi_Tabla WHERE '' "
    -- WHERE vencimiento >= '2024-10-01' AND vencimiento <= '2025-05-01'
    -- WHERE vencimiento >= '2024-10-01' OR  vencimiento <= '2025-05-01'
    -- WHERE NOT (vencimiento >= '2025-01-01' OR  vencimiento <= '2025-01-01')
    -- WHERE codigo IN ('H2O','S1','A1')
    -- WHERE precio BETWEEN 10 AND  100
    -- WHERE precio BETWEEN 10 AND  100
    -- WHERE descripcion like 'A%'
    -- WHERE descripcion like '%r%'-- #                    % cualquier cantidad de caracteres
    -- WHERE descripcion like 'A___z'-- #Arroz             _ un solo caracter
    -- WHERE descripcion REGEXP  '^A'-- #                  REGULAR EXPRESION ^inicio, fin^, | or, [caracteres] entres estos , [a-h] entre a y h
    -- WHERE descripcion IS NULL
    -- WHERE descripcion IS NOT NULL
    
    query ="SELECT * FROM Mi_Tabla "
    query ="SELECT * FROM Mi_Tabla WHERE precio BETWEEN 10 AND  100 and codigo like '%Z' "
    query ="SELECT * FROM Mi_Tabla WHERE codigo IN 'H2O','S1','A1' "
    query ="SELECT * FROM Mi_Tabla WHERE codigo like '%H%' "
    inicio = input ("INgrese las primeras letras del producto a buscar:")
    inicio = inicio +"%"
    '''
    
    inicio = "A%"
    query =(f"SELECT * FROM Mi_Tabla WHERE descripcion like '{inicio}' ")
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
def actualizar_datos():
    limpiar()
    print(f"""{Fore.WHITE+Back.BLUE}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    cursor = conectar_base_de_datos()#           sqlite // mysql

    query = f"UPDATE {nombre_tabla} SET {nombre_columna_3} = 'T_lta' WHERE {nombre_columna_1} = 'Tomates' "
    print (query)
    cursor.execute(query)
    connection.commit()
    print(cursor.rowcount, "record(s) affected")
    pausa()

######################################################################################################
def borrar_datos():
    limpiar()
    print(f"""{Fore.WHITE+Back.BLUE}
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
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    cursor = conectar_base_de_datos()#           sqlite // mysql
    query = f"DELETE FROM {nombre_tabla}  WHERE {nombre_columna_1} = 'Sal'"# and {columna2} = '{dato2}'
    cursor.execute(query )
    print(cursor.rowcount, "record(s) affected")
    query = f"DELETE FROM {nombre_tabla}  WHERE {nombre_columna_1} = "

    if base_de_datos == "S":#   SQLite
        query +=  " ? "
    else:#                      MySQL
        query +=  "%s "
    """
SQLite         ?   "
MySQL          %s  "
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
def borrar_tablas():
    limpiar()
    cursor = conectar_base_de_datos()#           sqlite // mysql

    print(f"""{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                         borramos la tabla de la base                        ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
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

def borrar_base():
    limpiar()
    cursor = conectar_base_de_datos()#           sqlite // mysql
    print(f"""{Fore.WHITE+Back.BLUE}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
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

nombre_DDBB = "Curso_Python_2024_MyV"
nombre_tabla = "Mi_Tabla"

nombre_columna_1 = "descripcion"
nombre_columna_2 = "precio"
nombre_columna_3 = "codigo"
nombre_columna_4 = "vencimiento"



while opcion !="0":
    limpiar()
    print(f"""{Fore.WHITE+Back.GREEN}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")

# ~ print(cursor.rowcount, "record inserted in pool.")
    print ("""
    1) Create - Crear base
    2) Create - Crear tablas
    3) Insert - Insertar datos
    4) Read   - Leer datos
    5) Update - Actualizar datos
    6) Delete - Borrar datos
    7) Delete - Borrar tablas
    8) Delete - Borrar BBDD
    0) Salir del programa""")
    opcion=input("Ingrese la opción seleccionada :").upper()
    match(opcion):
        case "1":
            crear_base()
        case"2":
            crear_tablas()
        case"3":
            insertar_datos()
        case"4":
            leer_tabla()
        case"5":
            actualizar_datos()
        case"6":
            borrar_datos()
        case"7":
            borrar_tablas()
        case"8":
            borrar_base()
        case "0":
            exit()
        case other: # case _:
            print("opcion incorrecta")
