# Ejercicio 2 - Sistema de reservas de salas DUOC

salas_disponibles = 30
salas_reservadas = 0
operaciones_reserva = 0

print("¡Bienvenido al sistema de reservas de salas DUOC!")

while True:
    print("\n--- Menú Principal ---")
    print("1. Salas disponibles")
    print("2. Reservar salas")
    print("3. Liberar salas")
    print("4. Historial")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print(f"\nSalas disponibles actualmente: {salas_disponibles}")
        
    elif opcion == "2":
        try:
            cantidad = int(input("Ingrese la cantidad de salas a reservar: "))
            if cantidad <= 0:
                print("Debe ingresar un número mayor a cero.")
            elif cantidad > salas_disponibles:
                print("No existen salas suficientes.")
            else:
                salas_disponibles -= cantidad
                salas_reservadas += cantidad
                operaciones_reserva += 1
                print("Reserva exitosa.")
        except ValueError:
            print("Debe ingresar un número entero.")
            
    elif opcion == "3":
        try:
            cantidad = int(input("Ingrese la cantidad de salas a liberar: "))
            if cantidad <= 0:
                print("Debe ingresar un número entero positivo.")
            elif cantidad > salas_reservadas:
                print("Error: Intenta liberar más salas de las que están reservadas.")
            else:
                salas_disponibles += cantidad
                salas_reservadas -= cantidad
                print("Salas liberadas exitosamente.")
        except ValueError:
            print("Debe ingresar un número entero positivo.")
            
    elif opcion == "4":
        print(f"\nTotal de salas reservadas actualmente: {salas_reservadas}")
        print(f"Total de operaciones de reserva realizadas durante la sesión: {operaciones_reserva}")
        
    elif opcion == "5":
        print("\nGracias por utilizar el sistema.")
        break
        
    else:
        print("Opción no válida. Intente de nuevo.")