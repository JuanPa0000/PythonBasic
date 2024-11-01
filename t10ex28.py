def majuscules(cadena):
    contador = 0
    for i in cadena:
        if i.isupper():
            contador += 1
    print(f"La cadena de texte té {contador} lletres majúscules")

majuscules("Hola Mundo, me llamo Juan Pablo")

