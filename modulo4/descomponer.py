print("##########Descomponer una oracion en letras##########")

oracion = input("Escribe la oracion que quieres descomponer \n")
print(f"Oracion Original: {oracion}")
new = oracion.split(sep=" ")
new.reverse()
oracion = new
print("Oracion descompuesta:",end=" ")
for palabra in oracion:
    print(palabra,end=" ")