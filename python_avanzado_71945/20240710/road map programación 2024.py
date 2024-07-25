



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

    # informacion un dato           (int, float, bool)
    #------------------------------------string "". metodos y atributos de uso
    # informacion por colecciones   (listas, tuplas, dict, set fset)
    print (dir(str()))

    """
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

    """
    #metodos y atributos por ubicacion
    string= " Hola Programacion avanzada IT 2024"
    print (f" center |{string.center(75)}|")
    print (f" rjust  |{string.rjust(75)}|")
    print (f" ljust  |{string.ljust(75)}|")
    #metodos y atributos por estilo
    print("*"*50)
    print (f" capitalize |{string.capitalize()}|")
    print (f" casefold   |{string.casefold()}|")
    print (f" lower      |{string.lower()}|")
    print (f" upper      |{string.upper()}|")
    print (f" title      |{string.title()}|")
    print (f" swapcase   |{string.swapcase()}|")
    print("*"*50)
    print (f" upper center |{string.upper().center(75)}|")
    print (f" center upper |{string.center(75).upper()}|")
    print (f" title  rjust |{string.title().rjust(75)}|")
    print("*"*50)
    #metodos y atributos por booleanos
    """
    'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
    'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper','startswith','endswith',
    """
    dato = "Ariel"
    print (f"startswith   {dato.startswith('Ar')=}")

    print (f"endswith   {dato.endswith('Ar')=}")
    # ~ dato = "Juan Carlos"
    # ~ dato = "2024"
    dato = "3.14159"

    print (f"isalnum   {dato.isalnum()=}")
    print (f"isalpha   {dato.isalpha()=}")#A-Z a-z
    print (f"isascii   {dato.isascii()=}")
    print (f"isdecimal {dato.isdecimal()=}")#simil isdigit
    print (f"isdigit   {dato.isdigit()=}")#0-9
    print (f"isnumeric {dato.isnumeric()=}")#simil isdigit
    print("*"*50)

    #metodos y atributos replace

    dato = "Ariel Garcia"
    print(f"{dato}")
    print(f"{dato.replace('Ariel', 'Profe')}")
    print(f"{dato}")

    dato = dato.replace('Ariel', 'Profe')
    print(f"{dato}")

    print("-"*50)
    numero = ""
    while not numero.isdigit():
        numero =  input("ingrese un numero entero:")
    numero = int (numero)
    print (f"{numero} {type(numero)}")


    print("-"*50)

    numero = ""
    while not numero.replace(".","").isdigit():# condiciono
        numero = input("ingrese un numero real:")
        numero = numero.replace(",",".")# piso el dato
    numero = float (numero)
    print (f"{numero} {type(numero)}")


    print("-"*50)

    ########################################################################
    import this
    
    
def segundo_paso():
    # ~ ya_hechos()
    # ~ print("-"*50)
    # ~ numero = ""
    # ~ while not numero.isdigit():
        # ~ numero =  input("ingrese un numero entero:")
    # ~ numero = int (numero)
    # ~ print (f"{numero} {type(numero)}")
    while True:
        try:
            numero =int(input ("ingrese un numero: ") )
            print (f"{numero} {type(numero)}")
            print (f"{numero=} {type(numero)=}")
            dato = 100/numero
            print (f"{dato=}")
            # ~ print (f"{pepe}")
            break
        except ValueError:
            print (f"no se puede convertir a entero")
        except ZeroDivisionError:
            print (f"no se puede dividir en cero")
        except Exception as meti_la_pata:
            print ("Su dato no se pudo procesar")
            print (f"el error fue {meti_la_pata}")
    """
    el error fue division by zero
    el error fue invalid literal for int() with base 10: 'cinco'
    el error fue name 'pepe' is not defined
    """
    print ("sali")






















