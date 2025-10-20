edad = -20;
while(edad < 1 or edad > 120):
    edad = int(input("Ingrese su edad (1-120): "));
    if(edad < 1 or edad > 120):
        print("Edad invalida, intente de nuevo.");
    elif(edad < 15):
        print("Eres niño.");
    elif(edad >= 15 and edad <= 21):
        print("Eres adolescente.");
    elif(edad > 21 and edad < 35):
        print("Eres joven.");
    elif(edad >= 35 and edad < 50):
        print("Eres maduro/a.");
    elif(edad >= 50 and edad < 60):
        print("Eres de mediana edad.");
    elif(edad > 61 and edad <= 80):
        print("Eres mayor.");
    elif(edad > 81 and edad <= 100):
        print("Eres viejo/a.");
    elif(edad > 100):
        print("Eres centenario/a.");


