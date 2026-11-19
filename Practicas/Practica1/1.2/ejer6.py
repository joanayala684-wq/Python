nombre=input("introduce tu nombre en minusculas").strip()
nombre_titulo = nombre.title()
print(f"tu nombre es: ", {nombre_titulo})

longitud = len(nombre)
print(f"tiene una extension de:", longitud)

lista_palabras = nombre.split(' ')
print(f"lista de palabras", lista_palabras)