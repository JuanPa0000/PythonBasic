def binari_a_enter(binari):
    for a in str(binari):
        if int(a) > 1:
            print("Numero binari incorrecte, torna a escriure bé")
            exit()
    char = len(str(binari)) - 1
    enter = 0
    for i in str(binari):
        enter = enter + int(i) * 2**char
        char -= 1
    return enter
     
print(binari_a_enter(1010111))
print(binari_a_enter(11001))
print(binari_a_enter(101))

