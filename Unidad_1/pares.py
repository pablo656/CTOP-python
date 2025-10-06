for i in range(1,21):
    if i % 2 == 0:
        print(f"{i} es par",end=", ")

"""
for i in range(1,21,2):
    print(f"{i} es par",end=", ")
    
pares = [i for i in range(1,21) if i % 2 == 0]
for par in pares:
    print(f"{par} es par",end=", ")
"""