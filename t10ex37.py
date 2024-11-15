import random
import time
import os

def intro():
    print("Bienvenido a MasterMind")
    print("""En este juego debes adivinar el codigo de 4 cifras que ha creado la máquina.
Para ello tendrás 10 intentos, si no logras descifrar el código en 10 intentos, pierdes.
Esta mini versión de MasterMind, es un poco diferente, tendrás vacas y toros, las vacas
representan los números acertados (que están en el código secreto pero no en la misma posición)
y los toros representan los números que están en la posición correcta.
          
También dispondras de un historial, que te dicen los intentos que has hecho y las vacas y toros
que has adivinado junto al número introducido, este historial te ayudará a resolver el juego
          
          """)
    a = input("Has leído el tutorial y quieres pasar al juego( S/s ): ")
    if a.lower() == "s" or a.lower() == "si":
        os.system("clear")
    else:
        exit()

def correctNumber(codiSecret, usuari):
    cn = 0
    for i in str(codiSecret):
        if i in usuari:
            cn += 1
    return cn

def correctPosition(codiSecret, usuari):
    cp = 0
    for i in range(4):
        if str(codiSecret)[i] == usuari[i]:
            cp += 1
    return cp

def codiMaquina():
    codiSecret = ""
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(l)
    ld = l[0:4]
    for e in ld:
        codiSecret += str(e)
    int(codiSecret)
    return codiSecret

def codiUsuari():
    codiUsuari = "0000"
    while True:
        codiUsuari = input("Introduce un código de 4 números: ")
        print("\n")
        if len(codiUsuari) == 4:
            break
    return codiUsuari

a = True
while a:
    intro()
    print("Creando código secreto...")
    time.sleep(2)
    print("Código secreto creado...")
    codiSecret = codiMaquina()
    codiSecret = int(codiSecret)
    time.sleep(1)
    intents = 1
    historial = []
    while True:
        usuari = codiUsuari()
        cn = correctNumber(codiSecret, usuari)
        cp = correctPosition(codiSecret, usuari)
        historial.append(f"Intento {intents}: " + usuari + f" {cn - cp}V {cp}T")
        print(f"En tu codigo {usuari} tienes {cn - cp} vacas y {cp} toros")
        for e in historial:
            print(e)
        if intents == 10:
            print("\n")
            print("Has perdido")
            print("\n")
            break
        elif cp == 4:
            print("\n")
            print("Felicidades, has ganado")
            print("\n")
            break
        intents += 1
    jugar = input("Vols tornar a jugar? s/n: ")
    if jugar.lower() == "n" or jugar.lower() == "no":
        a = False