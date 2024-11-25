#Crear un programa que me guarda una lista de comprar
# y me diga precio total de los productos.
import os
def guardar_lista_compras():
    lista_compras = []
    total_precio = 0.0

    while True:
        producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
        if producto.lower() == 'salir':
            break
        precio = float(input(f"Ingrese el precio de {producto}: "))
        lista_compras.append((producto, precio))
        total_precio += precio

    print("\nLista de compras:")
    for producto, precio in lista_compras:
        print(f"{producto}: ${precio:.2f}")

    print(f"\nPrecio total de los productos: ${total_precio:.2f}")
print()
os.system('cls')
print("-------------- Programa de: Lista de comprar y precio total de los productos-------------")
guardar_lista_compras()
