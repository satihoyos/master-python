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
        response = response + 'Monedas de ' + i + ": " + str(cambio_monedas[i]) + ", "
    return response


print(cambio(459))
print(cambio(20))
print(cambio(4))
print(cambio(100))
