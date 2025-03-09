with open('archivos/texto.txt', 'r') as f:  # uses close command automatically
    for linea in f:
        print(linea.strip())

with open('archivos/mi_texto2.txt', 'w') as f:
    f.write('Con diez cañones por banda\n')
    f.write('viento en popa a toda vela...\n')


lst = [3, 4, 5, 0, 6, 8]
with open('archivos/inverses.txt', 'w') as f:
    for number in lst:
        f.write('{0}\n'.format(1/number))
