def llistaNombre():
    l = []
    for i in range(4):
        l.append(int(input("Introdueix una llista de números: ")))
    return l

def sumaLlista(l):
    suma = 0
    for i in l:
        suma += i
    return suma

def funcioPrincipal():
    l = llistaNombre()
    suma = sumaLlista(l)
    print(l)
    print(f"La suma de la llista {l} és {suma}")
    print(f"La llista invertida és {l[::-1]}")
    print(l[-2:])

funcioPrincipal()
