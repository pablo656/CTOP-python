try:
    palabras = input("Ingresa una frase: ");
except Exception as e:
    print("Ocurrió un error inesperado: ", e)
contador = 0;
for palabra in palabras:
    contador+= 1;
print("El total de caracteres es: ", contador);