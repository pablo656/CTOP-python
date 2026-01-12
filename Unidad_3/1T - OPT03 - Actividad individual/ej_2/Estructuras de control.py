try:
    num1 = int(input("Ingresa un numero entre 5 y 12: "));
    if (num1 < 12 and num1 > 5):
        print("Tabla de multiplicar de ", num1);
        for i in range(1,11,1):
                print(i," x ",num1," = ", num1*i);
    else:
        print(f"El numero {num1} no es valido")
except ValueError:
    print("El numero ingresado no es valido");
