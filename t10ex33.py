def noms_que_comencen_per(noms, char):
    if len(char) != 1:
        print("Introdueix solament un caràcter")
        exit()
    llistaNoms = []
    for i in noms:
        if i[0].lower() == char:
            llistaNoms.append(i)
    return llistaNoms

char = input("Introdueix una lletra: ")
print(noms_que_comencen_per(["Antonio", "Joan", "Pablo", "Aris", "Javier"], char))