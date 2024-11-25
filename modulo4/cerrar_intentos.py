print("########Cierre en varios intentos##########")

intentos = 0 
while intentos < 3:
    print("Estoy Abierto")
    cerrar = input("Quieres cerrar? (s/n)").capitalize()
    if cerrar == "S":
        intentos += 1
print("Lograste los tres intentos")
print("\n Ya pudiste cerrar :) \n")