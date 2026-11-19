import math
producto =input("indica el nombre del producto")
cantidad =float(input("indica la cantidad"))
precio =float(input("indica el precio"))
totalSI = (cantidad * precio)
totalI = totalSI * 1.21
mensaje = "Ticket de compra"
print (f"{mensaje:^5}")
print ("=" * 32)
print (f"{producto:<15}{cantidad:^5}{totalI:>8.2f}$")

