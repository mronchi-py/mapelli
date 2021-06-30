"""
    Una parola è palindroma quando viene letta allo stesso modo da
    sinistra a destra e da destra a sinistra. Un esempio è “ANNA”

    String Slicing: ottenere parte di una stringa
"""

a = "pippo"
# | p(0, -5) | i(1, -4) | p(2, -3) | p(3, -2) | o(4, -1) |

# String slicing
print(a[0:])
print(a[-5:])
print(a[::-1])


# --------------------------------------
# Using construtto-for (1)
# aggiungo caratteri in coda
# --------------------------------------
print("=" * 79)
b = ""
for i in range(len(a) - 1, -1, -1):
    b = b + a[i]
print(b)
print(b == a)

# --------------------------------------
# Using construtto-for (2)
# aggiungo caratteri in testa
# --------------------------------------
print("=" * 79)
b = ""
for i in range(len(a)):
    b = a[i] + b
print(b)
print(b == a)

# --------------------------------------
# Using String Slicing
# --------------------------------------
print("=" * 79)
b = a[::-1]
print(b)
print(b == a)

# algo piu' efficiente
# # ... si interrompe alla prima disuguaglianza
