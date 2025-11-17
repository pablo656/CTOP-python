# Autor: Pablo Ruiz González
# Fecha: 14/11/2025
# Descripción: imprime todos los numeros desde el uno hasta el numero introducido por el usario.
try:
    num1 = int(input("Ingresa un numero: "))
except ValueError:
    print("Error: Debes ingresar numeros enteros.")
    exit()
if num1 >= 0:
    for num2 in range( 1, num1 + 1 ):
        print(num2)
else:
    print("El numero es negativo")