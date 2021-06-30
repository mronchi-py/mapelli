def print_perfetti(n):
    """Stampa i numeri perfetti fino ad n"""
    for i in range(2, n + 1):
        somma = 0

        for j in range(1, i // 2 + 1): # Oltre la metà + 1 non ci sono più divisori
            if i % j == 0:
                somma += j # Aggiungo a somma il divisore trovato
                #print(i, j, somma) # Stampa, se serve, i valori intermedi

        if somma == i:
            print(i, end=" ")
