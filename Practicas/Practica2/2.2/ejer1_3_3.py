x = 10
match x:
    case 10 if x % 2 == 0:
        print("es 10 y es par")
    case 10 :
        print("es 10 y no par")
    case _:
        print("opcion por defecto")
        