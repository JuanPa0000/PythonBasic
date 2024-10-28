def calcularEdat():
    edat = int(input("Indiqui la teva edat: "))
    if edat < 18:
        print("Ets menor d'edat")
    elif edat > 18:
        print("Ets major d'edat")
    elif edat == 18:
        print("Tens exactament 18 anys")

calcularEdat()