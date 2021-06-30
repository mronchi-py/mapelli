"""Disegna coriandoli come poligoni casuali colorati"""
from turtle import *
from random import randint

def inizializza(titolo):
    """Inizializza la finestra del programma"""
    title(titolo)
    tracer(0) # Blocca il ridisegno automatico per accelerare i calcoli
    setup(w, h, 0, 0) # Dimensiona e posiziona la finestra
    colormode(255) # Imposta i valori per i colori da 0 a 255

def disegna_poligono(n_min, n_max):
    """Disegna un poligono a caso sul canvas.
    Il numero dei lati è compreso tra n_min e n_max"""
    pencolor("black") # Nero per il colore della penna
    r, g, b = randint(40, 255), randint(0, 255), randint(0, 255)
    fillcolor((r, g, b)) # Colore di riempimento casuale red, green, blue
    n_lati = randint(n_min, n_max)
    begin_fill() # Apprestati a disegnare una forma da riempire
    
    for i in range(n_lati): # Disegna un poligono con n_lati 
        left(360 / n_lati)
        forward(200 / n_lati)

    end_fill() # Chiudi e riempi di colore la forma disegnata

def crea_poligoni(n, n_min, n_max):
    """Disegna n poligoni casuali sul canvas richiamando disegna_poligono()"""
    for i in range(n):
        x = randint(-w // 2, w // 2)
        y = randint(-h // 2, h // 2)
        penup()
        goto(x, y) # Parti da un punto casuale all'interno del canvas
        down()
        disegna_poligono(n_min, n_max)
        update() # Aggiorna il disegno sul canvas

if __name__ == "__main__":
    w, h = 900, 400 # Dimensione della finestra, in altezza e larghezza
    inizializza("Poligoni colorati casuali")
    crea_poligoni(150, 3, 20) # 150 poligoni dal triangolo all'icosagono
