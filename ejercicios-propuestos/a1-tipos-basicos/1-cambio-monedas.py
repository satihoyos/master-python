"""
def calculate_division(dividendo, divisor):
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return cociente, resto


def cambio2(dinero, monedas_diccinario, position_key):
    key = list(monedas_diccinario)[position_key]
    monedas_diccinario[key], resto = calculate_division(dinero, int(key))
    if resto > 0:
        cambio2(resto, monedas_diccinario, position_key + 1)


def cambio(dinero):
    cambio_monedas = {'25': 0, '5': 0, '1': 0}
    cambio2(dinero, cambio_monedas, 0)
    keys = list(cambio_monedas)
    response = ""
    for i in keys:
        msg = "Monedas de {0}: {1}, ".format(i, str(cambio_monedas[i]))
        response = response + ' ' + msg
    return response


print(cambio(459))
print(cambio(20))
print(cambio(4))
print(cambio(100))
"""
dinero = 459
monedas_25 = dinero//25
dinero = dinero % 25
monedas_5 = dinero//5
dinero = dinero % 5
monedas_1 = dinero//1

print("Monedas de 25:{0}, Monedas de 5: {1}, Monedas de 1{2}"
        .format(str(monedas_25), str(monedas_5), str(monedas_1)))
