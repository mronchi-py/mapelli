"""
    Controlla se un anno inserito dall’utente è bisestile oppure no.
    Sono bisestili  gli anni multipli di 4 a eccezione degli anni secolari (100, 200,…) che sono
    bisestili solo ogni 400 anni (400, 800,…).
    Per esempio, gli anni 1968 e 2000 sono bisestili, mentre il 1969, il 2100 e il 2200 non lo sono
"""
# Conversione da str a floats
anno = int(input("Inserire l'anno: "))

multiplo4 = anno % 4 == 0
multiplo100 = anno % 100 == 0
multiplo400 = anno % 400 == 0

if multiplo4 and ((not multiplo100) or multiplo400):
    print("Anno Bisesto anno funesto...")
else:
    print("Anno NON Bisestile...")
