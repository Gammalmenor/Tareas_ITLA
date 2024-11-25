print ('contraseña es segura \n')


while True:
    print('Crea una contraseña nueva')
    contrasena=input()

    if len(contrasena) < 8:
        print("Contraseña insegura, debe tener minimo 8 caracteres (@/.)")
    else:
        if (( not "@" in contrasena) and (not "." in contrasena)):
            print("Contraseña insegura, debe tener caracteres especiales")
        else:
            print("Contraseña es segura ")
            break
