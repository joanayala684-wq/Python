def sumar(*args):
    """Suma un numero indefinido de argumentos posicionales"""
    acumulado= 0
    for num in args:
        acumulado += num 
    return acumulado 

print("--- Tarea 1: sumar(*args) ---")
print(f"sumar(2)        -> {sumar(2)}")  # Devuelve 2
print(f"sumar(2, 3, 4)  -> {sumar(2, 3, 4)}")  # Devuelve 9
print(f"sumar()         -> {sumar()}\n")  # Caso sin argumentos: devuelve 0


def funcion3 (semilla=1, **kwargs):
    """Resta cada valor de kwargs a la variable semilla"""
    resultado = semilla 
    for valor in kwargs.values():
        resultado -= valor
    return resultado 