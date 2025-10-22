num1 = input("Ingresa un numero: ")
num2 = input("Ingresa otro numero: ")
if(float(num1) > float(num2)):
    print("El numero mayor es: " + num1)
elif(float(num2) > float(num1)):
    print("El numero mayor es: " + num2)
else:
    print("Los numeros son iguales.")