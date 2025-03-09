f = open('archivos/texto.txt', 'r')  # r = se abre en forma de lectura
for linea in f:
    print(linea.strip())
f.close()

print("----------------")

f = open('archivos/texto.txt', 'r')
for linea in f:
    print(linea, end="")
f.close()

print("----------------")
f = open('archivos/texto.txt', 'r')
for linea in f:
    print(linea.strip(), end="")
f.close()
print()
print(" ---- print readline ---- ")
f = open('archivos/texto.txt', 'r')
a = f.readline()
print(a)
a = f.readline()
print(a)

print("----------------------------")

linea = f.readline()
i = 1

while linea != '':
    print(i, " - ", linea)
    linea = f.readline()
    i += 1
f.close()

print("----------------------------")
f = open('archivos/texto.txt', 'r')
lista = f.readlines()
print(type(lista), len(lista))
print(lista)
f.close()

print(lista[2].strip())



