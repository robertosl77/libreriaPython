
import os
from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione una tecla para continuar")
def ya_hechos():
    pass
    limpiar();
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                                                                             ║
    ║              ╦     ╔═════╗     ╔═══╦═══╗   ╔═══════╗     ╔═════╗            ║
    ║              ║    ╔╝     ╚╗        ║       ║            ╔╝     ╚╗           ║
    ║              ║    ║                ║       ║            ║       ║           ║
    ║              ║    ╚╗               ║       ║            ║       ║           ║
    ║              ║     ╚═════╗         ║       ╠══════╣     ╠═══════╣           ║
    ║              ║           ╚╗        ║       ║            ║       ║           ║
    ║              ║    ╚╗     ╔╝        ║       ║            ║       ║           ║
    ║              ╩     ╚═════╝         ╩       ╚═══════╝    ╩       ╩           ║
    ║                                                                             ║
    ║                                                                             ║
    ╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
    ║                                                                             ║
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
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                                                                             ║
    ║    ╔╗        ╔╗    ╦    ╔╗      ╦   ╔══════╗   ╔══════╗    ╦    ╔═════╗     ║
    ║    ║╚╗      ╔╝║    ║    ║╚╗     ║   ║          ║      ╚╗   ║   ╔╝     ╚╗    ║
    ║    ║ ╚╗    ╔╝ ║    ║    ║ ╚╗    ║   ║          ║       ║   ║   ║       ║    ║
    ║    ║  ╚╗  ╔╝  ║    ║    ║  ╚╗   ║   ║          ║      ╔╝   ║   ║       ║    ║
    ║    ║   ╚╗╔╝   ║    ║    ║   ╚╗  ║   ╠═════╣    ╠═══╦══╝    ║   ╠═══════╣    ║
    ║    ║    ╚╝    ║    ║    ║    ╚╗ ║   ║          ║   ╚╗      ║   ║       ║    ║
    ║    ║          ║    ║    ║     ╚╗║   ║          ║    ╚╗     ║   ║       ║    ║
    ║    ╩          ╩    ╩    ╩      ╚╝   ╚══════╝   ╩     ╚╝    ╩   ╩       ╩    ║
    ║                                                                             ║
    ║                                                                             ║
    ║  ╔═════╗   ╔══════╗      ╔═════╗    ╔════╗  ╔═══╦═══╗   ╔════╗     ╔════╗   ║
    ║  ║     ╚╗  ║             ║     ╚╗  ╔╝    ╚╗     ║      ╔╝    ╚╗   ╔╝    ╚╗  ║
    ║  ║      ║  ║             ║      ║  ║      ║     ║      ║      ║   ║         ║
    ║  ║      ║  ║             ║      ║  ║      ║     ║      ║      ║   ╚╗        ║
    ║  ║      ║  ╠═════╣       ║      ║  ╠══════╣     ║      ║      ║    ╚════╗   ║
    ║  ║      ║  ║             ║      ║  ║      ║     ║      ║      ║         ╚╗  ║
    ║  ║     ╔╝  ║             ║     ╔╝  ║      ║     ║      ╚╗    ╔╝   ╚╗    ╔╝  ║
    ║  ╚═════╝   ╚══════╝      ╚═════╝   ╩      ╩     ╩       ╚════╝     ╚════╝   ║
    ║                                                                             ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝
    ''')

    pausa()
    limpiar();
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║   ╔══════╗     ╔═══════╗    ╔══════╗     ╔═════╗     ╔═════╗     ╔═════╗    ║
    ║   ║      ╚╗    ║            ║      ╚╗   ╔╝     ╚╗   ╔╝     ╚╗   ╔╝     ╚╗   ║
    ║   ║       ║    ║            ║       ║   ║       ║   ║           ║       ║   ║
    ║   ║      ╔╝    ║            ║      ╔╝   ║       ║   ╚╗          ║       ║   ║
    ║   ╠══╦═══╝     ╠═════╣      ╠══════╝    ╠═══════╣    ╚═════╗    ║       ║   ║
    ║   ║  ╚═╗       ║            ║           ║       ║          ╚╗   ║       ║   ║
    ║   ║    ╚═╗     ║            ║           ║       ║   ╚╗     ╔╝   ╚╗     ╔╝   ║
    ║   ╩      ╚═    ╚═══════╝    ╩           ╩       ╩    ╚═════╝     ╚═════╝    ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')


    pausa()
limpiar()
#----------------------------------------------------------------------
objeto = 8
print (f"el valor de {objeto=}  tipo {type(objeto)}   id {id(objeto)} ")

objeto = objeto + 555
print (f"el valor de {objeto=}  tipo {type(objeto)}   id {id(objeto)} ")
#----------------------------------------------------------------------
objeto = "Ariel"
print (f"el valor de {objeto=}  tipo {type(objeto)}   id {id(objeto)} ")

objeto = objeto + " Garcia"
print (f"el valor de {objeto=}  tipo {type(objeto)}   id {id(objeto)} ")
#----------------------------------------------------------------------

PI = 3.14159
print (f"el valor de {PI=}  tipo {type(PI)}   id {id(PI)} ")

#----------------------------------------------------------------------

tupla = (12345,1415,987654)
print (f"el valor de {tupla=}  tipo {type(tupla)}   id {id(tupla)}  dir dir(tupla)")

#----------------------------------------------------------------------

lista = [12345,1415,987654]
print (f"el valor de {lista=}  tipo {type(lista)}   id {id(lista)}  dir dir(lista)")
lista.append(5678912345)
print (f"el valor de {lista=}  tipo {type(lista)}   id {id(lista)}  dir dir(lista)")

#----------------------------------------------------------------------
"""
FIFO - First In -> First Out 
LIFO - Last  In -> First Out 
garantias, vencimiento, 
"""
"""

1 x 100       1 producto comprado
1 x 600       1 producto vendo
----------------------------------
    500 ganancia    3.5 IB
                   21% iva
                   33 ganancias
"""


lista= list()
lista = ["DATO_1","DATO_2","DATO_3","DATO_4","DATO_5","DATO_6","DATO_7","DATO_8"]

lista.append("DATO_9")#     ENTRADA SIEMPRE AL ULTIMO
#------------------------------------------------------
dato_salida = lista.pop(0)# SALIDA SIEMPRE EL PRIMERO FIFO
print (f"FIFO {dato_salida=}")
dato_salida = lista.pop()#  SALIDA SIEMPRE EL ULTIMO LIFO
print (f"LIFO {dato_salida=}")
#----------------------------------------------------------------------
"""
DICT clave - valor
"""

dic={"clave1":"valor 1",
     "clave2":2,
     "clave3":3.14159,
     "clave4":[2,34,6,8,10,12,14,16,18,20],
     "clave5":{"SUB_CLAVE1":2,
             "SUB_CLAVE1":34,
             "SUB_CLAVE2":6,
             "SUB_CLAVE3":8,
             "SUB_CLAVE4":10,
             "SUB_CLAVE5":12,
             "SUB_CLAVE6":14,
             "SUB_CLAVE7":16,
             "SUB_CLAVE8":18,
             "SUB_CLAVE9":20},
     "clave6":(2,34,6,8,10,12,14,16,18,20),
        }          
"""
print (f"{dic['clave1']=}")
print (f"{dic['clave2']=}")
print (f"{dic['clave3']=}")
print (f"{dic['clave4']=}")
print (f"{dic['clave4'][0]=}")
print (f"{dic['clave4'][1]=}")
print (f"{dic['clave4'][2]=}")
print (f"{dic['clave4'][3]=}")
print (f"{dic['clave4'][4]=}")
print (f"{dic['clave4'][5]=}")
print (f"{dic['clave5']['SUB_CLAVE1']=}")
print (f"{dic['clave5']['SUB_CLAVE2']=}")
print (f"{dic['clave5']['SUB_CLAVE3']=}")
print (f"{dic['clave5']['SUB_CLAVE7']=}")
print (f"{dic['clave5']['SUB_CLAVE8']=}")
print (f"{dic['clave5']['SUB_CLAVE9']=}")
dic['clave2']=888888
dic['clave4'][2]="Pepe"
dic['clave5']['SUB_CLAVE8']="3.14159"

for clave, valor in dic.items():
    print(f"la clave {clave} tiene asociado el valor {valor} {type(valor)}")
    if isinstance(valor,(list,tuple)):
        for index, sub_valor in enumerate(valor):
            print (f"\t\t\t{index =}     {sub_valor=}")
         
    if isinstance(valor, dict):
        for sub_clave, sub_valor in valor.items():
            print (f"\t\t\t{sub_clave =}     {sub_valor=}")

""" 
#----------------------------------------------------------------------
print ("*"*50)
"""
COPY ALIAS 
"""
#dic_stock = dic["clave4"].copy()#no tengo alias
dic_stock = dic["clave4"]#es un alias de una parte del original


print (f"{dic_stock=}")
for index, sub_valor in enumerate(dic_stock):
    print (f"\t\t\t{index =}     {sub_valor=}")

dic_stock[4]= "cambioooooooooooooo"
print (f"{dic_stock=}")
for index, sub_valor in enumerate(dic_stock):
    print (f"\t\t\t{index =}     {sub_valor=}")

#----------------------------------------------------------------------
for clave, valor in dic.items():
    print(f"la clave {clave} tiene asociado el valor {valor} {type(valor)}")
    if isinstance(valor,(list,tuple)):
        for index, sub_valor in enumerate(valor):
            print (f"\t\t\t{index =}     {sub_valor=}")
         
    if isinstance(valor, dict):
        for sub_clave, sub_valor in valor.items():
            print (f"\t\t\t{sub_clave =}     {sub_valor=}")

print ("*"*50)
#----------------------------------------------------------------------
"""
PSEUDOMATRICES Anidados
"""
#----------------------------------------------------------------------
"""
import numpy as np
"""
#----------------------------------------------------------------------
"""
AS - como
"""

























