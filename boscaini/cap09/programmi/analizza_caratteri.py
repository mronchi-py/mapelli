"""Programma che conta i seguenti elementi di un testo: caratteri, lettere,
distinguendo vocali e consonanti, segni di punteggiatura e parole"""
from string import ascii_lowercase, punctuation

def print_valore(descrizione, valore):
    """Stampa in colonne descrizione e valore la prima con allineamento a sinistra
    in un campo di 25 caratteri il secondo a destra in un campo di 12 e con
    il punto come separatore per le migliaia (che rimpiazza la virgola anglosassone)"""
    print("{:<25}{:12,d}".format(descrizione, valore).replace(",", "."))

if __name__ == "__main__":
    n_lettere = n_vocali = n_spazi = n_punteggiatura = 0

    for linea in open("i_promessi_sposi.txt", "r"):
        for car in linea.lower():
            if car in ascii_lowercase:
                n_lettere += 1

                if car in "aeiou":
                    n_vocali += 1
            elif car == " ":
                n_spazi += 1
            elif car in punctuation:
                n_punteggiatura += 1

    print_valore("Lettere", n_lettere)
    print_valore("Vocali", n_vocali)
    print_valore("Consonanti", n_lettere - n_vocali)
    print_valore("Spazi", n_spazi)
    print_valore("Segni di punteggiatura", n_punteggiatura)
