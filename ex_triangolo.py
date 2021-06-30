"""
    Affinché tre numeri possano essere le misure dei lati di un triangolo è
    necessario che siano tutti positivi e che ciascuno sia inferiore alla somma
    degli altri due
"""

a = float(input("Primo lato: "))
b = float(input("Secondo lato: "))
c = float(input("Terzo lato: "))

a_ok = a > 0 and a < b + c
b_ok = b > 0 and b < a + c
c_ok = c > 0 and c < a + b

if a_ok and b_ok and c_ok:
    print("I valori possono essere le misure dei lati di un triangolo")
else:
    print("I valori non possono essere le misure dei lati di un triangolo")