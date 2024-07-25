



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




patentes = [  #   0        1         2      3   
             ["QWE123","ASD123","ZXC123","123QAZ"],#   0
             [    8   ,   9    ,   10   ,    12  ],#   1
             [   "A"  ,  "C"   ,   "V"  ,    "M" ]#    2
            ]




caja=[]
patentes_stock          = patentes[0]
patentes_horas_entradas = patentes[1]
patentes_tipo_vehiculo  = patentes[2]


precios_por_horas = [
                      [ "A", "M", "C", "V"],#   0
                      [2000,1500,4000,3000] #   1
                    ]#  0     1    2    3

#---------------------------------------------------------------------
def funcion_entrada(patente_actual,hora_actual,patentes_stock,patentes_tipo_vehiculo,patentes_horas_entradas):
    print ("Deje las llaves, nosotros se lo estacionamos")
    tipo_de_vehiculo = ""
    while not (tipo_de_vehiculo in  precios_por_horas[0] ):
        tipo_de_vehiculo = input (f"ingrese el tipo de vehiculo {precios_por_horas[0]}:").upper()

    patentes_stock.append(patente_actual)
    patentes_horas_entradas.append(hora_actual)
    patentes_tipo_vehiculo.append(tipo_de_vehiculo)
    pausa()
    return patentes_stock,patentes_tipo_vehiculo,patentes_horas_entradas                
                    
#---------------------------------------------------------------------
def funcion_salida(patente_actual,hora_actual,patentes_stock,patentes_tipo_vehiculo,patentes_horas_entradas,caja):
    print ("Su vehiculo esta guardada, ya se lo traemos")
    indice_patente_buscada = patentes_stock.index(patente_actual)
    patentes_stock.pop(indice_patente_buscada)
    hora_entrada       = patentes_horas_entradas.pop(indice_patente_buscada)
    tipo_de_vehiculo   = patentes_tipo_vehiculo.pop(indice_patente_buscada)
    
    indice_precios_por_horas = precios_por_horas[0].index(tipo_de_vehiculo)
    precio_por_hora = precios_por_horas[1][indice_precios_por_horas]
    
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
    caja.append(total)
    pausa()
    
    return  patentes_stock,patentes_tipo_vehiculo,patentes_horas_entradas,caja                  
  #---------------------------------------------------------------------
def funcion_estado(patentes):
    limpiar()
    print ("*"*100)
    print ("*","estacionamiento 'es un rayoncito'".center(96),"*")
    print ("*"*100)
    # ~ for cada_patente in patentes_stock:
        # ~ print (f"{cada_patente}")
    rango = range(0,len(patentes[0]),1)
    for index in rango:
        print (f"patente {index}) -{patentes[0][index]}  hora de entrada {patentes[1][index]} tipo de vehiculo {patentes[2][index]}")
    #---------------------------------------------------------------
    return                     
                    
                    
                    
                    
while True:
    funcion_estado(patentes)
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
    if patente_actual in patentes_stock:
       patentes_stock,patentes_tipo_vehiculo,patentes_horas_entradas,caja =  funcion_salida(patente_actual,hora_actual,patentes_stock,patentes_tipo_vehiculo,patentes_horas_entradas,caja)
    else:
        patentes_stock,patentes_tipo_vehiculo,patentes_horas_entradas =funcion_entrada(patente_actual,hora_actual,patentes_stock,patentes_tipo_vehiculo,patentes_horas_entradas)

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


