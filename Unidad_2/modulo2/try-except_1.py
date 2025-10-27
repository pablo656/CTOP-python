texto = ""
try:
    f = open("archivo.txt", "r")
    #texto = f.read()
    f.write("hola, ke hase")
except IOError as e:
    print("Ocurrió un error:", e)
else:
    print("Fichero escribido correctamente")
finally:
    f.close()