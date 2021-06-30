# il modulo e' dateutil.utils
# se importo senza esplicitare le funzioni
# devo referenziarle indicando il modulo...

# from dateutil.utils import *
import dateutil.utils

# built-in function
# https://docs.python.org/3/library/functions.html
#

print('Hello World!!!')

# Multi-line string.... barbatrucco per multi-line comments
print("""aaaa
bbb
ccc
""")

# ---------------------------------
# Data Types
# ---------------------------------
print("=" * 29 + " DATA TYPES " + "=" * 29)
a = 10
print(type(a))
a = 10.0
print(type(a))
a = "Sarah"
print(type(a))
a = True
print(type(a))
a = dateutil.utils.today()  # a = today()
print(type(a))
print(a)

# ---------------------------------
# espressioni
# ---------------------------------
print("=" * 29 + " ESPRESSIONI " + "=" * 29)
a = 8 + 9
print(a)
print(type(a))

a = 8.0 + 9.0
print(a)
print(type(a))

a = 10 > 9
print(a)
print(type(a))

# ---------------------------------
# formatted print
# ---------------------------------
print("=" * 29 + " ESPRESSIONI " + "=" * 29)
a = "foo"
print("{a}")  # "std" print
print(f"{a}")  # formatted print

# concetto di template e placeholder (segnaposto)
template = "Il mio nome è {} e vivo a {}"
print(template.format("Marco", "Monza"))
