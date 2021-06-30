"""Disegna una spirale quadratica"""
import turtle

screen = turtle.Screen()    # Crea un riferimento alla finestra di disegno
screen.title("Spirale quadratica")

ninja = turtle.Turtle()
ninja.speed(0)
ninja.pensize(2)
#ninja.shape("star.gif")     # Indossa il nuovo costume

passi = 2                  # Imposta lo spostamento iniziale
n = 15

for i in range(n):
    ninja.forward(passi)    # Va avanti di "passi"
    ninja.left(90)          # Ruota di 45° gradi (45° x 8 = 360°)
    passi += 10              # Aumenta lo spostamento
    ninja.forward(passi)    # Va avanti di "passi"
    ninja.left(90)          # Ruota di 45° gradi (45° x 8 = 360°)

turtle.done()
