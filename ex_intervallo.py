"""
    Operatori di Confronto + Operatori Booleani

    Verificare se un numero appartiene ad un dato intervallo
"""

START = 10
END = 35

valore = float(input("Inserire un valore tra 10 e 35: "))

if valore < START or valore > END:
    print("Valore Esterno")
else:
    print("Valore Interno")
