def noms_que_comencen_per(noms, char):
    llistaNoms = []
    for i in noms:
        if i[0].lower() == char:
            llistaNoms.append(i)
    return llistaNoms

print(noms_que_comencen_per(["Antonio", "Joan", "Pablo", "Aris", "Pep"], "a"))
