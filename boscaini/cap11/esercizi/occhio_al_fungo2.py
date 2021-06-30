"""Immagini: http://it.italianfantendo.wikia.com/wiki/Funghi_di_Super_Mario

Sfondo: http://opengameart.org/content/bevouliin-free-game-background-for-game-developers

https://pixabay.com/en/wanted-poster-wanted-poster-west-1081663/
https://pixabay.com/en/exit-sign-arrow-right-signage-44205/

Crea il programma occhio_al_fungo2.py che modifica il programma visto
nel capitolo per soddisfare anche i seguenti requisiti:
- quando il giocatore fa clic sul fungo scelto non può ripetere l’azione (il
clic), continuando ad aumentare il punteggio, prima che cambi la scena
(consiglio: usa una variabile flag);
- se l’utente fa clic su uno sprite sbagliato il punteggio diminuisce:
- facendo clic sul pulsante Exit (da aggiungere) il gioco termina.

Clicca su fungo che appare sulla sinistra"""
import os
from turtle import *
from random import randint, shuffle

SIZE = 75 # Dimensione dello sprite dei personaggi
SIDEBAR = 150 # Larghezza dell'area del punteggio di sinistra
DELAY = 2000 # Intervallo in millisecondi per cliccare sullo sprite ricercato
PATH_IMG="immagini"

def inizializza(path=PATH_IMG):
    """Inizializza la finestra, carica e ritorna la lista dei costumi"""
    title("Occhio al fungo")
    setup(w, h) # Dimensiona e posiziona la finestra al centro dello schermo
    register_shape("./wanted.gif") # Shape per il cartello "wanted"
    register_shape("./exit.gif") # Shape per il cartello "exit"
    costumi = []
    for filename in os.listdir(path): # Scorre i file della directory path
        register_shape(path +"/"+ filename) # Registra l'immagine come shape
        costumi.append(filename) # e la aggiunge alla lista dei costumi
    return costumi
    
def gioca():
    """Sceglie uno sprite fungo e lo posiziona con altri n sprite casuali"""
    global is_colpito # Così può modificare la variabile globale is_colpito
    is_colpito = False
    clearscreen() # Resetta canvas e tartarughe
    tracer(0)
    hideturtle()
    bgpic("full-background.gif")
    set_sprite(-(w - SIDEBAR) // 2, 140, "wanted.gif", ".")
    exit_button = set_sprite(-(w - SIDEBAR) // 2, -180, "exit.gif", ".")
    exit_button.onclick(fine) 
    shuffle(costumi) # Mescola i costumi e...
    scelto = costumi[0] # sceglie il primo
    altri_costumi = costumi[1:] # Tutti i costumi tranne quello scelto
    for i in range(n):
        shuffle(altri_costumi)
        costume = altri_costumi[0]
        posiziona_random(costume, sbagliato)

    posiziona_random(scelto, colpito) # Disegna il personaggio scelto
    set_sprite(-(w - SIDEBAR) // 2, 120, scelto) # e lo ridisegna nel "wanted"
    scrivi_punteggio(punteggio)
    update() # Aggiorna il canvas
    ontimer(gioca, DELAY) # Dopo DELAY millisecondi richiama se stessa

def set_sprite(x, y, costume=None, path=PATH_IMG):
    sprite = Turtle()
    if costume:
        sprite.shape(path +"/"+ costume)
    sprite.penup()
    sprite.goto(x, y)
    return sprite

def posiziona_random(costume, onclick_handler, path=PATH_IMG):
    x = randint(-w // 2 + SIDEBAR, w // 2 - SIZE)
    y = randint(-h // 2 + SIZE, h // 2)
    sprite = set_sprite(x, y, costume)
    sprite.onclick(onclick_handler)    

def colpito(x, y):
    global punteggio, is_colpito # Così può modificare la variabile globale punteggio e is_colpito

    if not is_colpito:
        punteggio += 1
        scrivi_punteggio(punteggio)
        is_colpito = True

def sbagliato(x, y):
    global punteggio # Così può modificare la variabile globale punteggio
    punteggio -= 1
    scrivi_punteggio(punteggio)

def fine(x, y):
    bye()
    exit()

def scrivi_punteggio(punteggio):
    sprite_punti.undo() # Annulla l'azione precedente di scrittura dei punti
    sprite_punti.write(str(punteggio), font=('Arial', 50), align="center")

if __name__ == "__main__":
    w, h = 1024, 512
    sprite_punti = set_sprite(-(w - SIDEBAR) // 2, -50)
    sprite_punti.hideturtle()
    punteggio = 0
    n = 25 # Numero di funghi
    costumi = inizializza()
    is_colpito = False
    gioca()
    mainloop()
    
