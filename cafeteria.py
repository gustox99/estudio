saldo_actual = 150_000
saldo_maximo = 500_000
balance_movimiento = 0

print("\n--- Control de Fondos de Cafeteria Universitaria ---")

ejecutando = True
while ejecutando:
    print("\n=========================")
    print("1. Ver Saldo Actual en Caja")
    print("2. Registrar egreso(Gasto)")
    print("3. Registrar Ingreso (ganancia)")
    print("4. Ver Balance Neto de movimientos")
    print("5.Cerrar caja y salir")
    try:
        opcion_menu = int(input("Ingrese una opción: "))

        if opcion_menu == 1:
            print(f"\n[SALDO ACTUAL] {saldo_actual} pesos")
        elif opcion_menu ==2:
            try:
                gasto = int(input("Ingrese el monto del gasto a registrar: "))
                if gasto > 0:
                    if gasto <= saldo_actual:
                        saldo_actual -= gasto
                        balance_movimiento -= gasto
                        print(f"egreso realizado gasto de {gasto}")
                    else:
                        print("Rechazado, saldo insuficiente!!!")
                else:
                    print("Error el gasto debe ser mayor a cero")
            except ValueError:
                print("Error, ingrese un numero entero positivo")        
        elif opcion_menu == 3:
            try:
                reposicion = int(input("Ingrese el monto a reponer: "))
                if reposicion > 0:

                    if saldo_actual + reposicion <= saldo_maximo:
                        saldo_actual += reposicion
                        balance_movimiento += reposicion
                        print(f"ingreso aprobado se depositaron {reposicion} pesos")
                    else:
                        print(f"Rechazado, esta operacion excede el limite de {saldo_maximo} pesos")    
                else:
                    print("no se puede reponer un numero negativo, solo enteros positivos")
            except ValueError:
                print("Error, solo puede ingresar enteros positivos")
        elif opcion_menu == 4:
            print(f"\n[FLUJO NETO] de movimientos de hoy es {balance_movimiento}")            
        elif opcion_menu == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            ejecutando = False
        else:
            print("Error Ingrese numeros del 1 -5")
    except ValueError:
        print("error, ingrese solo valores numericos")               