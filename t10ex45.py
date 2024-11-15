def mostrarParells():
    l = [2, 4, 6, 8]
    np = []
    n = input("Introdueix un número: ")
    for i in n:
        if int(i) in l:
            np.append(int(i))
    print(f"Els dígits parells del número {n} són {np}")

mostrarParells()