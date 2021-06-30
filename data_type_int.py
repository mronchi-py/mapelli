"""
Sistemi numerici posizionali
- decimale: 10
- esadecimale: 16
- binario: 2

3 rappresentazioni diverse dello stesso numero (intero) 4783
"""

# Decimale
a = 4783
print(type(a))
print("Rappresentazione decimale " + str(a))

# Esadecimale
a = 0x12AF
print(type(a))
print("Rappresentazione decimale " + str(a))

# Binario
a = 0b1001010101111
print(type(a))
print("Rappresentazione decimale: " + str(a))

# -------------------------
# CONVERSIONI
# -------------------------
print("=" * 29 + " CONVERSIONI " + "=" * 29)
# Decimale -> Esadecimale
print(hex(4783))
# Decimale -> Binario
print(bin(4783))

# -------------------------
# OPERATORI ARITMETICI
# -------------------------
print("=" * 29 + " OPERATORI ARITMETICI " + "=" * 29)
print(7 + 3)
print(7 - 3)
print(7 * 3)
print(7 / 3)
print(7 // 3)  # divisione intera
print(7 % 3)  # MODULO: resto divisione intera
print(2 ** 3)  # elevamento a potenza
