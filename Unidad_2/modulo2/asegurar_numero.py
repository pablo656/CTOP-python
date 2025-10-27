while True:
    try:
        numero = int(input("Por favor, ingrese un número entero: "))
        break
    except ValueError:
        print("Error: No ingresaste un número entero válido.")

print("numero entero correcto.")