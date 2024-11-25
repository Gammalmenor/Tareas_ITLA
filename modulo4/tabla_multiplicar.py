print("Tabla de multiplicar")

numero = int(input("Dame un numero para darte la tabla:\n"))
print(f"Esta es la tabla del {numero}\n")
for n in range(1,13):
    print(f"{numero} x {n} = {numero*n}")
print("\nHasta luego !!!\n")