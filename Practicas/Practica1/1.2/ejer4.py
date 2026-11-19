import math
totalC=int(input(f"Introduce el num total de caramelos del evento"))
totalA=int(input(f"Introduce el num total de asistentes del evento"))
ca_persona, ca_sobra=divmod(totalC, totalA)
print(f"Cada participante recibe: {ca_persona} caramelos")
print(f"sobran en la caja: {ca_sobra} caramelos")

