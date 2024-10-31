def superposicio():
    llista1 = ["Juan", "Pablo", "Pedro", "Bryan", "Pau"]
    llista2 = ["Joan", "David", "Victor", "Pedro"]
    resultat = False
    for i in llista1:
        if i in llista2:
            resultat = True
    print(resultat)

superposicio()