def entrada():
    while True:
        cInicial = input("Introdueix la quantitat a sol.licitar: ")
        if int(cInicial) >= 50000 and int(cInicial) <= 800000:
            break
    while True:
        interes = input("Introdueix un interés: ")
        if float(interes) >= 0.5 and float(interes) <= 13:
            break
    while True:
        anys = input("Introdueix el número d'anys: ")
        if int(anys) >= 3 and int(anys) <= 40:
            break
    return cInicial, interes, anys

def cFinal(cInicial, interes, anys):
    cFinal = int(cInicial) * (1 + float(interes)/100) ** int(anys)
    return round(cFinal)

print("Aquest programa calcula el capital final d'una inversió amb interessos")
print("Hauràs d'introduir:")
print("- Capital inicial (50,000€ a 800,000€)")
print("- Interès anual (0.5% a 13%)")
print("- Anys de durada (3 a 40 anys)")
print("\n")
cInicial, interes, anys = entrada()
Cfinal = cFinal(cInicial, interes, anys)
print("\n")
print(f"{cInicial} a {interes}% d'interés en {anys} anys s'ha de convertir en {Cfinal}€")