a = "Hola"
b = input("Llegir paraula: ")

# Mostri caracters de la paraula llegida
for i in b:
    print(i)
# Longitud paraula
print(len(b))

# Comparar-les
if a == b:
    print(f"{a} i {b} són iguals")
else:
    print(f"{a} i {b} no són iguals")

# juntar-les amb un guió
print(a+"-"+b)

# Repetir-la 3 vegades
print(b*3)

# trobar una lletra dins b
if "a" in b:
    print(f"a és dins l'string {b}")
else:
    print("a no hi és")


#llistes mutables-inmutables
lb = [1, "hola", (3, 4), (1, 2)]
print(lb[2])

#modificar una llista, en aquest cas estic afegint
lb.append([100, 200])
print(lb)
#en aquest cas estic afegint més de un element a la llista
lb.extend([100, 200])
print(lb)

