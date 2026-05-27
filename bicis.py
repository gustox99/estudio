bicis_disponibles = 100
bicic_max = 100
balance_neto = 0

ejecutando = True
while ejecutando:
    print("1. bicis disponibles")
    print("2. arrendar bicis(egreso)")
    print("3. devolver bicis(ingreso)")
    print("4. Ver Balance neto de bicicletas de la jornada")
    print("5.Salir")

    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            print(f"Hay un total de {bicis_disponibles} bicis disponibles")
        elif opcion == 2:
            try:
                cantidad = int(input("Ingrese la cantidad de bicis que quiere arrendar: "))
                if cantidad > 0:
                    if cantidad <= bicis_disponibles:
                        bicis_disponibles -= cantidad
                        balance_neto += cantidad
                        print("Bicicletas arrendadas!!!")
                    else:
                        print("Error, maximo de bicicletas para arrendar 100")
                else:
                    print("Error, ingrese un numero entero positivo")
            except ValueError:
                print("Error, ingrese un dato valido")
        elif opcion == 3:
            try:
                cantidad = int(input("Ingrese las bicis que desea devolver"))

                if cantidad > 0:
                    if cantidad + bicis_disponibles <= bicic_max:
                        bicis_disponibles += cantidad
                        balance_neto -= cantidad
                        print("Bicicletas devueltas")
                    else:
                        print("Error no puede devolver mas que la capacidad maxima")
                else:
                    print("Ingrese un numero entero positivo")
            except ValueError:
                print("Ingrese un dato valido")  
        elif opcion == 4:
            print(f"balance neto del dia:  {balance_neto}")
        elif opcion == 5:
            print("Gracias por usar nuestro sosftware!!!")
            ejecutando = False
        else:
            print("Error ingrese una opcion del 1 al 5")
    except ValueError:
        print("Error, ingrese un dato valido")                                                                     