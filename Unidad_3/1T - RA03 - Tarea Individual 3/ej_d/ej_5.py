# Autor: Pablo Ruiz González
# Fecha: 14/11/2025
# Descripción: imprime suma todos los valores entre el numero 1 al numero un millón.
import time
# esto inicia el contador de tiempo para ver cuanto tarda el programa en ejecutarse
inicio = time.time()
sum2 = 0
for i in range(1,1000001):
    sum2 += i
print(sum2)
# esto termina el contador de tiempo iniciado antes para ver cuanto tarda el programa en ejecutarse
fin = time.time()
print('Tiempo:', fin - inicio, 'segundos')