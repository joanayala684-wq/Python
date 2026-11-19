cantidad =float(input("introduce la cantidad a retirar"))
if cantidad <= 0:
    print(f" la cantidad introducida no es valida. Introducir un numero positivo")
elif cantidad >= 0 and cantidad <= 999:
    total=cantidad+10
elif cantidad > 999 and cantidad <= 1999:
    total=cantidad+20
else:
    total=cantidad+30
print(f"el total de esta operacion es de {cantidad+total}$")
