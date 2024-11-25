#Crear un programa que guarde nombres y los organice por tamaño.
import os
def guardar_nombres():
    nombres = []

    while True:
        nombre = input("Ingrese un nombre \n(o 'no' para terminar): ")
        if nombre.lower() == 'no':
            break
        nombres.append(nombre)

    nombres_ordenados = sorted(nombres, key=len)

    print("\nNombres organizados por tamaño:")
    for nombre in nombres_ordenados:
        print(nombre)
os.system('cls')
print("----------------Programa que guarde nombres y los organice por tamaño-----------------")
guardar_nombres()