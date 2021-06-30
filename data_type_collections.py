"""
- Range -> range()
- Liste -> []
- Tuple ->  ()
- Set -> {}
- Dictionary -> {k:v}
"""
import sys

# ----------------------------------------------------------
# Range: intervallo numerico (ordinato per posizione)
# range(start, stop, step)
# ----------------------------------------------------------
print("=" * 29 + " RANGE: INTERVALLO NUMERICO, ORDINATO PER POSIZIONE " + "=" * 29)
a = range(5)  # range(0,5,1) => 0,1,2,3,4 => 0(0),1(1),2(2),3(3),4(4) => 0(0,-5),1(1,-4),2(2,-3),3(3,-2),4(4,-1)
print(type(a))
print("Elemento in pos 2:", a[2])
print("Elemento in pos -4 ", a[-4])

# range2list
a = range(1, 15, 2)  # 1(0,-7),3(1,-6),5(2,-5),7(3,-4),9(4,-3), 11(5,-2), 13(6,-1)
print("Elemento in pos 2:", a[2])
print("Elemento in pos -5:", a[-3])
b = list(a)
print("range2list #2", b)

# ----------------------------------------------------------
# List: Elenco eterogeneo, ordinato per posizione
# ----------------------------------------------------------
print("=" * 29 + " LIST: ELENCO ETEROGENEO, ORDINATO PER POSIZIONE " + "=" * 29)
a = ["Roma", "Oslo", "Lisbona", "Reykjavik", 234, 'Roma']
print(type(a))
print(a)

# ----------------------------------------------
# Set: Insieme => no ordine, no duplicati
# ----------------------------------------------
print("=" * 29 + " SET: INSIEME => NO ORDINE, NO DUPLICATI " + "=" * 29)
a = {1, 5, 733, 56, 5}
print(type(a))
print(a)

# --------------------------------------------
# Dictionary (Map,Array Associativo,...)
# --------------------------------------------
print("=" * 29 + " DICTIONARY (MAP,ARRAY ASSOCIATIVO,...) " + "=" * 29)
a = {"f": "Flash", "t": "Tempesta", "h": "Hulk"}
print(type(a))
print(a)
# Elenco chiavi e Valori
print(a.keys())
print(a.values())

# get Value from keys
print(a["t"])

# Aggiunta/Cancellazione Elementi
a["s"] = "Superman"
del a["t"]
try:
    print(a["t"])
except KeyError:
    print("Chiave non presente nel Dictionary")
except:
    print("*" * 79)
    print("Error: ", sys.exc_info()[0], "occurred.")
    print("*" * 79)
