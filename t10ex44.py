def entrada():
    while True:
        n = int(input("Introdueix un número: "))
        if type(n) == int:
            break
    return n

def retornarDigits(n):
    return len(str(n))

def parell(dn):
    if dn%2 == 0:
        print("Es parell")
    else:
        print("És senar")

n = entrada()
dn = retornarDigits(n)
parell(dn)
    