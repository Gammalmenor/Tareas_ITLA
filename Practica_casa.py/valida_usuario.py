print("\n ************LOGIN******************** ")

while True:
    print("Introduce Nombre")
    nombre = input()
    print("Introduce la contrasena")
    contrasena = input()
    if contrasena != "123456" or nombre != "gammal":
        print(f"\033[31m Lo sentimo {nombre}, al parecer tu contrasena o nombre no estan registrados, Vuelva a intentar...\033[0m")
    else:
        print(f"""
              _________________________________________
                        BIENVENIDO A MI PORTAL
              _________________________________________

              Hola: {nombre}, has entrado a mi portal
              _________________________________________

                                _                  __
                     ____ ___  (_)  ________  ____/ /
                    / __ `__ \/ /  / ___/ _ \/ __  /
                   / / / / / / /  / /  /  __/ /_/ /
                  /_/ /_/ /_/_/  /_/   \___/\__,_/
              
              """)
        break