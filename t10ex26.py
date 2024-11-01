def paraula_mes_llarga(llista):
    paraulaLlarga = llista[0]
    for i in llista:
        if len(i) > len(paraulaLlarga):
            paraulaLlarga = i
    print(paraulaLlarga)
        

paraula_mes_llarga(["juan", "papa", "espejo", "luz", "corazón"])