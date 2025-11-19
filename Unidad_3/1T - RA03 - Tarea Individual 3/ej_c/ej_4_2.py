#original
'''
def area_rectangulo(base, altura):
    area = base ** altura
    return area
base = input('Introduce la base: ')
altura = input('Introduce la altura: ')
area = area_rectangulo(base, altura)
print('El area es: ' area)
'''
def area_rectangulo(base, altura):
    # esto daria un error por que el operador para multiplicar es * y esto exponenciar **
    # tipo de error: error logico
    area = base * altura
    return area
# da error ya que el valor de estas operaciones devuelve un String y no un entero
# tipo de error: ValueError
try:
    base = int(input('Introduce la base: '))
    altura = int(input('Introduce la altura: '))
except ValueError:
    print("Error: Debes ingresar numeros enteros.")
    exit()
area = area_rectangulo(base, altura)
# esta operacion daba error por que no concatenaba dos parametros de diferente tipo
# tipo de error: SyntaxError
print('El area es: ', area)