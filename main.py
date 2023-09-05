import os
import random
from readchar import readkey, key
from typing import Tuple


class Juego:
    def __init__(self, mapa: str, inicio: Tuple[int, int],
                 fin: Tuple[int, int]):
        # Convierte el mapa en una lista de cadenas
        self.mapa = list(mapa.split('\n'))
        self.inicio = inicio
        self.fin = fin

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n'.join(self.mapa))

    def main_loop(self):
        px, py = self.inicio
        while (px, py) != self.fin:
            self.limpiar_pantalla()
            tecla = readkey()
            nueva_px, nueva_py = px, py

            if tecla == key.UP:
                nueva_px -= 1
            elif tecla == key.DOWN:
                nueva_px += 1
            elif tecla == key.LEFT:
                nueva_py -= 1
            elif tecla == key.RIGHT:
                nueva_py += 1

            if (
                0 <= nueva_px < len(self.mapa) and
                0 <= nueva_py < len(self.mapa[0]) and
                self.mapa[nueva_px][nueva_py] != '#'
            ):
                # Mover la 'P'
                fila = list(self.mapa[px])
                fila[py] = '.'
                self.mapa[px] = ''.join(fila)
                px, py = nueva_px, nueva_py
                fila = list(self.mapa[px])
                fila[py] = 'P'
                self.mapa[px] = ''.join(fila)

        self.limpiar_pantalla()
        print(f"Felicitaciones {jugador}!. Has llegado a tu destino")


class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        archivos_mapas = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(archivos_mapas)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)
        mapa, inicio, fin = self.leer_mapa(path_completo)
        super().__init__(mapa, inicio, fin)

    def leer_mapa(self, archivo):
        with open(archivo, 'r') as file:
            contenido = file.read().strip().split('\n')

        inicio = tuple(map(int, contenido[1].strip().split()))
        fin = tuple(map(int, contenido[2].strip().split()))
        mapa = contenido[3:]
        return '\n'.join(mapa), inicio, fin


jugador = input("Escribe tu nombre: ")
print("Bienvenido " + jugador + " al juego")

path_a_mapas = 'mapas'
juego = JuegoArchivo(path_a_mapas)
juego.main_loop()
