ladrillos_a = 0
ladrillos_b = 0

# 1. Bandera para el ciclo de la cantidad inicial
pidiendo_cantidad = True

while pidiendo_cantidad:
    try:
        cantidad = int(input("Ingrese la cantidad de ladrillos a analizar: "))
        if cantidad > 0:
            pidiendo_cantidad = False  # <--- Reemplaza al break
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")


# Inicia el procesamiento por lotes
for i in range(cantidad):
    print(f"\n--- Escaneo de ladrillo {i + 1} ---")

    # 2. Bandera para el ciclo del código
    pidiendo_codigo = True
    
    while pidiendo_codigo:
        codigo = input("Ingrese el codigo del lote del ladrillo: ")
        if len(codigo) >= 5 and " " not in codigo:
            pidiendo_codigo = False  # <--- Reemplaza al break
        else:
            print("Error, debe tener al menos 5 caracteres y no tener espacios")

    # 3. Bandera para el ciclo de la resistencia
    pidiendo_resistencia = True
    
    while pidiendo_resistencia:
        try:
            resistencia = int(input("Ingrese la resistencia del ladrillo (MPa): "))
            if resistencia > 0:
                pidiendo_resistencia = False  # <--- Reemplaza al break
            else:
                print("Error logístico! Ingresa un número entero positivo para la resistencia.")
        except ValueError:
            print("Error logístico! Ingresa un número entero positivo para la resistencia.")   

    # Clasificación (fuera de los while de validación, pero dentro del for)
    if resistencia > 15:
        ladrillos_a += 1             
    else:
        ladrillos_b += 1


# Despliegue final
print(f"\n¡El control ha finalizado con {ladrillos_a} ladrillos CLASE A y {ladrillos_b} ladrillos CLASE B! ¡Lote procesado!")