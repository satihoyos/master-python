# conjuntos: collecion de elementos sin orden ni repeticion

conj_a = {"a", "e", "i", "0", "u"}
conj_b = {"a", "b", "r", "a", "c", "a", "d", "a", "b", "r", "a"}

print("A = ", conj_a)
print("B = ", conj_b)
print("A union B = ", conj_a | conj_b)
print("A interseccion B = ", conj_a & conj_b)
print("A dif. simetrica B = ", conj_a ^ conj_b)

print("union", conj_a.union(conj_b))
print("Interseccion", conj_a.union({"a", "r", "p", "e", "g", "i", "o", "u"}))
print("diferencia", conj_a.difference({"a", "g", "r", "i", "o"}))
print("A = ", conj_a)
print("B = ", conj_b)
print("subconjunto", conj_a.issubset({"t", "r", "o", "p", "e", "t", "a"}))


conj_A = set("aeiou")
print(conj_A)
conj_A.add("A")
print(conj_A)
conj_A.remove("A")
print(conj_A)

if "a" in conj_A:
    print("a esta en el conjunto")
else:
    print("a no esta en el conjunto")

conj_a = {c for c in "aeiou"}
conj_b = {c for c in "abracadabra"}

print("A = ", conj_a)
print("B = ", conj_b)

# diccionario
telefonos = {"despacho": 397, "casa": 1111111}
print(telefonos)
telefonos["movil"] = 222222
print(telefonos)
del telefonos["movil"]
print(telefonos)
print("keys:", telefonos.keys())  # no es una lista type dict_keys
print("keys:", list(telefonos.keys()))
print("keys:", telefonos.values())  # no es una lista type dict_values
print("keys:", list(telefonos.values()))

for key in telefonos:
    print(key, telefonos[key])

for item in telefonos.items():
    print("item", item)

for key, value in telefonos.items():
    print(key, value)


def cuenta_letra(texto):
    contadores = dict()
    for car in texto:
        if car in contadores:
            contadores[car] = contadores[car] + 1
        else:
            contadores[car] = 1
    return contadores

texto_eje = """
esto es una prueba de texto 
"""

print(cuenta_letra(texto_eje))


from collections import defaultdict
def cuenta_letra2(texto):
    contadores = defaultdict(int) # defaultdict(list),  defaultdict(set)
    for car in texto:
        if car.isalpha():
            contadores[car] = contadores[car] + 1
    return contadores

print( cuenta_letra2("texto_eje"))

