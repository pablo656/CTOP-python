import random

# ej 1

estudiantes = ["paco", "ana", "luis"];
print(*estudiantes, sep=" | ");
try:
    estudiantes.append(input("Nombre del estudiante: "));
except ValueError as e:
    print("error: ", e);
estudiantes.pop(0);
estudiantes.sort();
# doble espacio para que se vea bonito
print(*estudiantes, sep=" | ", end="\n \n");

print("-"*20, end="\n \n");



# ej 2
calificaciones = {};
for estudiante in estudiantes:
    # en vez de asignar yo mismo la nota, se asigna con un valor ramdom
    # random coje el primer y ultimo valor de su rango asi que al poner 10 tambien se escoge el 10
    calificaciones[estudiante] = random.randint(0,10);
print("calificación: ", calificaciones.get("ana"));
nota_media = [];
for calificacion in calificaciones.keys():
    print("alumno: ",calificacion,", calificación: " ,calificaciones[calificacion]);
    nota_media.append(calificaciones[calificacion]);

nota = sum(nota_media) / len(nota_media);

print("media nota: ", round(nota,1), end="\n \n");

print("-"*20, end="\n \n");




# ej 3
# pongo el try y except para que al abrir un archivo de texto si no puede
# no de error
try:
    archivo = open("archivo.txt", "w");
    for calificacion in calificaciones.keys():
        #si no pongo str da una excepción.
        archivo.write(calificacion + "-"+ str(calificaciones[calificacion]) + "\n");
    archivo.close();
except FileNotFoundError as e:
    print("error: ", e);
except Exception as e:
    print("error: ", e);