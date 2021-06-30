from random import random
from math import sqrt
from time import time
from turtle import *

def disegna_goccia(x, y, colore, scala=400):
    """Disegna un punto colorato date le coordinate x e y e il fattore di scala"""
    penup()
    tracer(0) # Commenta questa riga per apprezzare il disegno eseguito mano a mano
    goto(x*scala, y*scala) # Utilizza un fattore di scala per disegnare i punti
    dot(4, colore)

def pi_greco(n):
    """Ritorna un'approssimazione del valore di pi greco calcolato con Monte Carlo"""
    n_interni = 0

    for i in range(n):
        x, y = random(), random()    # Genera una coppia di coordinate casuali tra [0, 1)        
        distanza = sqrt(x**2 + y**2) # Distanza dall'origine del punto (x, y)

        if distanza < 1:
            n_interni += 1
            colore = "blue"
        else:
            colore = "red"

        disegna_goccia(x, y, colore)
    
    return 4 * n_interni / n

if __name__ == "__main__":
    start_time = time()
    print(chr(960), "=", pi_greco(15000)) # Genero 15.000 gocce elettroniche
    elapsed_time = time() - start_time
    print("Tempo (s):", round(elapsed_time, 2))
