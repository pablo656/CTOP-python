#!/usr/bin/env python3
import sys
def sumar(a,b):
    resultado = a + b
    print("suma igual  "+str(resultado))
    return resultado


def restar(a,b):
    resultado = a - b
    print("resta igual a " + str(resultado))
    return resultado

def multiplicacion(a,b):
    resultado = a * b
    print("multiplicacion igual a " + str(resultado))
    return resultado

def division(a,b):
    resultado = a / b
    print("division igual a " + str(resultado))
    return resultado

if __name__ == "__main__":
    print("no me ejecutes solo soy un modulo.")
    print(__name__)
    sys.exit(1)
else:
    print("asi sí...")
    print(__name__)