from turtle import *

def disegna_punti(punti):
    """Disegna una lista di punti con le loro coordinate sul canvas"""
    penup()
    hideturtle()
    shape("square")
    shapesize(0.4, 0.4)
    
    for x, y in punti:
        goto(x, y)
        color("red")
        stamp()
        color("black")
        #s = " ({},{})".format(x, y) # Lo spazio serve per distanziare la scritta
        s = " (%s,%s)" % (x, y) # Lo spazio serve per distanziare la scritta dal quadratino
        write(s, font=("Arial", 15, "normal"))

if __name__ == "__main__":
    title("Punti numerati")
    punti = [(0,0), (-100,-37), (-175,10), (120,43)]
    disegna_punti(punti)

    done()