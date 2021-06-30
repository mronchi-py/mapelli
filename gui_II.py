"""
    Esempio dell'utilizzo del modulo tkinter (della std library)

    Widget: è un componente grafico di una interfaccia utente di un programma
"""
from tkinter import *


# Definisce la callback del bottone
def btn_onclick():
    print('Clicked Button')
    print("Valore inviato e': " + entry_var.get())
    w.configure(background=entry_var.get())


w = Tk()
w.title("gui_IV")
w.geometry("400x100")
w.resizable(False, False)
# w.configure(background="grey")


# variabile per memorizzare i
# valori scritti in entry_var
entry_var = StringVar()

# Widget Label
lbl = Label(w, text='Inserire un colore')
lbl.grid(row=0, column=0, padx=10, pady=10)

# Widget Entry (Input Field)
ent = Entry(w, textvariable=entry_var)
ent.grid(row=0, column=1, padx=10, pady=10)

# Widget Button
btn = Button(w, text='Set Background', command=btn_onclick)
btn.grid(row=0, column=2, padx=10, pady=10)

# Event loop
w.mainloop()
