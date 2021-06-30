"""Crea un indice analitico (con il numero di riga) di una lista di parole"""
def indice_analitico(filename, parole):
    """Ritorna un dizionario con la seguente struttura: parola:[n1, n2,...]
    dove n1, n2, etc. sono i numeri di riga dove compare la parola"""
    indice = {}
    n_linea = 1
    
    for linea in open(filename):
        for parola in parole:            
            if parola.lower() in linea.lower(): # Non differenzia maiuscole/minuscole
                if parola not in indice:
                    indice[parola] = [n_linea]
                else:
                    indice[parola].append(n_linea)
        n_linea += 1
    return indice                
        
if __name__ == '__main__':
    parole = ['Renzo', 'Lucia', 'don Abbondio', 'fra Cristoforo', 'don Rodrigo']
    indice = indice_analitico("i_promessi_sposi.txt", parole)
    for parola, numeri_linee in indice.items():
        print("{:<20}{:5,d}".format(parola, len(numeri_linee)))
    print(indice['fra Cristoforo']) # Stampa i numeri di riga dove compare fra Cristoforo
