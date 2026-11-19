grupo_A = set()
grupo_B = set()
grupo = ""

def agregar(grupo, juego):
    match grupo:
        case "A":
            grupo_A.add(juego)
        case "B":
            grupo_B.add(juego)
        case _:
            print("grupo no valido")
            return -1
while grupo != "fin":
    grupo = input("indica el grupo al que perteneces").strip()
    if grupo.lower() == "fin":
        break
    
    juego = input("indica el juego").strip()
    if (grupo == ""  or juego == ""):
        print("Debes mencionar el grupo y el juego")
    else:
        agregar(grupo.upper(), juego.capitalize())
if (len(grupo_A) > 0 and len(grupo_B) > 0):
    juegos_en_comun = grupo_A & grupo_B
    todos_los_juegos = grupo_A | grupo_B
    solo_grupo_a = grupo_A - grupo_B
    
    print("--- RESULTADOS ---")
    print("Juegos en común:", juegos_en_comun)
    print("Todos los juegos únicos:", todos_los_juegos)
    print("Solo le gustan al Grupo A:", solo_grupo_a)
else:
    print("Debes ingresar al menos un juego en cada grupo para hacer las operaciones.")