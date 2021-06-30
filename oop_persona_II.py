"""
    Modello per gli oggetti (istanza) di tipo Persona
"""


class Persona:

    # Costruttore. Metodo Speciale (DUNDER: double underscore)
    def __init__(self, nome, cognome):
        self.nome = nome  # attributo nome
        self.cognome = cognome  # attributo cognome

    # Metodi
    def description(self):
        #        return self.nome + " " + self.cognome
        return f"{self.nome} {self.cognome}"

    def __str__(self):
        """ sulla conversione a stringa  """
        return f"{self.nome} {self.cognome}"

    def __repr__(self):
        """ rappresentazione JSON dell'istanza """
        return f"{{\"nome\": \"{self.nome}\", \"cognome\": \"{self.cognome}\"}}"


if __name__ == '__main__':
    mario = Persona("Mario", "Rossi")

    # DUNDERs
    print("=" * 79)
    # oggetto di classe Person memorizzato all'indirizzo di memoria 0x00....
    # oppure viene invocato in modo automatico il DUNDE __str__()
    # e se non e' stato implementato il DUNDE __repr__()
    print(mario)
    print(mario.__str__())  # invocazione eplicita sull'istanza
    print(Persona.__str__(mario))  # invocazione eplicita sulla classe

    print(repr(mario))  # oggetto di classe Person memorizzato all'indirizzo di memoria 0x00....
    print(mario.__repr__())  # oggetto di classe Person memorizzato all'indirizzo di memoria 0x00....
    print(Persona.__repr__(mario))  # oggetto di classe Person memorizzato all'indirizzo di memoria 0x00....
