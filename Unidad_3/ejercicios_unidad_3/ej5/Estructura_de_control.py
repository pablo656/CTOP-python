try:
    edad = int(input("introduce tu edad por favor"));
    if edad <= 18 and edad >= 0:
        print("Eres menor de edad.");
    elif edad >= 18 and edad <= 64:
        print("Eres adulto.");
    elif edad >= 65:
        print("Eres adulto mayor.");
    else:
        print("alienigena sal de aqui.");
except ValueError:
    print("Por favor, ingresa un número válido para la edad.");
except Exception as e:
    print("error acurrido: ",e);

