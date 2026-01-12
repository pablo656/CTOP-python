def media():
    try:
        num1 = int(input("Ingresa un numero: "));
        num2 = int(input("Ingresa un numero: "));
        print(f"media de {num1} y {num2} es:",(num1 + num2)/2);
    except ValueError:
        print("El numero ingresado no es valido");
media();