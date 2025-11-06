frutas = ["coco", "mango", "fresa", "pera", "manzana"]
for i in range (len(frutas)):
    if i == 0:
        print(frutas[i]," es la primera fruta de la lista")
    elif i == len (frutas) -1:
        print(frutas[i]," es la ultima furta de la lista")
frutas.append("kiwi")
print("Lista de frutas actualizada:", frutas)