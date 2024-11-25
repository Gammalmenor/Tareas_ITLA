#Crear un programa que guarde nombre y 
# luego impida guardar nombres repetido
import os
def guardar_nombres():
    nombres = []

    while True:
        nombre = input("Ingrese un nombre \n(o 'no' para terminar): ")
        if nombre.lower() == 'no':
            break
        if nombre in nombres:
            print("El nombre ya existe. \nIntente con otro nombre.")
        else:
            nombres.append(nombre)

    print("\nNombres guardados:")
    for nombre in nombres:
        print(nombre)
print()
os.system('cls')
print("-----------Programa que guarde nombre e impida guardar nombres repetido---------------")
guardar_nombres()