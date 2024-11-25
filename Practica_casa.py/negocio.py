
#Variables
print("\n___________________BIENVENIDO_________________")
salario = 20000.00

#Ciclo para evaluar si quieres nodificar el salario
while True:
    print(f"\nSu salario regular es de {salario} Pesos")
    cambiar = input("\nQuieres cambiarlo? (s/n)")
    if cambiar == "s" or cambiar == "S":
        salario_nuevo = float(input("\nIntroduce el valor del nuevo saldo:  "))
        salario = salario_nuevo
        break
    elif cambiar == "n" or cambiar == "N":
        print(f"\n OK, Su salario sigue siendo: {salario} Pesos")
        break
    else: 
       
        print(f"\n\033[31mPerdone, debe elegir una opcion (s/n)\033[0m")
#sacar el valor de las variables impuesto,seguro,pension, etc.   
impuesto = round(salario*0.18)
seguro = round(salario*0.05)
pension = round(salario*0.07)
total_desc = round(impuesto+seguro+pension)
saldo = salario - total_desc

print()
print(f"""

     ____________Deducible__________________  
    |              |            |           |
    |Sueldo Inicial| Descuentos |Total      |
    |Sueldo Neto   |            |{salario}      
    |              | Impuesto   |{impuesto} 
    |              | Seguro     |{seguro}   
    |              | Pension    |{pension}  
    |              | Total Desc.|{total_desc}
    |Saldo Final   |            |{saldo}    
    ________________________________________
    

""")
print()

