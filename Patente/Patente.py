import re

def obtiene_patente():
    # Solicitar al usuario que ingrese una patente
    while True:
        patente = input("Ingrese la patente: ").upper()
        # Validar la patente
        if validar_patente(patente):
            break
    return patente

def validar_patente(patente):
    # Definir el patrón de la patente
    patron = r'^[A-Z]{3}[0-9]{3}$'
    # Usar re.match para verificar si la entrada coincide con el patrón
    return re.match(patron, patente)

def calcular(patente):
    num = int(patente[3:])
    car = [ord(letra) - ord('A') for letra in list(patente[:3])]
    # Calcula
    calculo = car[0] * 26**2 * 1000
    calculo += car[1] * 26 * 1000
    calculo += car[2] * 1000
    calculo += num
    print(f"Se obtuvieron los siguientes resultados: \n\tPatente ingresada: {patente}\n\tCombinación numérica: {car}[{num}]\n\tID Calculado: {calculo}")
    return calculo

def id_a_patente(id):
    # Dividir el ID en la parte de letras y la parte de números
    id_letras = id // 1000
    numeros = id % 1000
    
    # Convertir la parte de letras de vuelta a caracteres
    letra1 = chr((id_letras // 26**2) + ord('A'))
    letra2 = chr(((id_letras % 26**2) // 26) + ord('A'))
    letra3 = chr((id_letras % 26) + ord('A'))
    
    # Formatear la parte numérica para que tenga tres dígitos
    patente = f"{letra1}{letra2}{letra3}{numeros:03d}"
    print(f"Patente generada a partir del ID: {patente}")
    return patente

print("El sistema calculará el número correcto de ID:")
# Obtengo la información por separado
id_a_patente(calcular(obtiene_patente()))
