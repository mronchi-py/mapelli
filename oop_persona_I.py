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


if __name__ == '__main__':
    mario = Persona("Mario", "Rossi")

    print(type(mario))
    print(id(mario), ' -> ', hex(id(mario)))
    print(mario)

    print("ACCESSO AD ATTRIBUTO: " + mario.nome)
    print("CHIAMATA METODO DALL'ISTANZA: " + mario.description())
    print("CHIAMATA METODO DALLA CLASSE: " + Persona.description(mario))
