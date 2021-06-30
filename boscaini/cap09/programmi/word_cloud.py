"""Crea una word cloud con i nomi propri maggiormente presenti in un testo"""
from string import punctuation, ascii_uppercase
from turtle import *
from random import randint

def vocabolario(filename, lung_min=5, iniziale_maiuscola=True):
    """Ritorna un dizionario con le parole e la loro frequenza in un file di testo. Le parole
    devono superare una lunghezza minima e avere o non avere l'iniziale maiuscola"""
    diz = {}
    for linea in open(filename):
        # Converti i simboli di punteggiatura in spazi
        for sep in punctuation + "’": # Considera anche l'apostrofo curvo
            linea = linea.replace(sep, " ")
        for parola in linea.split(): # Lista delle parole della riga
            if len(parola) >= lung_min:
                if iniziale_maiuscola and parola[0] in ascii_uppercase:
                    if parola not in diz:
                        diz[parola] = 1 # Prima occorrenza
                    else:
                        diz[parola] += 1
    return diz

def vocabolario_filtrato(diz_base, min_occorrenze=15):
    """Ritorna un dizionario con solo gli elementi che hanno un minimo
    numero di occorrenze nel dizionario specificato"""
    diz = {}
    for chiave, n_occorrenze in diz_base.items():
        if n_occorrenze >= min_occorrenze:
            diz[chiave] = n_occorrenze            
    return diz    
    
def word_cloud(dizionario, w=900, h=600, bordo=150, scala=0.1):
    """Crea una word cloud con le parole specificate"""
    setup(w, h)
    penup()
    hideturtle()
    tracer(0)
    colori = ["slate blue", "navy", "firebrick", "dark violet", "snow4", \
              "orange red", "navajowhite3", "gold3", "red4", "turquoise3"]
    x_min, x_max = -w // 2 + bordo, w // 2 - bordo*2
    y_min, y_max = -h // 2 + bordo, h // 2 - bordo
    for parola, n_occorrenze in dizionario.items():
        x = randint(x_min, x_max)
        y = randint(y_min, y_max)
        goto(x, y)
        dim = 16 + int(n_occorrenze * scala) # Usa come minimo un font 16
        colore = colori[randint(0, len(colori) - 1)]
        color(colore)
        write(parola, font=("Arial", dim))
    
if __name__ == '__main__':
    voc = vocabolario("i_promessi_sposi.txt")
    voc = vocabolario_filtrato(voc)
    word_cloud(voc)
