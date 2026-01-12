from operator import is_not

diccionario = {
    "alum1" : {
    "nombre":"pablo",
    "edad":20,
    "estudiantes": True
    },
    "alum2" : {
    "nombre":"adrian",
    "edad":18,
    "estudiantes": True
    }
}
for i in diccionario:
    nombre =diccionario[i]["nombre"]
    edad = diccionario[i]["edad"]
    if( edad <= 0 ):
        print("El edad no es valido")
    elif(edad < 18):
        print(f"{nombre}:eres menor de edad")
    elif(edad <= 25):
        print(f"{nombre}:eres muy joven")
    elif(edad <= 40):
        print(f"{nombre}:eres mas joven")
    else:
        print(f"{nombre}:ya no eres jovem")