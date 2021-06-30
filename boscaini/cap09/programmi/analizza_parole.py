"""Programma che analizza le parole di un testo"""
import string

if __name__ == "__main__":
    n_parole = n_lettere = 0
    max_parola = "" # Parola più lunga

    for linea in open("i_promessi_sposi.txt"):
        # Converti i simboli di punteggiatura in spazi
        for sep in string.punctuation + "’": # Considera anche l'apostrofo curvo
            linea = linea.replace(sep, " ")

        for parola in linea.split(): # Lista delle parole della riga
            n_parole += 1
            n_lettere += len(parola)

            if len(parola) > len(max_parola): # Se ha trovato una parola più lunga...
                max_parola = parola
                print("{:2d} {}".format(len(max_parola), max_parola))
                
    print("\nNumero parole:", n_parole)
    print("Lunghezza media parole:", round(n_lettere / n_parole, 2))
