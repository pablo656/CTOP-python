diccionario = {"nombre": "Juan", "edad": 30, "curso": "phyton"};
print("Mi nombre es", diccionario["nombre"], ", tengo", diccionario["edad"]," años y estoy estudiando", diccionario["curso"]);
for clave, valor in diccionario.items():
    print(f"la clave actual: {clave} y su valor es: {valor}");