"""Programma che analizza le parole di un testo con la funzione parole_lunghe()
che, dato un testo contenuto in un file e un numero n, ritorna la lista delle
parole in ordine alfabetico la cui lunghezza è maggiore o uguale a n. Un con-
siglio: utilizza un oggetto di appoggio di tipo set."""
import string

def parole_lunghe(filename, n):
    parole = set()

    for linea in open(filename):
        # Converti i simboli di punteggiatura in spazi
        for sep in string.punctuation + "’": # Considera anche l'apostrofo curvo
            linea = linea.replace(sep, " ")

        for parola in linea.split(): # Lista delle parole della riga
            if len(parola) >= n: # Se ha trovato una parola più lunga di n
                parole.add(parola)

    return parole      

if __name__ == "__main__":
    filename = "i_promessi_sposi.txt"
    parole = parole_lunghe(filename, 15)

    for parola in parole:
        print("{:2d} {}".format(len(parola), parola))

