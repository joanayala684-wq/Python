def pintar (height, width, caracter="*"):
    for i in range (height):
        for j in range (width):
            print(caracter, end="")
        print()
print("Rectángulo de 3x5 con '*':")
pintar(3, 5)
