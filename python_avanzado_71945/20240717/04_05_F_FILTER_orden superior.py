#######################################################################################################
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tEnter para continuar")
    limpiar()
from colorama import *
#######################################################################################################
limpiar()
from datetime import datetime, date, time
# ~ nuevo(0,estado='inicio',modulo=4)
import math
import datetime
#######################################################################################################
from datetime import datetime, date, time

#######################################################################################################
def Ej_ya_hechos():
    #Con tab colocaremos aquí las practicas hechas
    pass
limpiar()
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║                                                                             ║
║ ╔══════╗ ╦      ╦ ╔╗      ╦  ╔════╗  ╦  ╔════╗  ╔╗      ╦ ╔══════╗  ╔════╗  ║
║ ║        ║      ║ ║╚╗     ║ ╔╝    ╚╗ ║ ╔╝    ╚╗ ║╚╗     ║ ║        ╔╝    ╚╗ ║
║ ║        ║      ║ ║ ╚╗    ║ ║        ║ ║      ║ ║ ╚╗    ║ ║        ║        ║
║ ║        ║      ║ ║  ╚╗   ║ ║        ║ ║      ║ ║  ╚╗   ║ ║        ╚╗       ║
║ ╠════╗   ║      ║ ║   ╚╗  ║ ║        ║ ║      ║ ║   ╚╗  ║ ╠═════╝   ╚════╗  ║
║ ║        ║      ║ ║    ╚╗ ║ ║        ║ ║      ║ ║    ╚╗ ║ ║              ╚╗ ║
║ ║        ╚╗    ╔╝ ║     ╚╗║ ╚╗    ╔╝ ║ ╚╗    ╔╝ ║     ╚╗║ ║        ╚╗    ╔╝ ║
║ ╩         ╚════╝  ╩      ╚╝  ╚════╝  ╩  ╚════╝  ╩      ╚╝ ╚══════╝  ╚════╝  ║
║                                                                             ║
║                                                                             ║
║                              ╔══════╗   ╔═══════╗                           ║
║                              ║      ╚╗  ║                                   ║
║                              ║       ║  ║                                   ║
║                              ║       ║  ║                                   ║
║                              ║       ║  ╠══════╝                            ║
║                              ║       ║  ║                                   ║
║                              ║      ╔╝  ║                                   ║
║                              ╚══════╝   ╚═══════╝                           ║
║                                                                             ║
║                                                                             ║
║           ╔═════╗    ╔══════╗    ╔══════╗   ╔═══════╗   ╔╗      ╦           ║
║          ╔╝     ╚╗   ║      ╚╗   ║      ╚╗  ║           ║╚╗     ║           ║
║          ║       ║   ║       ║   ║       ║  ║           ║ ╚╗    ║           ║
║          ║       ║   ║      ╔╝   ║       ║  ║           ║  ╚╗   ║           ║
║          ║       ║   ╠═══╦══╝    ║       ║  ╠══════╝    ║   ╚╗  ║           ║
║          ║       ║   ║   ╚╗      ║       ║  ║           ║    ╚╗ ║           ║
║          ╚╗     ╔╝   ║    ╚╗     ║      ╔╝  ║           ║     ╚╗║           ║
║           ╚═════╝    ╩     ╚╝    ╚══════╝   ╚═══════╝   ╩      ╚╝           ║
║                                                                             ║
║                                                                             ║
║    ╔═════╗  ╦       ╦ ╔══════╗  ╔═══════╗ ╔══════╗  ╦  ╔═════╗  ╔══════╗    ║
║   ╔╝     ╚╗ ║       ║ ║      ╚╗ ║         ║      ╚╗ ║ ╔╝     ╚╗ ║      ╚╗   ║
║   ║         ║       ║ ║       ║ ║         ║       ║ ║ ║       ║ ║       ║   ║
║   ╚╗        ║       ║ ║      ╔╝ ║         ║      ╔╝ ║ ║       ║ ║      ╔╝   ║
║    ╚═════╗  ║       ║ ╠══════╝  ╠══════╝  ╠═══╦══╝  ║ ║       ║ ╠═══╦══╝    ║
║          ╚╗ ║       ║ ║         ║         ║   ╚╗    ║ ║       ║ ║   ╚╗      ║
║   ╚╗     ╔╝ ╚╗     ╔╝ ║         ║         ║    ╚╗   ║ ╚╗     ╔╝ ║    ╚╗     ║
║    ╚═════╝   ╚═════╝  ╩         ╚═══════╝ ╩     ╚╝  ╩  ╚═════╝  ╩     ╚╝    ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
║                                                                             ║
║                                                                             ║
║    lambda denera una funcion anónima                                        ║
║                                                                             ║
║  ● lambda argumentos: expresión                                             ║
║      Son funciones que pueden definir cualquier número de parámetros pero   ║
║      una única expresión. Esta expresión es evaluada y devuelta.            ║
║      Se pueden usar en cualquier lugar en el que una función sea requerida  ║
║      Estas funciones están restringidas al uso de una sola expresión.       ║
║      Se suelen usar en combinación con otras funciones, generalmente como   ║
║      argumentos de otra función.                                            ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                                                             ║
║     map, filter y reduce necesitan una funcion como primer argumento.       ║
║                                                                             ║
║                                                                             ║
║  ● map(funcion, iterable(s))                                                ║
║      aplica una función a cada uno de los elementos de una lista.           ║
║                                                                             ║
║  ● filter(funcion, iterable(s))                                             ║
║      Filtra una lista de elementos para los que una función devuelve True   ║
║                                                                             ║
║  ● reduce(funcion, iterable[, initial]) del módulo functools.               ║
║      Esta función se utiliza principalmente para llevar a cabo un cálculo   ║
║      acumulativo sobre una lista de valores  y devolver el resultado.       ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                                                             ║
║     y de yapa                                                               ║
║                                                                             ║
║                                                                             ║
║  ● zip(iterable 1, iterable 2)                                              ║
║                                                                             ║
║                                                                             ║
║  ● enumerate(iterable)                                                      ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
''');#Funciones incorporadas (map, zip, enumerate, reduce, filter).Funciones incorporadas (map, zip, enumerate, reduce, filter).

# ~ print ("-"*50)
# ~ pausa()
# ~ limpiar()

# ~ def suma(a,b):
    # ~ '''ingreso 2 parametros numericos'''
    # ~ return(a+b)

# ~ def resta(a,b):
    # ~ return(a-b)
# ~ def funcion(llamada):
    # ~ a=4
    # ~ b=3
    #print(f"{llamada__doc__=}")
    # ~ print(f"{type(llamada)=}")
    # ~ ret= llamada(a,b)
    # ~ print(f"{ret=}")
# ~ opcion = input("Ingrese + o -:")
# ~ if opcion=='+':
    # ~ funcion(suma)
# ~ elif opcion=='-':
    # ~ funcion(resta)
# ~ else:
    # ~ print("Error")



import this




#######################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║        ╔══════╗  ╦    ╦         ╔════╦════╗   ╔═══════╗    ╔══════╗         ║
║        ║         ║    ║              ║        ║            ║      ╚╗        ║
║        ║         ║    ║              ║        ║            ║       ║        ║
║        ║         ║    ║              ║        ║            ║      ╔╝        ║
║        ╠════╗    ║    ║              ║        ╠══════╣     ╠════╦═╝         ║
║        ║         ║    ║              ║        ║            ║    ╚╗          ║
║        ║         ║    ║              ║        ║            ║     ╚╗         ║
║        ╩         ╩    ╚═══════╝      ╩        ╚═══════╝    ╩      ╚╝        ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

El operado filter (función f, lista) ofrece una forma elegante de filtrar todos los elementos de una lista,
    para los que la función f devuelve True.
El operador filter(f, l) necesita una función f como primer argumento y una coleccion como segundo.
Retorna una coleccion class filter iterables con los elementos que satisfacen la funcion/metodo condicional llamado.
Esta función se aplicará a cada elemento de la coleccion.

Dependiendo del contexto (y teniendo como objetivos colecciones) se puede usar la función map() o la función filter()
    en lugar de las listas por comprensión,

Como su nombre indica, filter crea una lista de elementos si usados en la llamada a una función devuelven True.
Es decir, filtra los elementos de una lista usando un determinado criterio. Veamos un ejemplo:
''')
lista = range(-5, 6)
lista =[-5,-4,-3,-2,-1,0,1,2,3,4,5]


def filtro_menor_a_0(numero):
    if numero < 0:
        return True
    """
    else:
        return False
    """
    #return  None implicito

menor_cero=[]
for dato in lista:
    rec= filtro_menor_a_0(dato)#deberia ser booledoa
    if rec is True :
        menor_cero.append(dato)
print (f"{menor_cero}")
#--------------------------------------
menor_cero = filter(filtro_menor_a_0 , lista)

print (f"filter {menor_cero}")
print (f"list filter {list(menor_cero)}")
#--------------------------------------


menor_cero = filter(lambda numero: True if numero < 0 else False , lista)
print (f"filter {menor_cero}")
print (f"list filter {list(menor_cero)}")
pausa()

print(f"objeto = {menor_cero=}\n{type(menor_cero)}\n{dir(menor_cero)}")
# retorna un objeto de la clase filter

for dato in menor_cero:
    print (F"{dato=}")

#      o
menor_cero = list(filter(filtro_menor_a_0 , lista))# casting convertir objetos filter- list
print(f"objeto = {menor_cero=}\n{type(menor_cero)}\n{dir(menor_cero)}")

#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print('''
Se puede utilizar una función anónima lambda:''')
def filtro_menor_a_0(numero):
    if numero < 0:
        return True
    '''
    else:
        return False# None
    '''
lista =[-5,-4,-3,-2,-1,0,1,2,3,4,5]

menor_cero=[]
for numero in lista:
    if filtro_menor_a_0(numero) is True:
        menor_cero.append(numero)

#------------------------------------------------------------------------------------------------------

menor_cero = list(filter((lambda x:True if x < 0 else False), lista))
#           o
menor_cero = list(filter((lambda x: x < 0 ), lista))
print(f"{menor_cero=}")
# Salida: [-5, -4, -3, -2, -1]
print ("-"*50)
pausa()
limpiar()
#######################################################################################################

print('''
La función filter es similar a un bucle, y de hecho podríamos conseguir lo mismo con un bucle y un if, pero su uso es más rápido.
''')
# Primero declaramos una función condicional
def filtro_multiplo_5(numero):
# Comprobamos si un numero es múltiple de cinco
    if numero % 5 == 0:
        # Sólo devolvemos True si lo es
        return True
lista = [2, 5, 10, 23, 50, 33]
filtrados=[]
for numero in lista:
    if filtro_multiplo_5(numero) is True:
        filtrados.append(numero)

filtrados = filter(filtro_multiplo_5, lista)

for cada_multiplo in filtrados:
    print(f"{cada_multiplo=}")
#------------------------------------------------------------------------------------------------------

filtrados = list(filter((filtro_multiplo_5), lista))
print(f"{filtrados=}")
filtrados = list(filter((lambda numero :  True if numero % 5 ==0 else False), lista))
print(f"{filtrados=}")
filtrados = list(filter((lambda numero :  numero % 5 ==0), lista))
print(f"{filtrados=}")
for cada_multiplo in filtrados:
    print(f"{cada_multiplo=}")

print('''
El verdadero potencial de la función filter() sale a relucir cuando usted necesita filtrar varios objetos de una lista.
''')

#------------------------------------------------------------------------------------------------------
print ("-"*50)
pausa()
limpiar()
#######################################################################################################
lista = [2, 5, 10, 23, 50, 33]


def filtro_mayor_q_10(number):
    if number > 10:
        return True
    return False

print(list(filter(filtro_mayor_q_10, lista)))
print(list(filter(lambda number: True if number > 10 else False, lista)))
print(list(filter(lambda number: number > 10, lista)))
#------------------------------------------------------------------------------------------------------
print ("-"*50)
pausa()
limpiar()

#######################################################################################################

patentes = {'ABC123':{"ingreso":10,"salida": 23},'XYZ987':{"ingreso":12,"salida": ""},'ZZZ999':{"ingreso":14,"salida": ""}}

def fun (cada_patente):
    if not cada_patente in patentes:
        return False
    elif  patentes[cada_patente]['salida'] != "":
        return True
    else:
        return False
lista_resultado_True=[]
for cada_patente in patentes:
    resultado_funcion = fun(cada_patente)
    if resultado_funcion is True:
        lista_resultado_True.append(cada_patente)
#------------------------------------------------------------------------------------------------------

def filtro_patentes(cada_patente):
    if cada_patente in patentes and patentes[cada_patente]['salida'] == "":
        return True
    # ~ else:
        # ~ return False

print(list(filter(filtro_patentes, patentes)))
#------------------------------------------------------------------------------------------------------
print(list(filter(lambda cada_patente: (False if not cada_patente in patentes else False if  patentes[cada_patente]['salida'] != "" else True), patentes)))

print(list(filter(lambda cada_patente: (cada_patente in patentes and patentes[cada_patente]['salida'] == ""), patentes)))
#------------------------------------------------------------------------------------------------------
print ("-"*50)
pausa()
limpiar()

#######################################################################################################
#Ejercicio_Funciones_Ej_012
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Lambda + filter (true / false)                 ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

Operador Filter:

El operado filter (función, lista) ofrece una forma elegante de filtrar todos los elementos de una lista, para los que la función de función devuelve True.
El operador filter(f, l) necesita una función f como primer argumento. f devuelve un valor booleano, es decir, verdadero o falso. Esta función se aplicará a cada elemento de la lista. Solo si f devuelve True, el elemento de la lista se incluirá en la lista de resultados.
''')
#esta funcion necesita una lista de datos y devuelve otra de los datos filtrados true

datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even = list(filter(lambda x: x%2 == 0, datos))
print(even)

#######################################################################################################
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]

def filtro(DatoElLista):
    if DatoElLista % 2 == 0:# es par
        return True
print (filter(filtro,array))
print (list(filter(filtro,array)))
print (list(filter(lambda x: x%2 == 0, datos)))
#------------------------------------------------------------------------------------------------------
#Usando el operador Filter
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
print("array",array)
resultado = list(filter(lambda x: x % 2 == 0, array))
print ("resultado = list(filter(lambda x: x % 2 == 0, array))")
print("x % 2 == 0, :",resultado)
#------------------------------------------------------------------------------------------------------
print ("-"*50)
resultado = list(filter(lambda x: x > 0, array))
print ("resultado = list(filter(lambda x: x > 0, array))")
print("x > 0 :",resultado)
#------------------------------------------------------------------------------------------------------
print ("-"*50)
resultado = list(filter(lambda x: x % 3 != 0, array))
print ("resultado = list(filter(lambda x: x % 3 != 0, array))")
print("x % 3 != 0 :",resultado)
#------------------------------------------------------------------------------------------------------
print ("-"*50)
resultado = list(filter(lambda x: x % 3 <= 5, array)) # list()' convierte el iterable
print ("resultado = list(filter(lambda x: x % 3 <= 5, array))")
print("x % 3 <= 5 :",resultado)
#------------------------------------------------------------------------------------------------------
print ("-"*50)
#------------------------------------------------------------------------------------------------------
print ("-"*50)
pausa()
limpiar()

#######################################################################################################
#Ejercicio_Funciones_Ej_013
# Ejercicio 5.6: Encontrar las palabras de una lista que tienen al menos 5 caracteres de longitud.
print(list( filter(lambda x: x % 2 == 0,[0,1,1,2,3,5,8,13,21,34]) ))
# filter users with marks greater than 80
puntos_total = [
                {"usuario": 'Juan',
                 "puntos": 60
                },
                {"usuario": 'Ana',
                 "puntos": 70
                },
                {"usuario": 'Lu',
                 "puntos": 90
                }
            ]
print(f"list( filter(lambda x: x['puntos'] >= 70, puntos_total) )=")
print(f"{list( filter(lambda x: x['puntos'] >= 70, puntos_total) )}")
#######################################################################################################
