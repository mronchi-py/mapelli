"""
    Diverse tipologie di funzioni
    - per numero di Parametri
    - per numero Valori di Ritorno
"""


# funzione senza parametri che non resituisce nulla
def stampa_ciao():
    """ stampa ciao """
    print("Ciao")


# funzione con un parametro che non resituisce nulla
def stampa_messaggio(message):
    """ invia message allo stdout """
    print(message)


# funzione con un parametro che restituisce un valore
def aggiungi_underscore(messaggio):
    return "_" + messaggio + "_"


# funzione con un parametro che restituisce un valore
def aggiungi_underscore_2(messaggio: str) -> str:
    """ aggiunge il carattere '_' prima e dopo la stringa  
    :rtype: str
    """
    return "_" + messaggio + "_"


# funzione con un parametro che restituisce un valore
def tutto_maiuscolo(messaggio):
    return str.upper(messaggio)


# funzione con 2 parametri che restituisce un valore
def aggiungi_underscore_nvolte(messaggio, n):
    return "_" * n + messaggio + "_" * n


# funzione con un numero variabile di argomenti
def multi_paramenter(*aaa):
    print(len(aaa))
    print(aaa[0])
    print(aaa[1])


# funzione che restituisce una tupla (piu' valori)
def fun_tupla():
    return 'foo', 100


# esempio di definizione di funzione ricorsiva
def fattoriale(n):
    """ restituisce il fattoriale di n
    :rtype: int
    """
    if n == 1:
        return 1
    return n * fattoriale(n - 1)


# ------------------------------------------------------------
# Chiamate alle funzioni sopradefinite
# ------------------------------------------------------------
print("=" * 79)
stampa_ciao()

print("=" * 79)
stampa_messaggio("LS Mapelli")

# chiamata Keyword Arguments
stampa_messaggio(message="LS Mapelli")

print("=" * 79)
print("aggiungo underscore a pippo: ", aggiungi_underscore("pippo"))
print("aggiungo underscore a pippo: ", aggiungi_underscore_2("pippo"))


print("=" * 79)
print("pippo scritto in maiuscolo e': ", tutto_maiuscolo("pippo"))

print("=" * 79)
print("aggiungo underscore (3 vote) a pippo:  ", aggiungi_underscore_nvolte("pippo", 3))
# chiamata Keyword Arguments.. ho invertito posizione degli argomenti
print("aggiungo underscore (3 vote) a pippo:  ", aggiungi_underscore_nvolte(n=3, messaggio="pippo"))

print("=" * 79)
multi_paramenter("pippo", "pluto")

print("=" * 79)
a, b = fun_tupla()
print(a + " ---> " + str(b))

# Chiamata a funzione con numero di parametri variabili...
print("=" * 79)
print('Hello', 'World!!!', sep="...", end=" xxx")
"""
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
"""
