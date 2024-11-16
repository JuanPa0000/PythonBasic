def indexParaula(paraula):
    l = ["gorra", "camiseta", "pantalon", "Joan"]
    try:
        index = l.index(paraula)
        return index
    except ValueError:
        return -1
    
print(indexParaula("pantalon"))
print(indexParaula("zapatos"))
    