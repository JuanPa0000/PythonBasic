def gran():
    n1 = int(input("Introdueix un nombre: "))
    n2 = int(input("Introdueix el segon nombre: "))
    n3 = int(input("Introdueix el tercer nombre: "))
    if n1 > n2 and n1 > n3:
        print(f"El nombre més gran és {n1}")
    elif n2 > n1 and n2 > n3:
        print(f"el nombre més gran és {n2}")
    else:
        print(f"El nombre més gran és {n3}")

gran()