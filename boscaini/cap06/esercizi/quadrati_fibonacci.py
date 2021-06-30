import turtle
from fibonacci import fibonacci

MOLT = 15 # Moltiplicatore per dare al quadrato una dimensione apprezzabile

def disegna_quadrato(ninja, segmenti, lato, fib):
    for i in range(segmenti):
        ninja.forward(lato)
        ninja.left(90)
        
    ninja.color('red')
    # Scrive il valore corrente di Fibonacci in rosso a fianco del quadrato
    ninja.write(fib, align="Right", font=("Arial", 12, "bold"))
    ninja.color('black')
    ninja.forward(lato) # Si posiziona per tracciare il prossimo quadrato

def disegna_figura(n_quadrati):
    ninja = turtle.Turtle()
    ninja.pensize(2)
    ninja.speed(0)
    segmenti = 3 # Nel primo passaggio ho solo 3 segmenti

    for i in range(n_quadrati):
        fib = fibonacci(i)
        disegna_quadrato(ninja, segmenti, fib * MOLT, fib)
        segmenti = 5 # D'ora in poi i segmenti sono 5

    turtle.done()

disegna_figura(7)

