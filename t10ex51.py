def crearLlistaFitxer():
    with open("fitxer1.txt", "r") as file:
        content = file.read()
    l = content.split(" ")
    return l

print(crearLlistaFitxer())

