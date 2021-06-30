"""
    Leonardo da Pisa, detto “Fibonacci”, è stato uno dei più grandi
    matematici di tutti i tempi. A lui si deve la scoperta di una serie di numeri
    che, curiosamente, si ritrovano in svariati settori

    1,1,2,3,5,8,13,21,34,55

"""


def fibonacci(n):
    """Ritorna l'n-simo valore della serie di Fibonacci"""
    a, b = 1, 1  # a = num. coppie al primo mese, b al secondo mese

    for i in range(1, n + 1):
        a, b = (b, a + b)  # Va in avanti con le coppie nei mesi successivi

    return a


for i in range(10):
    print(fibonacci(i))
