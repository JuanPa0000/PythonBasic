import random

def llista20Elements():
    l = []
    for i in range(20):
        l.append(random.randint(1, 100))
    return l

def hiHaDuplicats(l):
    if l == list(set(l)):
        print(f"En la llista {l} no hi ha elements duplicats")
    else:
        print(f"En la llista {l} si hi ha elements duplicats")

l = llista20Elements()
hiHaDuplicats(l)