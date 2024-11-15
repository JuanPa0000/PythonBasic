while True:
    entrada = input("Introdueix un número: ")
    entrada = int(entrada)
    if entrada <= 100:
        break

ln = []
resultat = 0
n = entrada
for i in range(int(entrada/4)):
    n = n - 4
    ln.append(str(n)+"**2")
    resultat = resultat + n**2

print("llista:" + str(ln))
print(f"El resultat de la suma dels quadrats és: {resultat}")



