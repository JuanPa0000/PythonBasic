def llegirLlista():
    l = []
    a = ""
    while a != ".":
        a = input("Introdueix una paraula: ")
        if a != ".":
            l.append(a)
        else:
            print("\n")
    return l

def repetits(l):
    a = False
    count = 1
    for i in l:
        if i in l[count:]:
            a = True
        count += 1
    return a


l = llegirLlista()
a = repetits(l)
if a == True:
    print("Si hi ha paraules repetides")
else:
    print("No hi ha paraules repetides")

