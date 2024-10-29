def calcularLongitud():
    llista = input("Escriu un texte o llista: ")
    long = 0
    for i in llista:
        long = long + 1
    print(f"La longitud del texte o llista és de {long} caràcters")

calcularLongitud()