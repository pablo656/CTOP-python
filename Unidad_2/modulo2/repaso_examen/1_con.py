import time as t

contador = int(input("Ingresa un número entero positivo para iniciar la cuenta regresiva: "))
if contador < 50 and contador > 5:
    for i in range(contador, 0, -1):
        print(i)
        t.sleep(0.5)
    print("termino")
else:
    print("El número ingresado es demasiado grande para una cuenta regresiva segura.")
