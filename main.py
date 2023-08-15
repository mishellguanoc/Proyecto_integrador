import os
from readchar import readkey, key
from typing import List, Tuple

jugador = input("Escribe tu nombre: ")
print("Bienvenido " + jugador + " al juego")


mapa_str = '..###################\n....#.#.............#\n###.#.###.###.#.#####\n#.#.........#.#...#.#\n#.#######.#######.#.#\n#.............#.....#\n###.###.#.###.###.###\n#...#.#.#.#.#.#.#.#.#\n#####.#.###.###.#.#.#\n#.........#.#.......#\n#.#####.###.#.#.#.###\n#.....#.#.#...#.#...#\n#########.###.#######\n#.#...#...#.#.......#\n#.#.#.#.###.#######.#\n#.#.#.....#.#...#...#\n#.###.#####.###.#.#.#\n#...#.#.#.........#.#\n###.#.#.#.#.#####.###\n#.........#.....#...#\n###################.#'

def convertir_mapa(mapa_str):
    lineas = mapa_str.strip().split('\n')  # Dividir la cadena en líneas
    
    global matriz
    matriz = [list(linea) for linea in lineas]  # Crear la matriz

    return matriz


def limpiar_pantalla():
    os.system('cls')
limpiar_pantalla()


def main_loop(mapa:List[List[str]],inicio:Tuple[int,int], fin: Tuple[int,int]):
    px, py = inicio

    while (px,py)!= fin:
        limpiar_pantalla()
        tecla = readkey()
        nueva_px, nueva_py = px, py

        if tecla == key.UP:
            nueva_px -=1
        elif tecla == key.DOWN:
            nueva_px += 1
        elif tecla == key.LEFT:
            nueva_py -= 1
        elif tecla == key.RIGHT:
            nueva_py += 1
        
        if (
            0 <= nueva_px < len(mapa) and
            0<= nueva_py < len(mapa[0]) and
            mapa[nueva_px][nueva_py] != '#'
        ):
            mapa[px][py] = '.'
            px,py = nueva_px, nueva_py
            mapa[px][py] = 'P'

        limpiar_pantalla()
    print("Has llegado a tu destino")



    
matriz = convertir_mapa(mapa_str)
inicio = (0, 0)
fin = (len(matriz) - 1, len(matriz[0]) - 1)

main_loop(matriz, inicio, fin)