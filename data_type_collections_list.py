"""
    Reminder
    - Liste []
    - Tuple ()
    - Set {}
    - Dictionary {k:v}
"""
import sys

# ----------------------------------------------------------
# List: Elenco eterogeneo, ordinato per posizione
# ----------------------------------------------------------

print("=" * 29 + " LIST: ELENCO ETEROGENEO, ORDINATO PER POSIZIONE " + "=" * 29)
a = ["Roma", "Oslo", "Lisbona", "Reykjavik", 234, 'Roma']
print(type(a))
print(a)

# accedo agli elementi per posizione
print("Elemento nella posizione 0", a[0])
print('Lista dalla pos 1 alla pos 3 (esclusa)', a[1:3])
print('Lista dalla pos 0 alla pos 2 (esclusa)', a[:2])
print('Lista dalla pos 2 alla fine della lista', a[2:])

# Negative Indexing
print("Ultimo Elemento della Lista", a[-1])

# Presenza di un elemento nella lista
if "Lisbona" in a:
    print("Yes, 'Lisbona' is in the list")

# Aggiunta di un elemento in una determinata posizione
a.insert(3, "Monza")
print("Aggiunto Monza", a)

# Aggiungo un elemento in coda
a.append(34.67)

# Aggiungo una lista alla lista
a.extend(["Vimercate", "Cambiago"])
print("Aggiunta (Estesa) Lista:", a)

# cancellazione per valore
a.remove(34.67)
print("Cancellazione per valore:", a)

# cancellazione per indice
a.pop(5)
print("Cancellazione per indice:", a)
a.pop()
print("Cancellazione dell'ultimo elemento della lista: ", a)

# cancellazione di tutti gli elelemnti della lista
# NON viene cancellata la lista nel senso che la varibile risulta definita
a.clear()
print("Cancellazione di tutti gli elelemnti della lista", a)

# Lista di numeri
print("=" * 29 + " LISTA DI NUMERI " + "=" * 29)
a = [1, 5, 733, 56]
print(max(a))
print(min(a))
# la funzione modifica direttamente la lista
a.reverse()
print(a)
# la funzione modifica direttamente la lista
a.sort()
print(a)

# ---------------------------------
# iterate over list
# ---------------------------------
print("=" * 29 + " ITERATE OVER LIST " + "=" * 29)
listaAmici = ["Carlo", "Andrea", "Barbara"]
for amico in listaAmici:
    print(amico.upper())

# ----------------------------------------------------------------------
# Liste parallele: iterating through ists in parallel
# (instead of OOP)
# ----------------------------------------------------------------------
print("=" * 29 + " ITERATING THROUGH ISTS IN PARALLEL " + "=" * 29)
names = ['Bob', 'Douglas']
ages = [38, 42]
occupations = ["Teacher", "Writer"]
for n, a,o in zip(names, ages,occupations):
    print(f"Name: {n}, Age: {a}, Occupation: {o}.")


# ---------------------------------------------------------------------------
# List Comprehensions I
# Una Comprensione di lista è costrutto sintattico per creare
# una lista basandosi su altre liste.
# ---------------------------------------------------------------------------
print("=" * 29 + " LIST COMPREHENSIONS (I) " + "=" * 29)
foo = [1, 5, 89]
print(foo * 2)

bar = [x * 2 for x in foo]
print(bar)

# ---------------------------------
# List Comprehensions II (filter)
# ---------------------------------
print("=" * 29 + " LIST COMPREHENSIONS (II) " + "=" * 29)
bar = [x for x in listaAmici if x.endswith("a")]
print(bar)
