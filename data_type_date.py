"""
    Calcola quanti giorni mancano a Natale
"""

# Importa dal modulo "datetime" il tipo "date"

from datetime import *
# from datetime import date


oggi = date.today()
natale = date(2021, 12, 25)  # Gli argomenti sono nella forma: "aaaa, mm, gg"
print("Oggi:", oggi)
print("Giorni a Natale:", natale - oggi)  # Sottrazione tra due date
