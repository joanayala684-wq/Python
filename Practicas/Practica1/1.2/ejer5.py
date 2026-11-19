import math
a= 256
b= 256
x= [1, 2]
y= [1, 2]
print(f"a == b: {a == b}")
print(f"a is b: {a is b}")
print(f"x == y: {x == y}")
print(f"x is y: {x is y}")
print(f"id(a): {id(a)}")
print(f"id(a): {id(b)}")
print(f"id(a): {id(x)}")
print(f"id(a): {id(y)}")
"""
EXPLICACIÓN:

1. `a is b` devuelve True debido al "Integer Caching" (internado de enteros) de Python:
   Python preasigna y reutiliza en memoria los enteros pequeños en el rango de -5 a 256.
   Por lo tanto, `a` y `b` hacen referencia exactamente al mismo objeto en memoria (tienen el mismo id).

2. `x is y` devuelve False porque las listas son objetos mutables:
   Cada vez que creas una lista con `[]`, Python reserva un nuevo bloque de memoria para ella,
   incluso si contienen los mismos valores. Por eso `x` e `y` son dos objetos distintos con
   diferentes identificadores de memoria.
"""
