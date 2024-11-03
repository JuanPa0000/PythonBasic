def es_de_traspas(any):
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        print(f"L'any {any} si és de traspàs")
    else:
        print(f"L'any {any} no és de traspàs")

es_de_traspas(2013)
