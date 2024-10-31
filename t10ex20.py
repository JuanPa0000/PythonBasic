def noSpace(texte):
    texteSinEspais = ""
    for i in texte:
        if i != " ":
            texteSinEspais = texteSinEspais + i
    return texteSinEspais

def reverse(texteSinEspais):
    nouTexte = ""
    for i in texteSinEspais:
        nouTexte = i + nouTexte
    return nouTexte

def es_palindrom(texte):
    texte = noSpace(texte)
    texte_al_reves = reverse(texte)
    return texte == texte_al_reves

print(es_palindrom("amo la paloma"))
print(es_palindrom("juan pablo"))
    