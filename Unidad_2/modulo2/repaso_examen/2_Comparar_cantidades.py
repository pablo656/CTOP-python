try:
    num1 = int(input("numero entero: "))
    num2 = int(input("otro numero entero: "))
    if isinstance(num1) == int or isinstance(num2) == int:
        if num1 > num2:
            print(f"el numero {num1} es mayor que {num2}")
        elif num2 > num1:
            print(f"el numero {num2} es mayor que {num1}")
        else:
            print("los numeros son iguales")
except ValueError:
    print("Error: Debes ingresar números enteros válidos.")
