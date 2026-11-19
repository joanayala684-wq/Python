import math
n1 = float(input("indica el primer numero"))
n2 = float(input("indica el segundo numero"))

def suma(n1, n2):
    return n1 + n2
def resta(n1, n2):
    return n1 - n2
def multi(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1/n2
print (f"la suma de ambos numeros es {suma(n1,n2)}")
print (f"la resta de ambos numeros es {resta(n1,n2)}")
print (f"la multi de ambos numeros es {multi(n1,n2)}")
print (f"la division de ambos numeros es {division(n1,n2)}")