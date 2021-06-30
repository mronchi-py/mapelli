"""Disegna 4 linee colorate in verticale"""
import turtle

distanza = 50
lunghezza = 200
dim = 6

ninja = turtle.Turtle()     # Crea una tartaruga
ninja.pensize(dim)          # Penna di dimensione 8
ninja.shape("turtle")       # Costume di una "vera tartaruga"

# 1° gradino
ninja.pendown()
ninja.pencolor("red")    # Colore della penna "red"
ninja.forward(lunghezza)
ninja.penup()
ninja.backward(lunghezza)
ninja.left(90)
ninja.forward(distanza)
ninja.right(90)

# 2° gradino
ninja.pendown()
ninja.pencolor("green")    # Colore della penna "green"
ninja.forward(lunghezza)
ninja.penup()
ninja.backward(lunghezza)
ninja.left(90)
ninja.forward(distanza)
ninja.right(90)

# 3° gradino
ninja.pendown()
ninja.pencolor("blue")    # Colore della penna "blue"
ninja.forward(lunghezza)
ninja.penup()
ninja.backward(lunghezza)
ninja.left(90)
ninja.forward(distanza)
ninja.right(90)

ninja.pencolor("black")    # Colore della penna nero (così si vede sul violetto)

turtle.done()