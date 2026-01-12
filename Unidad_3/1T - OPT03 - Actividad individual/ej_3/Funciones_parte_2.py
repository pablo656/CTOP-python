def media(*args):

    result = 0;
    for num in args:
        result += num ;
    try:
        result /= len(args);
        return result;
    except ZeroDivisionError:
        return "error";

media();
try:
    num1 = int(input("Ingresa un numero: "));
    num2 = int(input("Ingresa un numero: "));
    num3 = int(input("Ingresa un numero: "));
    media2 = media(num1 ,num2 ,num3);
    print("la media es: ", media2);
except ValueError:
    print("El numero ingresado no es valido");

