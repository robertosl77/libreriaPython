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
║     y de yapa                                                               ║
║                                                                             ║
║  ● zip(iterable 1, iterable 2)                                              ║
║                                                                             ║
║  ● enumerate(iterable)                                                      ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
''');#Funciones incorporadas (map, zip, enumerate, reduce, filter).Funciones incorporadas (map, zip, enumerate, reduce, filter).
pausa();limpiar()#

##################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║         ╔══════╗   ╔══════╗   ╔═════╗   ╦      ╦   ╔════╗   ╔══════╗        ║
║         ║      ╚╗  ║          ║     ╚╗  ║      ║  ╔╝    ╚╗  ║               ║
║         ║       ║  ║          ║      ║  ║      ║  ║         ║               ║
║         ║      ╔╝  ║          ║      ║  ║      ║  ║         ║               ║
║         ╠═══╦══╝   ╠═════╝    ║      ║  ║      ║  ║         ╠═════╝         ║
║         ║   ╚╗     ║          ║      ║  ║      ║  ║         ║               ║
║         ║    ╚╗    ║          ║     ╔╝  ╚╗    ╔╝  ╚╗    ╔╝  ║               ║
║         ╩     ╚╝   ╚══════╝   ╚═════╝    ╚════╝    ╚════╝   ╚══════╝        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
Reduce se encuentra en la libreria 'functools'.
   pip install functools
   https://visualstudio.microsoft.com/es/visual-cpp-build-tools/

La función reduce(fun,lista) se usa para aplicar una función particular pasada en su argumento a todo
los elementos de la lista mencionados en la secuencia pasada.

reduce es muy útil cuando queremos realizar ciertas operaciones sobre una lista y devolver su resultado.
Por ejemplo, si queremos calcular el producto de todos los elementos de una lista, y devolver un único valor,
podríamos hacerlo de la siguiente forma sin usar reduce.
''')
producto = 1
lista = [1, 2, 3, 4]
for num in lista:
    producto = producto * num
# ~ int (f"{producto=}")
# producto = 24

print (f"{producto=}")
#Ahora vamos a hacerlo con reduce.

from functools import reduce





producto = reduce((lambda x, y: x * y), [1, 2, 3, 4])





print (f"{producto=}")
exit()
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print (producto)
#Ej Nro 1/reduce:
'''
Ejemplo
    En el primer paso, se seleccionan los dos primeros elementos de la secuencia y se obtiene el resultado.
    El siguiente paso es aplicar la misma función al resultado obtenido anteriormente y el número que sigue al segundo elemento
        y el resultado se almacena nuevamente.
    Este proceso continúa hasta que no quedan más elementos en el contenedor.
    El resultado final devuelto se devuelve y se imprime en la consola.
'''
print("*"*50,"\nEj Nro 2/reduce")
from functools import reduce
lista_ = [1, 8, 3, 4, 7, 5, 6, 2, 9 ]
print(f"Sumatoria : lambda :{reduce(lambda a, b: a+b, lista_)}")
print(f"Sumatoria : {sum(lista_)}")
# using reduce to compute maximum element from list
print(f"Maximo : lambda :{reduce(lambda a, b: a if a > b else b, lista_)}")
print(f"Maximo : {max(lista_)}")
##################################################################################################
#Ej Nro 2/reduce:
'''
Crear una función que tome una lista de dígitos y devuelva al número al que corresponden.
voy tomando números de a uno, lo multiplico x 10 y sumo el siguiente como unidad, esto vuelvo a multiplicarlo x 10 y sumo el tercer valor..etc
'''
print("*"*50,"\nEj Nro 2/reduce")
from functools import reduce
def digitos_a_numero(digitos):
    return reduce(lambda x,y:x*10 + y,digitos)
lista_ = [1, 8, 3, 4, 7, 5, 6, 2, 9 ]
print (f"{digitos_a_numero(lista_)=}")
print (f"lambda : {reduce(lambda x,y:x*10 + y,lista_)=}")
pausa();limpiar()
##################################################################################################

def sumar(x):
    return x+100
def cuadrado(x):
    return x**2
def superior(funcion,lista):
    resultado =funcion(4)
    # ~ for n in lista:
        # ~ resultado.append(funcion(n))
    return resultado
numeros = [2,5,10]
print(superior(sumar,numeros))
out: [102, 105, 110]
print(superior(cuadrado,numeros))
out: [4, 25, 100]
from statistics import mean
mean([1, 2, 3, 4, 4])

print(mean([-1.0, 2.5, 3.25, 5.75]))


# ~ from fractions import Fraction as F
# ~ mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
# ~ Fraction(13, 21)

# ~ from decimal import Decimal as D
# ~ mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
def esPositivo(n):
    return n > 0
def positivosConFilter(numeros):
    return filter(esPositivo, numeros)
for x in (positivosConFilter([2, -1, 4, 0, -10, -2, 6, -8])):
    print ('positivosConFilter:',x)
pausa();limpiar()
##################################################################################################
from functools import reduce
print( 'reduce(lambda x, y: x + y, [1,2,3,4,5]):',reduce(lambda x, y: x + y, [1,2,3,4,5]) )



