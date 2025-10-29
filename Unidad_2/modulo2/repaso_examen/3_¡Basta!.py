hola = ""
array = []
while hola != "basta":
    hola = input("Escribe 'basta' para detener el bucle: ")
    hola = hola.lower()
    array.append(hola)
    for x in array:
        print(x, end=", ")
    print()
print("¡Has salido del bucle!")