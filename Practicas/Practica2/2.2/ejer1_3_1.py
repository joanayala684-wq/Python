x = 20
match x: 
    case 10 | 20 | 30:
        print(f"Matched: {x}")
    case _:
        print("no match found")
        