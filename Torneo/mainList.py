import random
"""Organizas un torneo relámpago de videojuegos con un máximo de 8 jugadores titulares. Abres un registro en consola donde los jugadores escriben su nickname y su puntuación media (un número entero entre 100 y 1000). Un mismo jugador puede intentar registrarse varias veces por error. El registro se cierra cuando se escribe "FIN".

Al cerrar el registro, el sistema debe:
a. Eliminar los registros duplicados (si un jugador se apuntó varias veces, nos quedamos con su última puntuación registrada).
b. Validar mediante excepciones que la puntuación sea un número entero válido; si meten letras o un número fuera de rango (100-1000), avisar sin que el programa se rompa.
c. Si hay más de 8 jugadores, eliminar primero a los jugadores con puntuación inferior a 300 puntos (pasándolos a una lista de reservas). Si tras esto siguen sobrando jugadores, elegir titulares al azar hasta tener exactamente 8, enviando el resto a reservas.
d. Si al aplicar el corte de los 300 puntos nos quedamos con menos de 8 jugadores, ir rescatando jugadores de reservas (empezando por los de mayor puntuación) hasta completar los 8 titulares.
e. Imprimir la lista final de titulares ordenada alfabéticamente y mostrar la media de puntos del torneo."""
def gestionar_torneo(jugadores: dict[str, int]) -> list[str]:
    titulares: list[str] = []
    reservas: list[str] = []

    # Si no se supera el límite de 8, entran todos directamente
    if len(jugadores) <= 8:
        titulares = list(jugadores.keys())
        titulares.sort()
        return titulares

    # c. Si hay más de 8, filtramos primero por puntuación >= 300
    for nick, puntos in jugadores.items():
        if puntos >= 300:
            titulares.append(nick)
        else:
            reservas.append(nick)

    # Si siguen sobrando más de 8 titulares, sacamos al azar y mandamos a reservas
    while len(titulares) > 8:
        # Elegimos un índice al azar entre 0 y el último elemento de titulares
        indice_azar: int = random.randint(0, len(titulares) - 1)
        eliminado: str = titulares.pop(indice_azar)  # .pop() lo saca y lo devuelve
        reservas.append(eliminado)

    # d. Si tras el filtro de 300 puntos faltan jugadores para llegar a 8:
    if len(titulares) < 8:
        # Ordenamos las reservas de MAYOR a MENOR puntuación usando una función clave
        # (x es el nick, jugadores[x] es su puntuación)
        reservas.sort(key=lambda x: jugadores[x], reverse=True)

        while len(titulares) < 8 and len(reservas) > 0:
            # Sacamos el primero de reservas (el de mayor puntuación) con .pop(0)
            rescatado: str = reservas.pop(0)
            titulares.append(rescatado)

    # e. Ordenamos alfabéticamente la lista final
    titulares.sort()
    return titulares


# --- PROGRAMA PRINCIPAL ---
# Usamos un diccionario {nick: puntos} porque las claves son ÚNICAS:
# si alguien se apunta dos veces, sobrescribe su puntuación (cumple el punto a).
registro: dict[str, int] = {}

print("--- REGISTRO DEL TORNEO (Escribe 'FIN' en el nick para cerrar) ---")

nick: str = ""

while nick != "FIN":
    nick = input("Introduce tu nickname: ").strip().upper()
    
    if nick != "FIN":
        # Validamos que el nick no esté vacío ni tenga espacios raros
        if not nick.isalnum():
            print("Error: El nickname solo puede contener letras y números.")
            continue  # Vuelve al inicio del while sin pedir puntos

        # b. Control de excepciones para pedir un número entero válido
        try:
            puntos: int = int(input(f"Puntuación de {nick} (100-1000): "))
            
            if puntos < 100 or puntos > 1000:
                print("Error: La puntuación debe estar entre 100 y 1000.")
                continue
                
            # Guardamos en el diccionario (si ya existía, se actualiza)
            registro[nick] = puntos
            
        except ValueError:
            print("Error: Debes introducir un número entero, no letras.")
# Ejecutamos la lógica del torneo
lista_titulares: list[str] = gestionar_torneo(registro)

# Calculamos la media de puntos de los titulares elegidos
suma_puntos: int = 0
for jugador in lista_titulares:
    suma_puntos += registro[jugador]

# Evitamos ZeroDivisionError por si no se apuntó nadie
media: float = suma_puntos / len(lista_titulares) if len(lista_titulares) > 0 else 0.0

print(f"\nTitulares oficiales ({len(lista_titulares)}): {lista_titulares}")
print(f"Media de nivel del torneo: {media:.2f} puntos")

