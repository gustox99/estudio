correos_institucionales = 0
correos_no_institucionales = 0
cantidad_valida = False
total_correos = 0

while not cantidad_valida:
    try:
        total_correos = int(input("Ingrese la cantidad de corros que desea validar: "))
    except ValueError:
        print("Error, ingrese un dato valido")
    else:#cantidad_valida = total_correos > 0
        if total_correos > 0:
            cantidad_valida = True
#retorna
for i in range(total_correos):
    correo_valido = False
    while correo_valido == False:
        correo = input("Ingrese el correo: ").strip().lower()
        #correo_valido = "@" in correo and " " not in correo and len(correo) >=6
        if "@" in correo and " " not in correo and len(correo) >= 6:
            correo_valido = True
        else:
            print("correo no valido")
    es_institucional = correo.endswith("duoc.cl")

    if es_institucional:
        correos_institucionales +=1
    else:
        correos_no_institucionales +=1

print(f"La cantidad de correos no institucionales es : {correos_no_institucionales}")
print(f"La cantidad de correos  institucionales es : {correos_institucionales}")







