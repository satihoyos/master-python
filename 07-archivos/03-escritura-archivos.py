f = open('archivos/mi_texto.txt', 'w')
f.write('con cien canones por banda \n')
f.write('viento en popa a toda vela \n')
f.close()

l = range(50)
h = open('archivos/lista_numeros.txt', 'w')
for x in l:
    h.write('{0}\n'.format(x))
h.close()