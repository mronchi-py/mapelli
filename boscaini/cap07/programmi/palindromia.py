"""Programma che verifica se le frasi sono palindrome"""
from inversa import inversa

def is_palindroma(s):
    """Ritorna True se la stringa specificata è palindroma
    non differenziando maiuscole e minuscole e non tenendo conto degli spazi"""
    # Rimuovi gli spazi e converti in minuscolo s e la sua inversa
    s1 = s.replace(" ", "").lower() 
    s2 = inversa(s).replace(" ", "").lower()
    return s1 == s2

if __name__ == '__main__':
    print("Monty Python:", inversa("Monty Python"))
    print("Anna:", is_palindroma("Anna"))
    print(is_palindroma("O mordo tua nuora o aro un autodromo")) # Quasi inquietante!
    print("A iosa la soia:", is_palindroma("A iosa la soia"))
    print("I topi non avevano nipoti:", is_palindroma("I topi non avevano nipoti"))
