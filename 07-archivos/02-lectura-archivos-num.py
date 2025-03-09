g =  open('archivos/numeros.txt')
lista =  g.readlines()
print(lista)
g.close()

lista_num = []
for cad in lista:
    lista_num.append(int(cad.strip()))
print(lista_num)
print('--------------------')

f = open('archivos/agenda.txt')
linea = f.readline()
print(linea)
elementos = linea.split()
print(elementos)
agenda = {
    elementos[0]: {
        "peso": int(elementos[1]),
        "altura": float(elementos[2]),
        "direccion": elementos[3]
    }
}

print(agenda)
f.close()

f = open('archivos/agenda.txt')
agenda = dict()
for linea in f:
    elementos = linea.split()
    agenda[linea[0]] = {
        "peso": int(elementos[1]),
        "altura": float(elementos[2]),
        "direccion": elementos[3]
    }
print(agenda)
f.close()

line_test = [
    'Fernando # 75 # 1.90 # carretera de Húmera, Pozuelo        # 28223',
    'Elena    # 70 # 1.70 # calle Bárbara de Braganza, Madrid   # 28004'
]

for l in line_test:
    split_1 = l.split("#")
    for s in split_1:
        print(" --- strip --")
        print(s.strip())
        print(" --- rstrip --")
        print(s.rstrip())
        print(" --- lstrip --")
        print(s.lstrip())

for l in line_test:
    split_1 = l.split(" # ")
    for s in split_1:
        print(" --- strip --")
        print(s.strip())
        print(" --- rstrip --")
        print(s.rstrip())
        print(" --- lstrip --")
        print(s.lstrip())

print("map & listas intensionales")
lista_cadenas = ['1\n', '2\n', '3\n', '4\n', '5\n']
lista_num = list(map(int, lista_cadenas))
print(lista_num)

lista_num2 = [int(cad) for cad in lista_cadenas]
print(lista_num2)

