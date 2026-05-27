ladrillos_a = 0
ladrillos_b = 0

while True:
    try:
        cantidad = int(input("Ingrese la cantidad de ladrillos a analizar: "))
        if cantidad > 0:
            break
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")



for i in range(cantidad):
    print(f"Escaneo de ladrillo {i + 1} ")

    while True:
        codigo = input("Ingrese el codigo del lote del ladrillo: ")
        if len(codigo) >= 5 and " " not in codigo:
            break
        else:
            print("Error, debe tener al menos 5 caracteres y no tener espacios")

    while True:
        try:
            resistencia = int(input("Ingrese la resistencia del ladrillo: "))
            if resistencia > 0:
                break
            else:
                print("Error logístico! Ingresa un número entero positivo para la resistencia.")
        except ValueError:
            print("Error logístico! Ingresa un número entero positivo para la resistencia.")   

    if resistencia > 15:
        ladrillos_a +=1             
    else:
        ladrillos_b +=1


print(f"¡El control ha finalizado con {ladrillos_a} ladrillos CLASE A y {ladrillos_b} ladrillos CLASE B! ¡Lote procesado!")
