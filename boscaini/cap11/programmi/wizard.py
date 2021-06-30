"""Programma per mostrare come muovere e animare un personaggio"""
import os
from turtle import *


def inizializza(w, h, n_costumi=3):
    setup(w, h)
    bgpic("wizard/background.gif")  # Imposta un'immagine di sfondo

    for filename in os.listdir("wizard"):  # Registra le immagini del mago
        addshape("wizard/" + filename)


# Funzioni per controllare il movimento del nostro mago-tartaruga
def up():
    wizard.setheading(90)  # Punta in alto (il costume rimane fisso)
    wizard.forward(move_speed)


def down():
    wizard.setheading(-90)
    wizard.forward(move_speed)


def right():
    wizard.setheading(0)
    wizard.forward(move_speed)


def left():
    wizard.setheading(180)
    wizard.forward(move_speed)


def fire():
    """Il tasto spazio scatena l'attacco"""
    for i in range(1, 4):  # Animazione dell'attacco (3 costumi)
        wizard.shape("wizard/attack_" + str(i) + ".gif")
        delay(80)
    wizard.shape("wizard/walk.gif")


if __name__ == "__main__":
    move_speed = 10  # Numero di pixel per ogni passo
    inizializza(800, 400)
    wizard = Turtle()
    wizard.shape("wizard/walk.gif")
    wizard.penup()
    # Associa le funzioni precedenti a eventi della tastiera
    screen = Screen()  # Serve un riferimento alla finestra di Turtle
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")
    screen.onkey(fire, "space")
    screen.listen()
