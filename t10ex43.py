def numero():
    print("El número introduit ha de ser mínim 1 i màxim 20")
    while True:
        n = int(input("Introdueix un número: "))
        if n >= 1 and n <= 20:
            break
    return n

def taula(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")

n = numero()
taula(n)