# Programa: EcoRide - Alquiler de Bicicletas Eléctricas
print(" Bienvenido a EcoRide GreenCity ")

continuar = True

while continuar:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Alquilar bicicleta")
    print("2. Consultar tarifas")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        print("\nTipos de bicicleta:")
        print("1. Estándar ($0.5 por minuto)")
        print("2. Premium ($0.8 por minuto)")

        tipo = input("Selecciona el tipo (1 o 2): ")
        
        if tipo == "1":
            tipo_bici = "Estándar"
            tarifa = 0.5
        elif tipo == "2":
            tipo_bici = "Premium"
            tarifa = 0.8
        else:
            print("Opción inválida.")
            continue

        # Tiempo de uso
        while True:
            try:
                minutos = int(input("Ingresa el tiempo de uso (minutos): "))
                if minutos <= 0:
                    print("El tiempo debe ser mayor a 0.")
                else:
                    break
            except ValueError:
                print("Por favor ingresa un número válido.")

        # Método de pago
        metodo = input("Método de pago (efectivo / tarjeta / puntos): ").lower()
        if metodo not in ["efectivo", "tarjeta", "puntos"]:
            print("Método de pago inválido.")
            continue

        # Día de la semana
        fin_semana = input("¿Es sábado o domingo? (si/no): ").lower() == "si"

        # Devolución fuera de tiempo
        fuera_tiempo = input("¿Devolvió la bicicleta fuera de" \
        "l tiempo? (si/no): ").lower() == "si"

        # Cálculo del costo
        costo_base = tarifa * minutos
        descuento = 0
        penalizacion = 0
         
        # Descuentos
        if minutos > 60 and metodo == "tarjeta":
            descuento += costo_base * 0.10  # 10% por tiempo y tarjeta
        elif minutos < 10 and metodo == "puntos":
            descuento += 0  # sin descuento
       
        # Descuento fin de semana
        if fin_semana:
            descuento += costo_base * 0.05  # 5% de descuento

        # Penalización
        if fuera_tiempo:
            penalizacion = 5.0

        total = costo_base - descuento + penalizacion

        # Mostrar resumen
        print("\n--- RESUMEN DEL SERVICIO ---")
        print(f"Tipo de bicicleta: {tipo_bici}")
        print(f"Tiempo de uso: {minutos} minutos")
        print(f"Costo base: ${costo_base:.2f}")
        print(f"Descuento total: -${descuento:.2f}")
        print(f"Penalización: +${penalizacion:.2f}")
        print(f"TOTAL A PAGAR: ${total:.2f}")

    elif opcion == "2":
        print("\n--- TARIFAS ---")
        print("Estándar: $0.5 por minuto")
        print("Premium : $0.8 por minuto")

    elif opcion == "3":
        print("\nGracias por usar EcoRide. ¡Hasta pronto! ")
        continuar = False
    else:
        print("Opción inválida.")

    # Preguntar si desea continuar
    if continuar:
            seguir = input("\n¿Deseas realizar otra operación? (si/no): ").lower()
            if seguir != "si":
                continuar = False
                print("¡Gracias por usar EcoRide! ")
# Fin del programa EcoRide.py


