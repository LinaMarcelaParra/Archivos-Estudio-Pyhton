print(" MENU\n======\n")
while True:
    print("Seleccionar una opción:\n")
    print("1: Saludar")
    print("2: Sumar dos numeros")
    print("3: Salir\n")

    user_choice=input()

    if user_choice == "1":
           print("Hola,que tal?")
    elif user_choice == "2":
        n1=float(input("Introduce el primer numero: "))
        n2=float(input("Introduce el segundo numero: "))
        print("El resultado de la suma es: ",n1+n2)
    elif user_choice == "3":
        print("Saliendo del programa!")
        break
    else:
        print("Opción no valida, vuelve a intentralo.\n")
