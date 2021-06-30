"""Cambia il costume (shape) della tartaruga ninja con un'immagine"""
import turtle

screen = turtle.Screen()               # Crea un riferimento alla finestra di disegno
screen.addshape("ninja.gif") # Registra una nuova "shape" dal file
ninja = turtle.Turtle()
ninja.shape("ninja.gif")                 # Fa indossare a ninja il nuovo costume
