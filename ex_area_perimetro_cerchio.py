import math
"""
    Calcola l'area e il perimetro di un cerchio dato il suo raggio.
"""


# ---------------------
# Versione 1
# ---------------------
r = float(input("Raggio: "))

perimetro = 2 * math.pi * r
area = math.pi * r * r

print("Circonferenza:", round(perimetro, 2))
print("Area:", round(area, 2))


# -----------------------------------------------
# Versione 2: Validazione Input
# -----------------------------------------------
try:
    r = float(input("Raggio: "))

    perimetro = 2 * math.pi * r
    area = math.pi * r * r

    print("Circonferenza:", round(perimetro, 2))
    print("Area:", round(area, 2))
except:
    print("Valore inserito non valido!")

