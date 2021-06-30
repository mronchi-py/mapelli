from turtle import *
from frequenze_voti import frequenze

def disegna_riferimento(x, passo, dati):
    """Disegna i tratti per l'asse delle ascisse con le relative etichette"""
    goto(x, 0)
    color("grey")

    for etichetta in dati:
        goto(x, -30) # Spostati un po' sotto (30 pixel) per scrivere l'etichetta
        write(etichetta, font=("Arial", 16), align="center")
        goto(x, 0) # Ritorna in posizione per disegnare il tratto
        pendown()
        x += passo 
        goto(x - 5, 0) # Lascia uno spazio di 5 pixel tra un tratto e l'altro
        penup()

    # Stampa un'etichetta in più per completare l'insieme dei valori possibili
    # Per es. i voti sono 11 (da 0 a 10) ma gli intervalli sono 10 (0-1, 1-2,...)
    goto(x, -30)
    write(etichetta + 1, font=("Arial", 16), align="center")

def disegna_grafico(dati, scala=20, bordo=20, w=800, h=400):
    """Disegna un grafico dell'andamento delle frequenze di una lista di valori"""
    passo = (w - bordo*2) // len(dati) # Lunghezza di ogni passo nell'area del grafico
    x = -w // 2 + bordo # Ascissa d'inizio vicino al margine sinistro (c'è un bordo)
    setup(w, h)
    hideturtle()
    speed(0)
    pensize(3)
    penup()
    disegna_riferimento(x, passo, dati)
    goto(x, 0)
    pendown()
    color("blue")
    for freq in dati.values():
        freq_r = freq[0]
        goto(x, freq_r*scala)
        x += passo
        goto(x, freq_r*scala)
        write(freq_r, font=("Arial", 16), align="right")

if __name__ == "__main__":
    voti = [5, 7.5, 8, 5, 8, 7, 9.5, 5.5, 7, 7, 6, 4.5, 5, 3.5, 7, 6, 6.5, 4, 8, 7]
    freq = frequenze(voti, 0, 10)
    disegna_grafico(freq)

