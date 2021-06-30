"""
    Il sistema di codifica base è l’ASCII (American Standard Code for Information Interchange)
    ASCII: 7 bit => 128 simboli
    ASCII ESTESO: 8 bit => 256 simboli

    - 95 stampabili
    - 33 di controllo (spazio, nuova linea, tabulazione, cancellazione del carattere precedente ecc.)
    - 128 simboli ASCII Esteso

    Python supporta la codifica Unicode che estende l’ASCII e comprende tutti i caratteri dell’italiano
    (quindi, anche le vocali accentate) e di tutte le lingue antiche e moderne dell’intera galassia
    conosciuta.
    Unicode ha codifica variabile e la codifica dei simboli ASCII coincide con quella Unicode.
"""

import string

# Il tipo str e' immutabile
print("=" * 79)
a = "1234567890"
print(type(a))
# a[4]='3'

# Classificazione come tipo composto...
print("=" * 79)
print("Lunghezza Stringa: " + str(len(a)))
print("Primo Carattere: " + a[0])
print("Ultimo Carattere: " + a[-1])

for i in range(5):
    print(">" + a[i] + "<")

# Python mette a disposizione anche 44 funzioni predefinite per operare sulle stringhe
print("=" * 79)
a = "pippo"
print("UPPER: " + str.upper(a))
# OOP style call
print("UPPER: " + a.upper())
print("REPLACE: " + a.replace("i", "o"))
print("FOUND 'ip' at position: " + str(a.find("ip")))
print("FOUND 'p' " + str(a.count("p")) + " times")
a = " 1238 "
print("ISNUMERIC " + str(a.isnumeric()))
print("ISNUMERIC " + str(a.strip().isnumeric()))

"""
String Parsing
Un’altra operazione che possiamo compiere con gli indici è lo SLICING.
Questa consente di ottenere gli elementi di una stringa compresi tra
due indici arbitrari
"""
# String Slicing
print("=" * 79)
s = "1234567890 abcdefghij ABCDEFGHIJ"
print(s[0:len(s)])

# String Splitting
x = s.split()
print(type(x))
print(x)

# ----------------------------
# Char Encoding
# ----------------------------
print("=" * 79)
print(ord('A'))
print(ord('è'))
print(chr(232))
print(chr(1064) + " -> " + chr(0x0428))

# ----------------------------
# Modulo string
# ----------------------------
print("=" * 79)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)

""""
>>> string.whitespace => ' \t\n\r\x0b\x0c'
"""
