def paraules():
    n = "0123456789"
    while True:
        p1 = input("Introdueix la primera paraula: ")
        if p1 not in n:
            break
    while True:
        p2 = input("Introdueix la segona paraula: ")
        if p2 not in n:
            break
    return p1, p2

def rimen(p1, p2):
    if p1[-3:] == p2[-3:]:
        print("Si rimen")
    elif p1[-2:] == p2[-2:]:
        print("Rimen un poc")
    else:
        print("No rimen")

print("Aquest programa te indica si dos paraules rimen o no")
p1, p2 = paraules()
rimen(p1, p2)
