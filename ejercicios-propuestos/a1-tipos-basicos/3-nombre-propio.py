"""
def capitalize(nombre: str):
    return nombre.capitalize()

def capitalize2(nombre: str):
    return nombre[0].upper() + nombre[1:].lower()

def capitalize3(nombre: str):
    nombreAux = ""
    for index, character in enumerate(nombre):
        character = character.upper() if index == 0 else character.lower()
        nombreAux = nombreAux + character
    return nombreAux


print(capitalize("blacky"))
print(capitalize("bLaCkY"))
print(capitalize("BLACKY"))



print(capitalize2("blacky"))
print(capitalize2("bLaCkY"))
print(capitalize2("BLACKY"))

print(capitalize3("blacky"))
print(capitalize3("bLaCkY"))
print(capitalize3("BLACKY"))
"""
nombre_propio = "blacky"
print(nombre_propio.capitalize())
print(nombre_propio[0].upper() + nombre_propio[1:].lower())

nombreAux = ""
for index, character in enumerate(nombre_propio):
    character = character.upper() if index == 0 else character.lower()
    nombreAux = nombreAux + character

print(nombreAux)

