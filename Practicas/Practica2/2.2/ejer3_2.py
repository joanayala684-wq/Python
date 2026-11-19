def operar(n1, n2, operador="+", resultado="El resultado es:"):
    if operador == "+":
        res = n1 + n2
    elif operador == "-":
        res = n1 - n2
    elif operador == "*":
        res = n1 * n2
    elif operador == "/":
        res = n1 / n2 if n2 != 0 else "Error (división por cero)"
    else:
        return "Operador no válido"

    return f"{resultado} {res}"