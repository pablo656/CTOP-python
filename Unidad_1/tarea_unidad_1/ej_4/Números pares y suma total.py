contador = int (input("Ingresa el valor N: "))
suma = 0
for i in range (1, contador + 1):
    if i % 2 == 0:
        suma += i
        print("numeros pares "+str(i))
print("La suma de los números pares desde 1 hasta", contador, "es:", suma)
