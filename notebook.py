notebooks_disponibles = 40
notebooks_max = 40
ejecutando = True
balance_neto = 0
print("\n--- Gestión de Préstamo de Notebooks - Laboratorio ---")
while ejecutando:
    print("1.Equipos disponibles")
    print("2.Prestar Notebooks")
    print("3.Devolver Notebooks")
    print("4.Historial neto de prestamos")
    print("5.Salir")

    try:
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            print(f"equipos disponibles: {notebooks_disponibles} ")
        elif opcion == 2:
            try:
                cantidad = int(input("Ingrese la cantidad de notebooks que desea: "))
                if cantidad > 0:
                    if cantidad <= notebooks_disponibles:
                        notebooks_disponibles -= cantidad
                        balance_neto += cantidad
                        print(f"Notebooks prestados: {cantidad} ")
                    else:
                        print("Error, no hay cantidad de notebooks suficientes")
                else:
                    print("Error, ingrese un numero entero positivo")
            except ValueError:
                print("Error, ingrese dato válido")
        elif opcion == 3:
            try:
                cantidad = int(input("Ingrese la cantidad de notebooks a devolver: "))
                if cantidad > 0:
                    if cantidad + notebooks_disponibles <= notebooks_max:
                        notebooks_disponibles += cantidad
                        balance_neto -= cantidad
                        print(f"notebooks devueltos: {cantidad} ")
                    else:
                        print(f"Error, supera a la cantidad maxima: {notebooks_max} ")
                else:
                    print("Error, ingrese un numero entero positivo")
            except ValueError:
                print("Error, ingrese dato válido")
        elif opcion == 4:
            print(f"Historial neto: {balance_neto} ")
        elif opcion == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            ejecutando = False
        else:
            print("Error, ingrese numero del 1 al 5")
    except ValueError:
        print("Error, ingrese dato válido")                    



