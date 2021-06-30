import tkinter as tk

def somma():
    risultato.set(operando1.get() + operando2.get())

if __name__ == "__main__":
    root = tk.Tk()    
    root.geometry("300x90") # Ridimensiona la finestra
    root.title("Sommatore")

    # Variabili da associare ai controlli
    operando1 = tk.DoubleVar()
    operando2 = tk.DoubleVar()
    risultato = tk.DoubleVar()

    # Controlli: 2 box, un pulsante e una label
    box_operando1 = tk.Entry(root, textvariable=operando1).pack()
    box_operando2 = tk.Entry(root, textvariable=operando2).pack()
    button_esegui = tk.Button(root, text="Esegui", command=somma).pack()
    label_risultato = tk.Label(root, textvariable=risultato).pack()
    
    root.mainloop() # Loop di Tkinter: gestisce gli eventi fino alla chiusura della finestra
