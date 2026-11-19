lista_compra=input("introduce la lista de compra separada por comas").strip().upper()
lista_producto=lista_compra.split(",")

productos = []
for elemento in lista_producto:
    producto_limpio = elemento.strip()
    
tiene_leche = "LECHE" in productos
no_empty= True

for producto in productos:
    if producto == "":
       no_empty = False
       break
   
print("\n--- RESUMEN DE LA CESTA ---")
print("Lista de producno_emptytos:", productos)
print("Cantidad total de elementos:", len(productos))
print("¿Contiene 'LECHE'?:", tiene_leche)
print("¿Sin elementos vacíos?:", no_empty)