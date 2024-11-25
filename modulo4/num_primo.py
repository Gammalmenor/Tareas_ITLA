#Programa que valide cual son sus números primos del al 1 al 100
import os
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_hasta_100():
    primos = []
    for num in range(1, 101):
        if es_primo(num):
            primos.append(num)
    return primos

os.system("cls")
print("------------Programa que valide cual son sus números primos------------")
primos = numeros_primos_hasta_100()
print(f"Los números primos del 1 al 100 son: {primos}")