def cripta_farfallino2(messaggio):
    """Dato un messaggio ne ritorna una versione criptata
    secondo una version semplice dell'alfabeto farfallino."""
    messaggio_criptato = ""    

    for car in messaggio:
        if car in "aeiou":
            messaggio_criptato += "f"+ car 
        elif car in "AEIOU":
            messaggio_criptato += "F"+ car 
        else:
            # Ricopia così com'è tutto ciò che non è una vocale
            messaggio_criptato += car             

    return messaggio_criptato

def decripta_farfallino2(messaggio):
    """Dato un messaggio criptato ritorna il corrispondente messaggio originale"""
    messaggio_decriptato = messaggio    

    for codice in ("fa", "fe", "fi", "fo", "fu", "FA", "FE", "FI", "FO", "FU"):
        vocale = codice[1]
        messaggio_decriptato = messaggio_decriptato.replace(codice, vocale)            

    return messaggio_decriptato

frase = "Effetto farfalla e teoria del caos"
print(cripta_farfallino2(frase))
print(decripta_farfallino2(cripta_farfallino2(frase)))

