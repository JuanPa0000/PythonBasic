def hiHaDuplicats(l):
    if l == list(set(l)):
        print(f"En la llista {l} no hi ha elements duplicats")
    else:
        print(f"En la llista {l} si hi ha elements duplicats")

hiHaDuplicats([1, 2, 3, 2, 4, 5])
hiHaDuplicats([1, 2, 3, 4, 5, 6])

