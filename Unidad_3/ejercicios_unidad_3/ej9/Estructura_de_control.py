try:
    numero = int(input("Ingresa un numero: "));
    print("Tabla de multiplicar del ", numero,end=":\n")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
except ValueError:
    print("Error: Debes ingresar un número válido.")
except Exception as e:
    print("Ocurrió un error inesperado: ", e)
