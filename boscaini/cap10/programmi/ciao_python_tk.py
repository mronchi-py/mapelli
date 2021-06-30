"""Crea una finestra TKinter con una scritta e un'immagine"""
from tkinter import *
from PIL import Image

root = Tk() # Inizializza Tkinter e crea la finestra principale (root=radice)
root.title("Un saluto...")

# Con PIL crea una miniatura PNG dell'immagine JPG di partenza
image = Image.open("risorse/agnesina.jpg")
# Proporzione, w : image.width = h : image.height
w = 230
h = w * image.height // image.width
image = image.resize((w, h), Image.ANTIALIAS)
image.save("risorse/agnesina_miniatura.png")

# Aggiunge ("impacchetta") a destra l'etichetta (label) con l'immagine
miniatura = PhotoImage(file="risorse/agnesina_miniatura.png")
label_immagine = Label(root, image=miniatura).pack(side="right")

# Aggiunge a sinistra un testo con distanza da sx e dx di 20 pixel
# Per leggibilità gli argomenti sono riportati su più linee
label_testo = Label(root,
                   font=("Helvetica", 16),
                   padx = 25, 
                   text="Ciao, Python!").pack(side="left")

root.mainloop() # Loop di Tkinter: gestisce gli eventi fino alla chiusura della finestra
print("Programma terminato") # Viene stampato quando la finestra si chiude
