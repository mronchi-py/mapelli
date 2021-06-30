from turtle import *
from random import randint


def inizializza(w, h, n_costumi=2):
    setup(w, h, None, None)  # Con "None" posiziona la finestra al centro dello schermo
    bgpic("bg.gif")  # Imposta un'immagine di sfondo

    for colore in colori:  # Registra i costumi associati a ciascun colore
        for i in range(1, n_costumi + 1):
            addshape(colore + str(i) + ".gif")


def vola(colore, n_costumi=2):
    penup()
    hideturtle()  # Mentre si prepara, la tartaruga è invisibile
    x = -w // 2  # Parte dal bordo sinistro,
    y = randint(-h // 2, h // 2)  # da un'altezza casuale tra i bordi superiore e inferiore
    speed(0)  # e alla massima velocità
    goto(x, y)
    speed('normal')  # Ora si muove con velocità "normal", cioè 6
    showturtle()
    passi = randint(5, 80)  # Numero di passi (=velocità di spostamento) casuale

    while xcor() < w // 2:  # Fintanto che non ha raggiunto il bordo dx
        for i in range(1, n_costumi + 1):  # Per ogni costume...
            shape(colore + str(i) + ".gif")
            forward(passi)
            delay(50)  # Attendi 50 millisecondi


if __name__ == "__main__":
    colori = "yellow", "pink", "blue"
    w, h = 1200, 600  # w=width (larghezza), h=height (altezza)
    inizializza(w, h)

    while True:  # Per sempre
        for colore in colori:
            vola(colore)
