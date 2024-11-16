np = []
for n in range(1, 101):
    noDivisor = []
    for i in range(2, n):
        if n % i != 0:
            noDivisor.append("-")
        else:
            noDivisor.append(".")
    if ("." not in noDivisor) and n > 1:
        np.append(n)

print(f"""Los números primos que hay entre 1 y 100 són:
{np}""")
print(f"En total hay {len(np)} números primos")

