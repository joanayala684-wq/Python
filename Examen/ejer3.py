inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]
def anyadir_precio(item):
    zona = item['zona']
    metros = item['metros']
    habitaciones = item['habitaciones']
    garaje = item['garaje']
    año = item['año']
    if zona == "A" :
        precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (año / 100)   
    elif zona == "B":
        precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (año / 100) * 1.5
    else: 
        return -1
    item['precio'] = precio    
    
for item in inmuebles:
    anyadir_precio(item)
    
def filtrar (precio_leido, inmuebles):
    lista_inmuebles = []
    for item in inmuebles:
        precio = item['precio']
        if precio <= precio_leido:
            lista_inmuebles.append(item)
    return lista_inmuebles

    
precio_leido = int(input("Dime el precio por el cual quieres buscar: "))
lista_inmuebles = filtrar(precio_leido, inmuebles)
print(lista_inmuebles)