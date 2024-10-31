def multLlista(llista):
    resultat = llista[0]
    for i in llista[1:]:
        resultat = resultat * i
    print(resultat)

def sumarLlista(llista):
    resultat = 0
    for i in llista:
        resultat = resultat + i
    print(resultat)

sumarLlista([2, 5, 7])
multLlista([8, 3])




