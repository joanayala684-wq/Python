caracter = input("INtroduce un caracter: ")
if len(caracter) != 1:
        print("por favor, introduce solo un caracter")
elif caracter.islower():
        print(f"'{caracter}' es una letra MINUSCULA")
elif caracter.isupper():
        print(f"'{caracter}' es una letra MAYUSCULAS")
elif caracter.isdigit():
        print(f"'{caracter}' es un DIGITO")
else:
        print(f"'{caracter}' no es ni una letra ni un digito")