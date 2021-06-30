"""
    Esempio dell'utilizzo del modulo tkinter (della Standard Library di Python)

    Widget: è un componente grafico di una interfaccia utente di un programma

    Un programma interattivo può cambiare il proprio comportamento in risposta
    all’input dell’utente, durante l’esecuzione. Tra i programmi interattivi ci
    sono quelli che rispondono solamente agli input da tastiera, i programmi grafici
    con bottoni e menu, e quelli che rispondono a interazioni “naturali”
    tramite touch screens.
    Gli ultimi due tipi usano interfacce utente grafiche,
    in inglese Graphical User Interface, o più brevemente GUI.
    Nel seguito considereremo le interfacce per sistemi a finestra,
    tipiche dei programmi su notebook e desktop.

"""
from tkinter import *


# Definisce la callback del bottone
def btn_onclick():
    print('Clicked Button')
    print("Ciao " + entry_var.get())


w = Tk()
w.title("gui_III")
w.geometry("400x100")
w.resizable(False, False)
# window.configure(background="grey")


# variabile per memorizzare i
# valori scritti in entry_var
entry_var = StringVar()

# Widget Label
lbl = Label(w, text='Inserirsci il tuo Nome')
lbl.grid(row=0, column=0, padx=10, pady=10)

# Widget Entry (Input)
ent = Entry(w, textvariable=entry_var)
ent.grid(row=0, column=1, padx=10, pady=10)

# Widget Button
btn = Button(w, text='Click Me!!!', command=btn_onclick)
btn.grid(row=0, column=2, padx=10, pady=10)

w.mainloop()
