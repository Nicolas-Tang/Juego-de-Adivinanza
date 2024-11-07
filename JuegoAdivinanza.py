import random


numeroSecreto = random.randint(0, 11)
cant_intentos = 0
cant_maxima_intentos = 3
adivinado = False

print('Bienvenido al juego de adivinar el numero secreto!!')

while not adivinado:
    if not cant_intentos < cant_maxima_intentos:
        print("Game Over! No has adivinado dentro de los 5 intentos")
        break
    numero = int(input("Introduce un numero del 1 al 10: ")) #TODO: convertir a numero

    if numero == numeroSecreto:
        print("Felicitaciones!! Has adivinado el numero secreto")
        adivinado = True
    elif numero < numeroSecreto:
        print("El numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")

    cant_intentos += 1
