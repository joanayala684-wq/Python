mensaje_alienigena = ["zorg", "gleep", "zorg", "vort", "blip", 
    "zorg", "gleep", "xenon", "blip", "zorg", 
    "vort", "krypton", "zorg"]

palabras_unicas = set(mensaje_alienigena)
lista_ordenada = sorted(palabras_unicas)
tupla_ordenada = tuple(lista_ordenada)
#tupla_ordenada = tuple(sorted(palabras_unicas))

print("Palabras únicas:", palabras_unicas)
print("Tupla ordenada:", tupla_ordenada)

palabra = input("introduce la palabra que deceas contar: ").strip().lower()
if ( palabra == ""):
    print("debes indicar una palabra valida")
else:
    repeticion = mensaje_alienigena.count(palabra)
    if (repeticion == 0):
        print("no se ha encontrado ninguna palabra que coincida")
    else :
        print("el numero de veces que " +palabra+ " aparece es " + str(repeticion))
        