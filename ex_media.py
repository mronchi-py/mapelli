"""
    Calcolare la media di 2 numeri inseriti da stdin

    Operazioni Matematiche
    Gestione Eccezioni
"""

# ========================
# Versione I
# ========================
# Conversione da str a floats
a = float(input("Inserire il Primo Numero: "))
b = float(input("Inserire il Secondo Numero: "))

print("La media e' " + str((a + b) / 2))

# =======================================
# Versione II
# leggermente piu' robusto...
# costrutto try-except
# =======================================
print("=" * 79)
try:
    a = float(input("Inserire il Primo Numero: "))
    b = float(input("Inserire il Secondo Numero: "))
    print("La media e' " + str((a + b) / 2))
except:
    print("Please, insert a numeric value...")
