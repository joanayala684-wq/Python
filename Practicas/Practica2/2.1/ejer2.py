n = int(input("introduce un numero entero"))
if n <= 0:
    print(f"el numero introducido es incorrecto")
elif n > 0 and n <=12:
    resto= n % 1
    if resto != 0:
        print("el numero introducido no es entero")
    else:
        if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
         print(f"el mes {n} tiene 31 dias")
        elif n == 2:
             print(f"el mes {n} tiene 28 dias")
        else: 
            print(f"el mes {n} tiene 30 dias")

"""hacerlo mejor con un matches de lista"""