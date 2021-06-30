"""
    Esempio utilizzo Modulo turle della Standard Library

    https://docs.python.org/3/library/turtle.html#module-turtle
"""
import turtle


def draw_polygon(no_lati, lun_lato):
    """ disegna un poligono regolare di no_lati di lunghezza lun_lato"""
    for i in range(no_lati):
        ninja.forward(lun_lato)
        ninja.left(360 / no_lati)


if __name__ == '__main__':
    ninja = turtle.Turtle()  # Crea una "Turtle" di nome "ninja"

    draw_polygon(7, 100)

    turtle.done()
