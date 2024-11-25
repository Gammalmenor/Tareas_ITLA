#Crear un programa que guarde palabras y luego me diga cuantas
# letras y consonantes contienes esta palabra.
import os
def contar_letras(palabra):
    vocales = "aeiouAEIOU"
    letras = len(palabra)
    consonantes = sum(1 for letra in palabra if letra.isalpha() and letra not in vocales)
    return letras, consonantes

def guardar_palabras():
    palabras = []

    while True:
        palabra = input("Ingrese una palabra (o ingresa 'No' para terminar): ")
        if palabra.lower() == 'no':
            break
        palabras.append(palabra)

    for palabra in palabras:
        letras, consonantes = contar_letras(palabra)
        print(f"La palabra '{palabra}' tiene {letras} letras y {consonantes} consonantes.")
os.system(('cls'))        
print("------------------Programa que cuenta letras y consonantes contienes en una palabra-------------------")
guardar_palabras()
