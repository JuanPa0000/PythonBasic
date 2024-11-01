def filtrar_paraules(llista, letres):
    novaLlista = []
    for i in llista:
        if len(i) > letres:
            novaLlista.insert(0, i)
    print(f"Les paraules que tenen més de {letres} són {novaLlista}")

filtrar_paraules(["Juan", "Pablo", "Amistad", "escribir", "si"], 5)

#Aquesta és la segona forma de fer-ho, i que no doni el resultat com una llista (Ho he fet per provar)
# def filtrar_paraules2(llista, letres):
#     paraules = ""
#     for i in llista:
#         if len(i) > letres:
#             paraules = paraules + i + " "
#     print(f"Les paraules que tenen més de {letres} són {paraules}")

# filtrar_paraules2(["Juan", "Pablo", "Amistad", "escribir", "si"], 5)