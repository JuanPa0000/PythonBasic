def digits():
    print("El número introduit ha de ser mínim 1 i màxim 900000")
    while True:
        n = int(input("Introdueix un número: "))
        if n>=1 and n<=900000:
            break
    return len(str(n))

digits = digits()
print(f"El número introduit té {digits} dígits")