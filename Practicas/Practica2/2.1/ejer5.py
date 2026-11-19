
import random 
max_intentos = 3
numero_secreto = random.randint(1, 100)
print("¡Bienvenido al juego de adivinar el número!")
print("He pensado un número entre 1 y 100. ¿Puedes adivinar cuál es?")
acertado = False
for intento_num in range(1, max_intentos+1):
    intento = int(input("introduce un numero: "))
    if intento < numero_secreto:
        print("el numero a adivinar es mayor")
    elif intento > numero_secreto:
        print("el numero a adivinar es menor")
    else:
        print("has acertado")
        break
else:
    print(f"se acabaron los intentos, El numero era: {numero_secreto}")