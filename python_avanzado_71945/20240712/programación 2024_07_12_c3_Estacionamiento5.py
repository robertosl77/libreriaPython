



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
  'copy'
"""


# ~ #---------------------------------------------------------------------
# ~ dic_patentes_h  = {"QWE123": 8 ,"ASD123": 9 ,"ZXC123":10 ,"123QAZ":12}
# ~ dic_patentes_tv = { "QWE123":"A",
                # ~ "ASD123":"C",
                # ~ "ZXC123":"V",
                # ~ "123QAZ":"M"}


# ~ print (f"{dic_patentes_h=}")
# ~ print (f"{dic_patentes_tv=}")

# ~ print (f"['QWE123']{dic_patentes_h['QWE123']=}")
# ~ print (f"['QWE123']{dic_patentes_tv['QWE123']=}")
import random
medios_de_pagos=["TC","TD","QR","ML","MP","EFECTIVO","TRANF"]
dic_patentes ={ "QWE123": {
                            "hora de entrada":8,
                            "tipo de vehiculo":"A",
                            "hora de salida":99,
                            "cliente":"NO",
                            "Telefono":"",
                            "direccion":"",
                            "total estacionado":0,
                            "total $":"",
                            "medio de pago":"",
                            "cod.operacion":""
                            },
                "ASD123":  {
                            "hora de entrada":9,
                            "tipo de vehiculo":"C" ,
                            "hora de salida":99,
                            "cliente":"NO",
                            "Telefono":"",
                            "direccion":"",
                            "total estacionado":0,
                            "total $":"",
                            "medio de pago":"",
                            "cod.operacion":""
                            },
                "ZXC123": {
                            "hora de entrada":10,
                            "tipo de vehiculo":"V" ,
                            "hora de salida":99,
                            "cliente":"NO",
                            "Telefono":"",
                            "direccion":"",
                            "total estacionado":0,
                            "total $":"",
                            "medio de pago":"",
                            "cod.operacion":""
                            },
                "123QAZ": {
                            "hora de entrada":12,
                            "tipo de vehiculo":"M" ,
                            "hora de salida":99,
                            "cliente":"NO",
                            "Telefono":"",
                            "direccion":"",
                            "total estacionado":0,
                            "total $":"",
                            "medio de pago":"",
                            "cod.operacion":""
                            }
                }


# ~ print (f"['QWE123']{dic_patentes['QWE123']=}")
# ~ print (f"['QWE123']{dic_patentes['QWE123']['hora de entrada']=}")
# ~ print (f"['QWE123']{dic_patentes['QWE123']['tipo de vehiculo']=}")



#---------------------------------------------------------------------
caja=[]#una lista donde guardo el total de los tickets
#---------------------------------------------------------------------

#                      tipo de vehiculo aceptado por el estacionamiento 
#                     /
precios_por_horas= {"A":2000,
                    "M":1000,
                    "C":4000,
                    "V":3000
                    }#    \
#                          \precio de hora segun tipo vehiculo

#---------------------------------------------------------------------
def funcion_entrada(patente_actual,hora_actual,dic_patentes):
    """
    docstings
    entradas   
              - parametros           argumentos
                    patente_actual - str
                    hora_actual    - datetime
                    dic_patentes       - listas anidadas con datos de movimiento
    salidas
              - parametros           argumentos
                    patente_actual - str
                    hora_actual    - datetime
                    dic_patentes       - listas anidadas con datos de movimiento
    funcionamiento
    """
    print ("Deje las llaves, nosotros se lo estacionamos")
    tipo_de_vehiculo = ""
    while not (tipo_de_vehiculo in  precios_por_horas.keys()):
        tipo_de_vehiculo = input (f"ingrese el tipo de vehiculo {precios_por_horas.keys()}:").upper()

    
    dic_patentes[patente_actual]= {
                                    "hora de entrada":hora_actual,
                                    "tipo de vehiculo":tipo_de_vehiculo,
                                    "hora de salida":99,
                                    "cliente":"NO",
                                    "Telefono":"",
                                    "direccion":"",
                                    "total estacionado":0,
                                    "total $":"",
                                    "medio de pago":"",
                                    "cod.operacion":""
                                    }
    
    
    
    print (f"{dic_patentes[patente_actual]=}")
    
    pausa()
    return dic_patentes               
                    
#---------------------------------------------------------------------
def funcion_salida(patente_actual,hora_actual,dic_patentes,caja):
    print ("Su vehiculo esta guardada, ya se lo traemos")

    hora_entrada       = dic_patentes[patente_actual]['hora de entrada']
    tipo_de_vehiculo   = dic_patentes[patente_actual]['tipo de vehiculo']
    precio_por_hora = precios_por_horas[ dic_patentes[patente_actual]['tipo de vehiculo']]

    tiempo_estacionado = hora_actual-hora_entrada
    total = precio_por_hora * tiempo_estacionado
    print (f"""
                      ticket
    su vehiculo {patente_actual}
        ingreso a las       {hora_entrada} hs.
        sale a las          {hora_actual} hs.
        tiempo estacionado  {tiempo_estacionado} hs.
        -----------------------------------------------
        precio por hora   $ {precio_por_hora}
        total             $ {total}        
    """)
    if dic_patentes[patente_actual]['cliente']=="Mensual":
        pass
    elif dic_patentes[patente_actual]['cliente']=="Nocturno":
        pass
    elif dic_patentes[patente_actual]['cliente']=="Empresa":
        pass
    dic_patentes[patente_actual]['hora de salida']= hora_actual
    dic_patentes[patente_actual]["total estacionado"]=tiempo_estacionado
    dic_patentes[patente_actual]["total $"]=total
    dic_patentes[patente_actual]["medio de pago"]=random.choice(medios_de_pagos)
    dic_patentes[patente_actual]["cod.operacion"]=f"op:{random.randint(9999,999999)}"
    print (f"{dic_patentes[patente_actual]=}")
    caja.append(total)
    pausa()
    return  dic_patentes,caja
  #---------------------------------------------------------------------
def funcion_estado(dic_patentes):
    limpiar()
    print ("*"*100)
    print ("*","estacionamiento 'es un rayoncito' (diccionario)".center(96),"*")
    print ("*"*100)
    for patente_actual in dic_patentes:
        if dic_patentes[patente_actual]['hora de salida'] ==99:
            print (f"patente {patente_actual}) - hora de entrada {dic_patentes[patente_actual]['hora de entrada']} tipo de vehiculo {dic_patentes[patente_actual]['tipo de vehiculo']}")
    #---------------------------------------------------------------
    return

# ~ help(funcion_entrada)

while True:
    funcion_estado(dic_patentes)
    patente_actual=""
    while not (patente_actual.isalnum() and 5<len(patente_actual)<7) and  patente_actual!="SALIR":
        patente_actual = input("ingrese su patente:").upper()
    if patente_actual=="SALIR":
        break
    hora_actual=""
    #while not (hora_actual.isdigit() and int(hora_actual)>=0 and int(hora_actual)<24 ):
    while not (hora_actual.isdigit() and 0<=int(hora_actual)<24) :
        hora_actual = input("ingrese la hora actual como entero:")
    hora_actual = int(hora_actual)
    
    # ~ patente_actual = patente_actual.upper()
    if patente_actual in dic_patentes.keys():
       dic_patentes,caja =  funcion_salida(patente_actual,hora_actual,dic_patentes,caja)
    else:#no esta en  dic_patentes.keys()
        dic_patentes =funcion_entrada(patente_actual,hora_actual,dic_patentes)

print("*"*100)
if len(caja)==0:
    print ("te estas fundiendo.")
else:
    print (f"""
    su caja se compone de {caja}
    el total es de        $ {sum(caja)}
    cantidad de tickets     {len(caja)}
    el mejor cliente     $  {max(caja)}
    el peor cliente      $  {min(caja)}
    la media de su turno $  {sum(caja)/len(caja)}
    """)
print ("Adios")


