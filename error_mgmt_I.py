"""
    Concetto di Exit Code: exit(n)
"""

print("=" * 79)

try:
    raise Exception('Sollevo un Exception...')
except:
    print("Exception Catturata")

