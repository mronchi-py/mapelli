"""
    I dati rappresentati dalle variabili di un programma in esecuzione risiedono nella RAM.
    Questa memoria è volatile e, quindi, quando il programma termina, o il computer viene spento,
    questi dati sono irrimediabilmente persi.
    Un file serve a memorizzare dati in modo permanente su memoria di massa (hard disk, chiavetta USB, SSD,…)
    affinché siano disponibili per un uso successivo.

    I file sono archivi di dati organizzati in contenitori chiamati directory, o cartelle, secondo una
    struttura ad albero chiamata File System.
    Ogni file all’interno di una cartella è identificato da un nome univoco.

    Se il contenuto di un file può essere interpretato come una sequenza di linee di testo elettronico,
    cioè sequenze di caratteri Unicode separate dal carattere di ritorno a capo (\n), si tratta di un file di testo,
    altrimenti è un file binario
"""



# --------------------------
# Write text file
# --------------------------
print("=" * 29 + " WRITE TXT FILE " + "=" * 29)
out_file = open("e:/tmp/foo.txt", "w")
out_file.write("Hello\n")
out_file.write("\n")
out_file.write("World!!!\n")
# Chiede al sistema operativo di trasferire i dati su file
out_file.flush()
out_file.close()

# --------------------------
# READ TEXT FILE (I)
# File content as a single String
# --------------------------
print("=" * 29 + " READ TEXT FILE (I) " + "=" * 29)
in_file = open("e:/tmp/foo.txt", "r")
a = in_file.read()
in_file.close()
print(type(a))
print(a)

# --------------------------
# READ TEXT FILE (II)
# File content as a List of String
# --------------------------
print("=" * 29 + " READ TEXT FILE (II) " + "=" * 29)
in_file = open("e:/tmp/foo.txt", "r")
a = in_file.readlines()
in_file.close()
print(type(a))
print(a)

# ---------------------------------------------------
# READ TEXT FILE (III)
# File content Line by Line (the long way)
# ---------------------------------------------------
print("=" * 29 + " READ TEXT FILE (III) " + "=" * 29)
in_file = open("e:/tmp/foo.txt", "r")

# the long way
while line := in_file.readline():
    print(type(line))
    print(line[:-1])    # oppure modifica l'end della funzione print
in_file.close()

# ---------------------------------------------------
# READ TEXT FILE (IV)
# File content Line by Line (the short way)
# Python Idiom
# ---------------------------------------------------
print("=" * 29 + " READ TEXT FILE (IV) " + "=" * 29)
in_file = open("e:/tmp/foo.txt", "r")

with open("e:/tmp/foo.txt") as f:
    for line in f:
        print(type(line))
        print(line[:-1]) # oppure modifica l'end della funzione print
