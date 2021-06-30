"""Gioco del tris"""
from turtle import *

def vincitore():
    """Ritorna il simbolo vincitore, se c'è, altrimenti ritorna implicitamente None"""
    oriz, vert = "", "" # Stringhe per memorizzare le terne orizzontali e verticali
    for i in (0, 1, 2):
        for j in (0, 1, 2):
            oriz += m[i][j]
            vert += m[j][i]
        oriz += " "            
        vert += " "                        
    diag1 = m[0][0] + m[1][1] + m[2][2] # Terna della diagonale principale
    diag2 = m[0][2] + m[1][1] + m[2][0] # e secondaria
    s_matrice = oriz +" "+ vert +" "+ diag1 +" "+ diag2
    print(s_matrice)
    if "xxx" in s_matrice:
        return "x"
    elif "ooo" in s_matrice:
        return "0"

def inizializza():
    """Setup del gioco con visualizzazione della griglia vuota"""
    title("Tris")
    setup(500, 500) # Dimensiona e posiziona al centro dello schermo la finestra
    register_shape("v.gif")
    register_shape("x.gif")
    register_shape("o.gif")
    penup()
    for riga in (0, 1, 2):
        for colonna in (0, 1, 2):
            disegna_cella("v", riga, colonna)

def disegna_cella(stato, riga, colonna):
    """Stampa uno stato del gioco nella cella specificata"""
    shape(stato +".gif")
    x = colonna*dim - dim*1.5
    y = dim*1.5 - riga*dim
    goto(x, y)
    stamp()

def esegui_mossa(x, y):
    """Gestisce il click del mouse per eseguire, se possibile, la prossima mossa"""
    global giocatore
    if not vincitore(): # Se non c'è un vincitore vado avanti col gioco
        riga =  abs(round((dim*1.5 - y) / dim)) # Calcola la riga su cui è avvenuto il click
        colonna = round((x + dim*1.5) / dim)  # e la colonna
        if riga in (0, 1, 2) and colonna in (0, 1, 2): # Se il click è stato su una cella reale
            if m[riga][colonna] == "v":
                m[riga][colonna] = giocatore
                disegna_cella(giocatore, riga, colonna)                
                giocatore = "o" if giocatore == "x" else "x" # Turno successivo
    risultato = vincitore() # Dopo una mossa ricontrolla se c'è un vincitore
    if risultato: 
        stampa_vincitore(risultato)

def stampa_vincitore(risultato):        
    hideturtle()
    goto(-210, 20) # Si posiziona per scrivere il messaggio di vittoria
    color("white")
    messaggio = 'Ha vinto "%s"' % risultato
    write(messaggio, font=("Arial", 45))
    forward(-4)
    write(messaggio, font=("Arial", 45))
    color("black")
    forward(2)
    write(messaggio, font=("Arial", 45))

if __name__ == "__main__":
    giocatore = "x" # Il primo turno è associato al simbolo "x"
    dim = 110 # Dimensione del lato delle immagini dei simboli delle celle
    m = [["v", "v", "v"],
         ["v", "v", "v"],
         ["v", "v", "v"]]
    inizializza()
    screen = Screen()
    screen.onclick(esegui_mossa) # Associa esegui_mossa() all'evento click del mouse
