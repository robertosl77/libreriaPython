import random

class BlackJack:
    
    def tomaNombre():
        while True:
            nombre = input("Ingrese su nombre, o escriba 'x' para cancelar: ")    
            if len(nombre) > 0:
                print(f"¡Bienvenido {nombre} al 21!")
                return nombre
            
    def mazoCartas(indice):
        cartas_poker = [
            (1, 'As de Corazones', 14), (2, '2 de Corazones', 2), (3, '3 de Corazones', 3), (4, '4 de Corazones', 4), (5, '5 de Corazones', 5),
            (6, '6 de Corazones', 6), (7, '7 de Corazones', 7), (8, '8 de Corazones', 8), (9, '9 de Corazones', 9), (10, '10 de Corazones', 10),
            (11, 'J de Corazones', 11), (12, 'Q de Corazones', 12), (13, 'K de Corazones', 13),
            (14, 'As de Diamantes', 14), (15, '2 de Diamantes', 2), (16, '3 de Diamantes', 3), (17, '4 de Diamantes', 4), (18, '5 de Diamantes', 5),
            (19, '6 de Diamantes', 6), (20, '7 de Diamantes', 7), (21, '8 de Diamantes', 8), (22, '9 de Diamantes', 9), (23, '10 de Diamantes', 10),
            (24, 'J de Diamantes', 11), (25, 'Q de Diamantes', 12), (26, 'K de Diamantes', 13),
            (27, 'As de Tréboles', 14), (28, '2 de Tréboles', 2), (29, '3 de Tréboles', 3), (30, '4 de Tréboles', 4), (31, '5 de Tréboles', 5),
            (32, '6 de Tréboles', 6), (33, '7 de Tréboles', 7), (34, '8 de Tréboles', 8), (35, '9 de Tréboles', 9), (36, '10 de Tréboles', 10),
            (37, 'J de Tréboles', 11), (38, 'Q de Tréboles', 12), (39, 'K de Tréboles', 13),
            (40, 'As de Picas', 14), (41, '2 de Picas', 2), (42, '3 de Picas', 3), (43, '4 de Picas', 4), (44, '5 de Picas', 5),
            (45, '6 de Picas', 6), (46, '7 de Picas', 7), (47, '8 de Picas', 8), (48, '9 de Picas', 9), (49, '10 de Picas', 10),
            (50, 'J de Picas', 11), (51, 'Q de Picas', 12), (52, 'K de Picas', 13)
        ]
        return cartas_poker[indice - 1]  # Convertir índice a 0 basado en index

    def resultadoJuego(suma_jugador):
        suma_pc=random.randint(14, 32)
        if suma_pc>21 or suma_pc<suma_jugador:
            print(f"Ahora es el turno de la pc... al final sumo {suma_pc}, entonces: Usted Gano!")
        elif suma_pc>suma_jugador:
            print(f"Ahora es el turno de la pc... al final sumo {suma_pc}, entonces: La PC Gano!")
        else:
            print(f"Ahora es el turno de la pc... al final sumo {suma_pc}, entonces: Empataron!")    

    # Inicializar la suma del jugador
    suma_jugador = 0
    nombre = "Rob"

    # nombre= tomaNombre()
    if nombre.lower() == 'x':
        print("Saliendo del sistema...")
    else:
        while True:
            rnd = random.randint(1, 52)  # Obtener un número aleatorio entre 1 y 52
            carta = mazoCartas(rnd)
            nombre_carta = carta[1]
            suma_jugador += carta[2]
            print(f"\aSe repartio del mazo: \n\tCarta: {nombre_carta} \n\tSuma: {suma_jugador} puntos")
            if suma_jugador>21:
                break
            stop = input("\nIngrese 'n' para parar o cualquier tecla para continuar: ")
            if stop.lower() == 'n':
                break
        # 
        if suma_jugador>21:
            print("ha perdido!")
        else:
            resultadoJuego(suma_jugador)
            
                