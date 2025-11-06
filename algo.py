for i in range(1, 21,1):
    tipo = "par" if i % 2 == 0 else "impar"
    print(f"{i} es {tipo}", end=", ")