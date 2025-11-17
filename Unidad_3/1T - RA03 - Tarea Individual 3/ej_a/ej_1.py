# Autor: Pablo Ruiz González
# Fecha: 14/11/2025
# Descripción: Calcula cual es el numero mas grande entre los tres numeros ingresados por el usario.
try:
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))
    num3 = int(input("Ingresa otro numero: "))
except ValueError:
    #   comprueba si los datos que el usario a introducido da un error al introducir un valor incorrecto.
    print("Error: Debes ingresar numeros enteros.")
    exit()
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3
print("El numero mayor es: ", mayor)