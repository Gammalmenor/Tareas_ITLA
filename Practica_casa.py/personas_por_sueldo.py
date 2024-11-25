print("Clasificar a las personas por su sueldo \n")
nombre= input('Dame tu Nombre \n')

sueldo= float(input('Ingrese su sueldo \n'))

if sueldo > 10000 and sueldo < 21000:
    print(f"{nombre} es un operario ")
elif sueldo >= 21000 and sueldo <= 45000:
    print(f'{nombre} es un supervisor ')
elif sueldo > 46000:
    print(f'{nombre} es un gerente general ')
else:
    print(f'{nombre} es un conserge ')
