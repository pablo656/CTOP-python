if __name__ != '__main__':
    def suma(a, b):
        return a + b

    def resta(a, b):
        return a - b

    def multiplicacion(a, b):
        return a * b

    def division(a, b):
        if b == 0:
            return "Error: División por cero"
        return a / b
else:
    print("Este módulo no se puede ejecutar directamente.")
    exit();