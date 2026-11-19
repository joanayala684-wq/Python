"""Organizas una fiesta para 25 personas, abres un formulario para que se apunte
todo el que quiera, una persona puede apuntarse varias veces. Cuando cierras
fecha:
a. Elimina a los repetidos dejando solo una vez a cada persona
b. Ordena la lista de invitados alfabéticamente.
c. Si se ha superado el aforo, genera una letra aleatoriamente y crea una
nueva lista con los nombres que empiecen con esa letra o posteriores. Si
sigue habiendo más de 50 personas, genera otra letra posterior a la
anterior y repite el proceso... Lo harás tantas veces como sea necesario.
Genera una lista con todas las personas que se van quedando fuera de la
fiesta. Si en el último descarte, no se llega a 25 personas, irás sacando de
la lista de “espera” hasta completar el aforo.
d. Imprime el mensaje: «Los elegidos de la fiesta son: [...]»."""
import random
def addPersons (contListas: int, cont: int, lista: list[str], descarte: list[str] ):
    abecedario: list[str] = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    contPeople : int =0
    indice_minimo: int = 0
    while len(lista) > 25:
        
        num: int =random.randint(0, len(abecedario)-1)
        listaLimpia: list[str] =[]
        for contPeople in range (len(lista)):
            persona: str =lista[contPeople]
            for i in range(num, len(abecedario)):
                letra: str = abecedario[i]
                if persona[0] == letra:
                    listaLimpia.append(persona)
                    cont += 1
                    break
            if persona not in listaLimpia:
                descarte.append(persona)    
        lista = listaLimpia
        num+=1
        if (num >= len(abecedario)):
            break
    if (len(listaLimpia) < 25):
        for i in range(len(lista), 25):
            if len(descarte) > 0:
                lista.append(descarte.pop(0))
            
    lista.sort()
    print(f"Los elegidos de la fiesta son: {lista}")
            
listaPersonas: list[str] = []
listaDescarte: list[str] = []

nombre: str =""
cont: int =0
contListas: int =1
print("Holaa, bienvenido a la lista de invitados")
while nombre != "SAL":
    nombre : str =input ("introduce tu nombre").upper()
    if (nombre == "SAL"):
        break
    else:
        if (nombre.isalpha()):
            listaPersonas.append(nombre)
            cont+=1
        else:
            print("debes introducir un nombre valido")    
invitados_unicos: set[str] = set(listaPersonas)       
listaOrdenada: list[str] = list(invitados_unicos) 
listaOrdenada.sort()

addPersons(contListas, cont, listaOrdenada, listaDescarte)