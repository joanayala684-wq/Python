"""El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más
abajo, donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se
le aplica. Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los
nombres de los campos con la información contenida en el directorio.

Escribir un programa que genere un diccionario con la información, donde cada elemento corresponde
a un cliente y tiene por clave su nif y por valor otro diccionario con el resto de la información del cliente.
Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y
como valores la información de cada cliente correspondientes a esos campos. Es decir, un diccionario
como el siguiente"""
cadena_clientes = (
    "nif;nombre;email;teléfono;descuento\n"
    "01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n"
    "71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n"
    "63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n"
    "98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
)

# 1. Separar la cadena en una lista de líneas por salto de línea (\n)
lineas = cadena_clientes.splitlines()

# 2. La primera línea contiene las claves/campos
campos = lineas[0].split(';')

# Diccionario principal que contendrá a todos los clientes
directorio_clientes = {}

for linea in lineas[1:]:
    datos = linea.split(";")
    cliente = dict(zip(campos, datos))
    nif = cliente["nif"]
    directorio_clientes[nif] = cliente
    
print(directorio_clientes)
    
for cliente, campo in directorio_clientes, campos:
    print("Cliente", cliente)
    print("Campo", campo)