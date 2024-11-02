
llista = [
    ["Pere", 2000],
    ["Maria", 1999],
    ["Anna", 2007],
    ["Joan", 1987],
]
anyActual = 2024

def edat(elements, anyActual):
    edat = anyActual - elements[1]
    return edat

def calcular_anys(llista, anyActual):
    llista.insert(0, ["Nom", "Data Naixement", "Edat"])
    print(f"Any actual:", anyActual)
    print(llista[0])
    for elements in llista[1:]:
        elements.insert(2, edat(elements, anyActual))
        print(elements)
        
calcular_anys(llista, anyActual)