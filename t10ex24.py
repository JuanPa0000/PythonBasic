def crear_punts(llista):
    for i in llista:
        print(i * ".")
        
        
def dibuixarImatge():
    imatge = [0, 1, 2, 3, 4, 3, 2, 1, 0]
    imatge = crear_punts(imatge)

dibuixarImatge()