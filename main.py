from readchar import readkey, key
''' la libreria readchar tiene dos metodos 
readchar.readchar() para leer caracteres individuales
y readchar.readkey(). para leer pulsaciones de teclas.


'''
jugador = input("Escribe tu nombre: ")
print("Bienvenido " + jugador + " al juego")

while True:
    impresion = readkey()
    print(f'{impresion}\n')
    if impresion == key.UP:
        break
