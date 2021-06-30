"""
    Somma i quadrati da 1 a n

    Scrivi il programma somma_quadrati.py che utilizza un ciclo for
    per stampare i quadrati dei numeri da 1 a n (con n è inserito dall’utente) e la loro somma

    AUGMENTED ASSIGNMENT STATEMENTS
    -------------------------------
    The short form
        a += 1
    has the option to modify a in-place, instead of creating a new object representing the sum and
    rebinding it back to the same name:
        a = a + 1.
    So,The short form(a += 1) is much efficient as it doesn't necessarily need to make a copy of a unlike a = a + 1.
"""

n = int(input("Numero: "))
somma = 0
i = 1

while i <= n:
    somma += i*i            # somma = somma + i*i
    print(i*i, end=" ")
    i += 1                   # i = i + 1

print("\nSomma quadrati: ", somma)
