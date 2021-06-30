"""Disegna un quadrato utilizzando il ciclo for"""
import turtle
import time

screen = turtle.Screen()           # Crea un riferimento alla finestra di disegno
screen.setup(450, 380, 0, 0)    # Dimensiona e posiziona la finestra principale
screen.addshape("ninja.gif")    # Registra una nuova "shape" da un file

ninja = turtle.Turtle()
ninja.pensize(8)            # Penna con dimensione di 8 pixel
ninja.pencolor("blue")   # e di colore blu
ninja.shape("ninja.gif")  # Indossa il costume della shape appena aggiunta

for i in range(4):   # Ripeti per 4 volte...
    ninja.forward(150)
    ninja.left(90)
    time.sleep(0.5)   # Attendi mezzo secondo
