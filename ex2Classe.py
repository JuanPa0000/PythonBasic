p=[]
a = "1"
while a != ".":
    a = input("Introdueix un element: ")
    if a != ".":
        p.append(len(a))
    else:
        print("Adéu")
print(p)
lp = 0
for e in p:
    lp += 1
print(f"La longitud de la llista {p} és de {lp} elements")

"""l=[]
for i in range(4):
    l.append(int(input("Introdueix un número: ")))
print(l)
suma = 0
for e in l:
    suma = suma + e
print(f"La suma de tota la llista {l} és {suma}")
"""
