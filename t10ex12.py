def menu():
    op = 0
    print("Menu")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sortir")

    op = int(input("Introdueixi una opció: "))
    return op

def sumar():
    a = int(input("Introdueixi el primer element: "))
    b = int(input("Introdueixi el segon element: "))
    c = a + b
    print("El resultat de restar {} menys {} és {}".format(a, b, c))
def restar():
    a = int(input("Introdueixi el primer element: "))
    b = int(input("Introdueixi el segon element: "))
    c = a - b
    print("El resultat de restar {} menys {} és {}".format(a, b, c))
def multiplicar():
    a = int(input("Introdueixi el primer element: "))
    b = int(input("Introdueixi el segon element: "))
    c = a * b
    print("El resultat de multiplicar {} menys {} és {}".format(a, b, c))
def dividir():
    a = int(input("Introdueixi el primer element: "))
    b = int(input("Introdueixi el segon element: "))
    c = a / b
    print("El resultat de dividir {} menys {} és {}".format(a, b, c))

while True:
    op = menu()
    match op:
        case 1:
            sumar()
        case 2:
            restar()
        case 3:
            multiplicar()
        case 4:
            dividir()
        case 5:
            print("Adeu, gracies per haver utilitzat aquest programa")
            break