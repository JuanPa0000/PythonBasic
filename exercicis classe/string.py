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