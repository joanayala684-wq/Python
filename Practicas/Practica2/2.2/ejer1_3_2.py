data = [ "py", "java", "C" ]
match data:
    case [x, y]:
        print("lista de dos elementos: {x}, {y}")
    case [x, y, z]:
        print("lista de tres elemntos: {x}, {y}, {z}")
    case _:
        print("formato desconocido")