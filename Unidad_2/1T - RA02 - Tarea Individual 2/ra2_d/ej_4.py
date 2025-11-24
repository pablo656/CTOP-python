'''
version: erronea.
num = input("Introduce un número: ")
if num % 2 = 0:
print("Es par")
else
    print("Es impar")
'''
# Versión corregida:
#buena practica para manejar errores de entrada
try:
    num = int(input("Introduce un número: "))
    # uso correcto del operador de comparación
    if num % 2 == 0:
        # uso adecuado de la tabulación
        print("Es par")
    else:
        print("Es impar")
except ValueError:
    print("Error: Entrada no válida. Por favor, ingrese un número entero.")
