def media_aritmetica(uno,dos):
    try:
        if type(uno) == int or type(uno) == float and type(dos) == float or type(dos) == int:
            resultado = (uno + dos) / 2
            return resultado
    except Exception as e:
        print("Ocurri un error inesperado: ", e)
        return e;
def media_aritmetica2(*args):
    try:
        for i in args:
            if type(i) != int and type(i) != float:
                return "Error: Todos los argumentos deben ser numeros";
        resultado = sum(args) / len(args)
        return resultado
    except Exception as e:
        print("Ocurri un error inesperado: ", e)
        return e;

print(media_aritmetica(10,20));
print(media_aritmetica2(1,2,3,4,5,6,7,8,9,10));