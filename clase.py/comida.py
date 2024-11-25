comida = []
while True:
    comida= input('ingrese la comida')
    if comida == 'n':
        break
    else:
        comida.append (comida)

for comida in comida:
    print(comida)

