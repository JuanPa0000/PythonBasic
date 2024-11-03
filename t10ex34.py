def comptar_vocals(paraula):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for lletres in paraula:
        match lletres.lower():
            case "a":
                a += 1
            case "e":
                e += 1
            case "i":
                i += 1
            case "o":
                o += 1
            case "u":
                u += 1

    return f"En la paraula {paraula} hi ha {a} a's, {e} e's, {i} i's, {o} o's, {u} u's"

print(comptar_vocals("Ratapinyada"))