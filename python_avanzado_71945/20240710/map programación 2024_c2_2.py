



import os
from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione enter para continuar")
limpiar();


def ya_hechos():
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
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
    init()
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                                                                             ║
    ║    Modulos IT -  Programacion                                               ║
    ║        Constantes y variables, tipos de datos.                              ║
    ║        Operadores lógicos y matemáticos.                                    ║
    ║        Estructuras de toma de decisiones.                                   ║
    ║        Estructuras de repeticiones.                                         ║
    ║        Procedimientos y funciones.                                          ║
    ║        Listas, tuplas, diccionarios.                                        ║
    ║        Algoritmos y estructuras de datos.                                   ║
    ║        Bases de datos                                                       ║
    ║               Conexión - Cursor                                             ║
    ║                      BBDD                                                   ║
    ║                      Tablas                                                 ║
    ║                      Campos (tipos de datos)                                ║
    ║                      Registros                                              ║
    ║               CRUD - ABM                                                    ║
    ║                                                                             ║
    ╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}{Fore.BLACK+Back.CYAN}
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                                                                             ║
    ║    Road map de clases con Ariel                                             ║
    ║        Programación Modulo 1 - presentación e instalacion                   ║
    ║        Programación Modulo 2 - t obj_1ros operadores                        ║
    ║        Programación Modulo 3 - m flujo - if                                 ║
    ║        Programación Modulo 4 - entradas de datos                            ║
    ║        Programación Modulo 5 - m flujo - while                              ║
    ║        Programación Modulo 6 - colecciones - m flujo - for                  ║
    ║                                           ingresar                          ║
    ║                                           eliminar                          ║
    ║                                           modificar                         ║
    ║        Programación Modulo 7 - random - ternarios - comprension             ║
    ║        Programación Modulo 8 - funciones propias                            ║
    ║                                          parametro    | entrada - salida    ║
    ║                                          argumento                          ║
    ║                                          recursividad                       ║
    ║                                                                             ║
    ║        Programación Modulo 9 - lambda - o_sup                               ║
    ║                                        map(funcion_accion simple, coleccion)║
    ║                                        filter(funcion_booleana, coleccion)  ║
    ║                                        reduce(funcion-2 parametros entrada  ║
    ║                                                       1 parametro de salida)║
    ║                                                                             ║
    ║        Programación Modulo 10 - externos with open(nombre archivo, mode     ║
    ║                                                rb             r read        ║
    ║                                                wb             w write       ║
    ║                                                ab             a append      ║
    ║                                                xb?            x crea vacio  ║
    ║                                          binario pickle     json            ║
    ║                                                                             ║
    ║        Programación Modulo 11 - try except basico                           ║
    ║        Programación Modulo 12 - BBDD                                        ║
    ║        Programación Modulo 13 - GUI                                         ║
    ║        Programación Modulo 14 - web                                         ║
    ║                                                                             ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')



dato = 88788
print (dato)
print ("el dato es :" , dato , " kg")
print ("el dato es :%s kg", format( dato))

print ("el dato es :"+str(dato)+" kg")
print ("el dato es :",dato," kg")

print (f"el dato es : {dato} kg")
print ( "el dato es : {dato} kg")
print (f"el dato es : {dato=} kg")
dato = input (f"ingrese un valor para cambiar a {dato} :")
print (f"nuevo valor de dato = {dato} :")
if dato.isdigit():
    dato = int(dato)
elif dato.replace(".","",1).isdigit():
    dato= float(dato)
else:
    dato = "no valido"




lista = [9,5,1,"p","o","i","u",8,8,9,2,0,"y","t",3,5,4,7,8,0,3]#iterabe mutable

for cada_dato in lista:
    print (f"{cada_dato=}")
string = "hola mundo IT"

for cada_caracter in string:
    print (f"{cada_caracter=}")


entero  = 98765443#'int' object is not iterable
string = str(entero)
for cada_numero in string:
    print (f"{cada_numero=}")


print (f"metodos y atribitos de tuplas {dir(tuple())}")
"""
metodos y atribitos de tuplas [ 'count', 'index'] '



"""
print (f"metodos y atribitos de lista {dir(list())}")


"""
metodos y atribitos de lista ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

agregar datos
'append', 'extend', 'insert'

eliminar datos
'clear', 'pop', 'remove'

ordenar datos
 'reverse', 'sort'
 
 informacion de colecciones lista y  tuplas 
 [ 'count', 'index'] 
  
para mas adelante 
  'copy',
 

"""


