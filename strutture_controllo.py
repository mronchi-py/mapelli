"""
    Strutture (Costrutti) di Controllo
    - IF, IF-ELSE, IF-ELIF-ELSE
    - FOR
    - WHILE
"""

# ---------------------------------
# COSTRUTTO if-else
# ---------------------------------
print("=" * 29 + " COSTRUTTO IF-ELSE " + "=" * 29)
n = 10
if n > 10:
    print("n e' > di 10")
else:
    print("n e' <= di 10")

# ---------------------------------
# COSTRUTTO if-elif-else
# ---------------------------------
print("=" * 29 + " COSTRUTTO IF-ELIF-ELSE " + "=" * 29)
n = 10
if n > 10:
    print("n e' > di 10")
elif n < 10:
    print("n e' < di 10")
else:
    print("n e' = 10")

"""
    Le strutture di controllo while e for sono intercambiabili: al posto di
    una puoi usare l’altra e viceversa.
    Il for è più adatto a ripetere un blocco di codice un certo numero di volte e
    per ogni elemento di un elenco.
    Il while si adatta meglio a situazioni in cui non si sa a priori
    quante volte verrà eseguito il ciclo.
"""

# ---------------------------------
# COSTRUTTO (CICLO) for
# DataType: range (Intervallo)
#  range(start, stop, step)
# ---------------------------------
print("=" * 29 + " CICLO FOR " + "=" * 29)

a = range(5)  # range(0,5,1)
print(type(a))
print(a[0])
for i in a:
    print(i)

# range --> list
b = list(a)
print("range2list #1", b)

a = range(1, 15, 2)
b = list(a)
print("range2list #2", b)

# ---------------------------------
# COSTRUTTO (CICLO) while
# ---------------------------------
print("=" * 29 + " CICLO WHILE " + "=" * 29)
i = 0
while i < 5:
    print(i)
    i += 1  # i=i+1
