#daba error por que no se habia puesto los : haciendo que no entendiera que era una función y que lo siguiente era su bloque de codigo.
#tipo de error: SyntaxError
def area_rectangulo(base, altura):
    area = base * altura
    # esta operacion daba error por que no concatenaba dos parametros de diferente tipo
    # tipo de error: SyntaxError
    print('El area es: ',area)
# da error ya que el valor de estas operaciones es un String y no un entero
# tipo de error: ValueError
try:
    base = int(input('Introduce la base: '))
    altura = int(input('Introduce la altura: '))
except ValueError:
    print("Error: Debes ingresar numeros enteros.")
    exit()
area_rectangulo(base, altura)

