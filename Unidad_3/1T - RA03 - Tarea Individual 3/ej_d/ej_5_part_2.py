# Autor: Pablo Ruiz González
# Fecha: 14/11/2025
# Descripción: imprime la suma todos los numeros desde el uno hasta el numero introducido por el usario.
import time
inicio = time.time()
sum2 = sum(range(1,1000001))
print(sum2)
fin = time.time()
print('Tiempo:', fin - inicio, 'segundos')