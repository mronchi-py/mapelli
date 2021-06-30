"""programma per aumentare la luminosità di un’immagine
(suggerimento: un metodo semplice è quello di aumentare,
andando verso il bianco, i valori delle componenti RGB)"""
from PIL import Image

AUMENTO = 128

image = Image.open("risorse/vienna.jpg")
pixels = list(image.getdata()) # Lista dei pixel dell'immagine

for i in range(len(pixels)): # Passa in rassegna tutti i pixel
    r, g, b = pixels[i]
    r = min(r + AUMENTO, 255)
    g = min(g + AUMENTO, 255)
    b = min(b + AUMENTO, 255)
    pixels[i] = (r, g, b) 

image.putdata(pixels) # Riversa i valori della lista nell'immagine (in memoria)
image.save("risorse/vienna_luminoso.png") # Salva l'immagine su file

image.show() # Apre l'immagine nel visualizzatore di immagini predefinito

