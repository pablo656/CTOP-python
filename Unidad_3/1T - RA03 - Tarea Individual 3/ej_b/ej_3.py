# Autor: Pablo Ruiz González
# Fecha: 14/11/2025
# Descripción: permite calculcular la suma, resta, división y multiplicación de dos numeros introducidos por el usario.
try:
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))
    operaciones = input("Ingrese una de estas operaciones +,-,*,/: ")
except ValueError:
    print("Error: Debes ingresar numeros enteros.")
    exit()
if operaciones == "+":
    resultado = num1 + num2
    print("El resultado de la suma es: ", resultado)
elif operaciones == "-":
    resultado = num1 - num2
    print("El resultado de la resta es: ", resultado)
elif operaciones == "*":
    resultado = num1 * num2
    print("El resultado de la multiplicacion es: ", resultado)
elif operaciones == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado de la division es: ", resultado)
    else:
        #   comprueba que el numero del divisor introducido por el usuario no sea 0 para que no de error.
        print("Error: No se puede dividir entre cero.")
else:
    print("Error: Operacion no valida.")