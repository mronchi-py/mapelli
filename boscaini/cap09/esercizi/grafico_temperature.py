from turtle import *
from frequenze_voti import frequenze

def disegna_grafico(filename, scala=2, bordo=20, w=800, h=400):
    """legge i dati delle temperature registrate sul file temperature.txt,
    dove ogni riga contiene un valore numerico (per esempio “35.4”),
    e crea un grafico con Turtle dell’andamento dei valori con linee e punti"""
    dati = open(filename).readlines()
    passo = (w - bordo*2) // len(dati) # Lunghezza di ogni passo nell'area del grafico
    x = -w // 2 + bordo # Ascissa d'inizio vicino al margine sinistro (c'è un bordo)
    setup(w, h)
    hideturtle()
    speed(0)
    shape("square")
    turtlesize(0.5, 0.5, 1)
    pensize(3)
    penup()
    goto(x, 0)
    pendown()

    for linea in dati:
        color("orange")
        freq_r = eval(linea[:-1]) # Non considero l'a capo finale
        y = freq_r*scala
        goto(x, y)
        stamp()
        color("black")
        penup()
        goto(x, y + 20)
        write(str(freq_r) +"%", font=("Arial", 16), align="left")
        goto(x, y)
        pendown()
        x += passo

if __name__ == "__main__":
    disegna_grafico("temperature.txt")
    done()

