# Valores iniciales ajustados a tu guía (100 libros iniciales y 100 máximo)
libros_disponibles = 100
MAX_LIBROS_COLECCION = 100
prestamos_netos = 0

ejecucion_biblioteca = True
while ejecucion_biblioteca:
    print("\n--- Control de préstamos de la biblioteca ---")
    print("1. Libros disponibles")
    print("2. Préstamo de libros")
    print("3. Devolución de libros")
    print("4. Historial neto de préstamos y devoluciones de libros")
    print("5. Salir")

    try:
        seleccion = int(input("Ingrese una opción del menú: "))

        match seleccion:
            case 1:
                print(f"\n[LIBROS DISPONIBLES] Cantidad de libros disponibles: {libros_disponibles}")
            
            case 2:
                try:
                    cantidad_prestamos = int(input("Ingrese la cantidad de libros que desea: "))
                    if cantidad_prestamos > 0:
                        if cantidad_prestamos <= libros_disponibles:
                            libros_disponibles -= cantidad_prestamos
                            prestamos_netos += cantidad_prestamos
                            print(f"¡Préstamo autorizado! Se prestaron {cantidad_prestamos} libros.")
                        else:
                            print("¡Error! La solicitud excede las existencias físicas del estante.")
                    else:
                        print("¡Error! Ingrese una cantidad superior a cero.")
                except ValueError:
                    print("¡Error! Debe ingresar un número entero válido para procesar cantidades.")
            
            case 3:
                try:
                    cantidad_devolver = int(input("¿Cuántos libros se están reincorporando?: "))
                    if cantidad_devolver > 0:
                        # Verificamos que no supere el máximo de 100
                        if libros_disponibles + cantidad_devolver <= MAX_LIBROS_COLECCION:
                            libros_disponibles += cantidad_devolver
                            prestamos_netos -= cantidad_devolver
                            print(f"¡Devolución aceptada! {cantidad_devolver} libros regresaron a catálogo.")
                        else:
                            print(f"¡Error! No se puede procesar el ingreso. Supera la capacidad máxima institucional de {MAX_LIBROS_COLECCION} libros.")
                    else:
                        print("¡Error! La cantidad devuelta debe ser mayor a cero.")
                except ValueError:
                    print("¡Error! Debe ingresar un número entero válido para procesar cantidades.")
            
            case 4:
                print(f"\n[HISTORIAL] Balance de préstamos netos de la jornada: {prestamos_netos} libros.")
            
            case 5:
                print("\nGracias por utilizar nuestro software, hasta la próxima.")
                ejecucion_biblioteca = False
                
            case _:
                print("¡Error! Opción fuera de rango. Ingrese números del 1 al 5.")
                
    except ValueError:
        print("¡Error! Debe ingresar un número entero válido para seleccionar una opción.")