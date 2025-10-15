#!/usr/bin/env python3
import sys
__counter = 0


def saludar(nombre):
    return 'Hola, '+ nombre+'!'


def despedir(nombre):
    return 'adios, '+ nombre+'!'


if __name__ == "__main__":
    print("no me ejecutes solo soy un modulo.")
    print(__name__)
    sys.exit(1)
else:
    print("asi sí...")
    print(__name__)

