"""
    Gestione degli errori.
    Costrutto: try-except-else-finally
"""


# esempio di definizione di funzione ricorsiva
def fattoriale(n):
    """ restituisce il fattoriale di n
    :rtype: int
    """
    if n == 1:
        return 1
    return n * fattoriale(n - 1)


try:
    print(fattoriale(4))
except:
    print("run-time error")
else:
    print("no run-time error")
finally:
    print("always executed: free locked resources")

# gestisco in modo diverso i diversi tipi di eccezione
# ValueError
# ZeroDivisionError

