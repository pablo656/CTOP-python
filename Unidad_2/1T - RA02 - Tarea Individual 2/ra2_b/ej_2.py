try:
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        print("El número ",num," es par.")
    else:
        print("El número", num,"es impar.")
except ValueError:
    print("Error: Entrada no válida. Por favor, ingrese un número entero.")