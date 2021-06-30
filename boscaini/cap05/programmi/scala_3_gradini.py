"""Disegna un una scala con 3 gradini"""
import turtle

alzata = eval(input("Alzata: "))
pedata = eval(input("Pedata: "))

ninja = turtle.Turtle()        # Crea una tartaruga
ninja.pensize(8)                # Penna di dimensione 8
ninja.shape("turtle")         # Ecco finalmente la tartaruga!
ninja.pencolor("violet")     # Colore della penna viola, o violetto
ninja.shape("turtle")         # Ecco finalmente la tartaruga!

# 1° gradino
ninja.left(90)
ninja.forward(alzata)
ninja.right(90)
ninja.forward(pedata)

# 2° gradino
ninja.left(90)
ninja.forward(alzata)
ninja.right(90)
ninja.forward(pedata)

# 3° gradino
ninja.left(90)
ninja.forward(alzata)
ninja.right(90)
ninja.forward(pedata)

ninja.pencolor("black")    # Torno al nero (così la tartaruga si vede meglio sul violetto)
