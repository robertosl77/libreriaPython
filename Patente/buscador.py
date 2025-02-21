import re

class Buscador:

    def __init__(self) -> None:
        pass

    def validar_patente(patente):
        patron = r'^[A-Z]{3}[0-9]{3}$'
        return re.match(patron, patente)

    def calcular(patente):
        num = int(patente[3:])
        car = [ord(letra) - ord('A') for letra in list(patente[:3])]
        calculo = car[0] * 26**2 * 1000
        calculo += car[1] * 26 * 1000
        calculo += car[2] * 1000
        calculo += num
        return calculo

    def id_a_patente(id):
        id_letras = id // 1000
        numeros = id % 1000
        letra1 = chr((id_letras // 26**2) + ord('A'))
        letra2 = chr(((id_letras % 26**2) // 26) + ord('A'))
        letra3 = chr((id_letras % 26) + ord('A'))
        patente = f"{letra1}{letra2}{letra3}{numeros:03d}"
        return patente


