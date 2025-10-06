#!/usr/bin/env python3
import sys
total = 10
def saludar(nombre="", apellido=""):
    return 'Hola, '+ nombre+" "+apellido+'!'

def modificar_total(nuevo_total):
    global total
    total = nuevo_total
    return total


if __name__ == "__main__":
    print("no me ejecutes solo soy un modulo.")
    print(__name__)
    sys.exit(1)
else:
    print("asi sí...")
    print(__name__)