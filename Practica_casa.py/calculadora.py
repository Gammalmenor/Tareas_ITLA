def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero no permitida"

print("Selecciona operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

while True:
    eleccion = input("Introduce tu elección (1/2/3/4): ")

    if eleccion in ('1', '2', '3', '4'):
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if eleccion == '1':
            print(f"{num1} + {num2} = {suma(num1, num2)}")

        elif eleccion == '2':
            print(f"{num1} - {num2} = {resta(num1, num2)}")

        elif eleccion == '3':
            print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")

        elif eleccion == '4':
            print(f"{num1} / {num2} = {division(num1, num2)}")
        
        siguiente_calculo = input("¿Quieres realizar otra operación? (sí/no): ")
        if siguiente_calculo.lower() != 'sí':
            break
    else:
        print("Entrada no válida")

print("¡Gracias por usar la calculadora!")