import os
from readchar import readkey, key
''' la libreria readchar tiene dos metodos 
readchar.readchar() para leer caracteres individuales
y readchar.readkey(). para leer pulsaciones de teclas.


'''
jugador = input("Escribe tu nombre: ")
print("Bienvenido " + jugador + " al juego")

numero = 0
while numero <= 50:
    impresion = readkey()
    
    if impresion == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(numero)
        numero += 1

print("Juego terminado")
