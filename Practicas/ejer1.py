mi_lista = []
pares = []
miaw= True
while True:
    numero =print("introduce un numero")
    if (numero >= 0 ):
        mi_lista.append(numero)
        if (numero % 2 == 0):
            pares.append(numero)
            
    else :
        if (miaw == False): 
    
            cantidad = len(mi_lista)
            cantidad_pares = len(pares)
            if (cantidad != 0 ):
                print("el numero maximo de valores introducidos es de " + cantidad)
            else :
                print("no se ha introducido ningun numero par")   
            if ( cantidad_pares != 0 ):
                    print("los numeros pares introducidos son")
                    print(pares)
            else :
                print("no se ha introducido ningun numero par")
        break
    
