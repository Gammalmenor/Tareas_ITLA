
#PROGRAMA QUE EVALUA EL PERFIL DE UNA PERSONA
#  Y ACUMULA PUNTOS SEGUN VAYA RESPONDIENDO
# PARA APROBAR LA VISA DEBE TENER MINIMO 65 PUNTOS APROBADOS

print("\n############### Entrevista para visado ##################")
nombre = input("Nombre del Interesado: ")
casado = input("Es Casad@? (s/n) ").lower()
trabajo = input("Trabaja actualmente? (s/n) ").lower()
ingresos = int(input("Cuantos son sus Ingrsos Mensuales? "))
puntos = 0
cant_hijos = 0
# PREGUNTA SI ES CASADO Y SI LO ES LE SUMA 30 PUNTOS
# SI NO LE RESTA 5 PUNTOS
if casado == 's':
    puntos += 20
    hijos = input("Tienes hijos? (s/n) ").lower()
    if hijos == "s":
        puntos += 5
        cant_hijos = int(input("Cuantos hijos tienes? "))
else:
    puntos -= 5
if cant_hijos > 1:
    puntos += cant_hijos*3
if trabajo == "s":
    puntos += 20
else:
    puntos -= 5
if ingresos > 20000 and ingresos<=35000:
    puntos += 10
elif ingresos > 40000 and ingresos <= 90000:
    puntos += 20
else:
    puntos -= 10

if puntos >= 65:
    print()
    print(f"Acumulaste {puntos} puntos")
    print(f"Felicidades {nombre}, su visa ha sido aprobada")
    print()
else:
    print()
    print(f"Solo Acumulaste {puntos} puntos")
    print(f"Lo sentimos {nombre}, su visa ha sido negada")
    print()



