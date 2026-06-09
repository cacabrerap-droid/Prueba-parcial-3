# Ejercicio 1 - Olimpiada programacion

while True:
    try:
        cantidad = int(input("¿Cuántos participantes desea registrar?: "))
        if cantidad > 0:
            break
        else:
            print("¡Cantidad inválida! Debe ingresar un número entero positivo.")
    except ValueError:
        print("¡Cantidad inválida! Debe ingresar un número entero positivo.")

avanzados = 0
iniciales = 0

for i in range(cantidad):
    print(f"\n-- Participante {i+1} --")
    
    while True:
        alias = input("Ingrese el alias del participante: ")
        if len(alias) >= 5 and " " not in alias:
            break
        else:
            print("Alias inválido: Debe tener mínimo 5 caracteres y no contener espacios.")
            
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if edad > 0:
                break
            else:
                print("¡Edad inválida!")
        except ValueError:
            print("¡Edad inválida!")
            
    while True:
        try:
            puntaje = int(input("Ingrese puntaje: "))
            if puntaje > 0:
                break
            else:
                print("¡Puntaje inválido!")
        except ValueError:
            print("¡Puntaje inválido!")
            
    if puntaje >= 70:
        avanzados += 1
    else:
        iniciales += 1

print(f"\nParticipantes avanzados: {avanzados}")
print(f"Participantes iniciales: {iniciales}")