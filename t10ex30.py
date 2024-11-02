
llista = [
    ["Pere", 2000],
    ["Maria", 1999],
    ["Anna", 2007],
    ["Joan", 1987],
]
anyActual = 2024

def calcular_any(llista, anyActual):
    print("_" * 27)
    print(f"Any actual: {anyActual}")
    print(f"{"Nom":3} {"|"} {"Data Naixement":13} {"|"} {"Edat"}")
    print("-" *27)
    for nom, anyNaixement in llista:
        edat = anyActual - anyNaixement
        print(f"{nom:3}{anyNaixement:10}{edat:11}")
        
calcular_any(llista, anyActual)
