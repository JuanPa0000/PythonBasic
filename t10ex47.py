def estaOrdenada(l):
    if l == sorted(l):
        print(f"La lista {l} està ordenada de forma ascendent")
    elif l == sorted(l, reverse=True):
        print(f"La lista {l} està ordenada de forma descendent")
    else:
        print(f"la lista {l} està desordenada")

estaOrdenada([1, 2, 3, 4, 5])
estaOrdenada([5, 4, 3, 2, 1])
estaOrdenada([1, 4, 2, 6, 9])
