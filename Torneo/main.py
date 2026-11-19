import random
"""Enunciado:

Organizas un torneo de eSports con un máximo de 8 jugadores titulares. Al abrir el registro, cada jugador introduce su nickname y su puntuación (un entero entre 100 y 1000). Si un jugador se registra varias veces, nos quedamos con su última puntuación. El registro cierra al escribir "FIN".

Al cerrar el registro:
a. Valida con excepciones que la puntuación sea un entero válido entre 100 y 1000.
b. Crea dos diccionarios: titulares: dict[str, int] y reservas: dict[str, int].
c. Si hay más de 8 inscritos, pasa a titulares solo los que tengan 300 puntos o más, y manda al resto a reservas. Si tras este filtro siguen habiendo más de 8 titulares, saca jugadores al azar de titulares y pásalos a reservas hasta que queden exactamente 8.
d. Si tras el filtro de 300 puntos hay menos de 8 titulares, rescata jugadores de reservas (empezando por los de mayor puntuación) y pásalos a titulares hasta completar los 8.
e. Imprime el diccionario final de titulares ordenado alfabéticamente por nickname y muestra la media de puntos."""
def gestionar_torneo(inscritos: dict[str, int]) -> dict[str, int]:
    titulares: dict[str, int] = {}
    reservas: dict[str, int] = {}

    # Si hay 8 o menos inscritos, entran todos al diccionario de titulares
    if len(inscritos) <= 8:
        # Ordenamos por clave (nickname) y reconstruimos el diccionario
        return dict(sorted(inscritos.items()))

    # c. Repartimos entre dos diccionarios según la puntuación (>= 300)
    for nick, puntos in inscritos.items():
        if puntos >= 300:
            titulares[nick] = puntos
        else:
            reservas[nick] = puntos

    # Si siguen sobrando titulares (> 8), sacamos al azar y movemos a reservas
    while len(titulares) > 8:
        # Sacamos las claves del diccionario como lista para elegir una al azar
        lista_nicks: list[str] = list(titulares.keys())
        nick_azar: str = random.choice(lista_nicks)
        
        # .pop(clave) en un diccionario lo borra y nos devuelve su valor (los puntos)
        puntos_eliminado: int = titulares.pop(nick_azar)
        reservas[nick_azar] = puntos_eliminado

    # d. Si tras el corte de 300 puntos faltan titulares (< 8), rescatamos de reservas
    if len(titulares) < 8 and len(reservas) > 0:
        # Ordenamos las parejas (nick, puntos) de reservas por puntuación (item[1]) de mayor a menor
        reservas_ordenadas: list[tuple[str, int]] = sorted(
            reservas.items(), key=lambda item: item[1], reverse=True
        )

        for nick, puntos in reservas_ordenadas:
            if len(titulares) == 8:
                break
            titulares[nick] = puntos
            reservas.pop(nick)  # Lo quitamos de reservas porque ya subió a titular

    # e. Devolvemos el diccionario ordenado alfabéticamente por clave (nick)
    titulares_ordenados: dict[str, int] = dict(sorted(titulares.items()))
    return titulares_ordenados


# --- PROGRAMA PRINCIPAL ---
registro: dict[str, int] = {}
nick: str = ""  # La inicializamos vacía para que entre al bucle

while nick != "FIN":
    nick = input("Nickname (o 'FIN' para cerrar): ").strip().upper()
    
    if nick != "FIN":
        if not nick.isalnum():
            print("Error: Solo letras y números.")
            continue

        try:
            puntos: int = int(input(f"Puntuación de {nick} (100-1000): "))
            if puntos < 100 or puntos > 1000:
                print("Error: Debe estar entre 100 y 1000.")
                continue
            
            registro[nick] = puntos
        except ValueError:
            print("Error: Introduce un número entero.")

# Llamamos a la función
dict_titulares: dict[str, int] = gestionar_torneo(registro)

# Calculamos la media usando .values() del diccionario (súper limpio)
media: float = sum(dict_titulares.values()) / len(dict_titulares) if len(dict_titulares) > 0 else 0.0

print("\n--- TITULARES OFICIALES ---")
for nick, puntos in dict_titulares.items():
    print(f"- {nick}: {puntos} pts")

print(f"Media de nivel: {media:.2f} puntos")