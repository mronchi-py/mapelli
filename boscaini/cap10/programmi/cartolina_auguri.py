"""Programma che ruota un'immagine"""
from PIL import Image, ImageFont, ImageDraw

def scrivi(testo, x, y, font_filename, colore="yellow"):
    """Disegna un testo a partire da (x, y) col font indicato"""
    font = ImageFont.truetype(font_filename, 100) # Imposta il font con dimensione 100
    draw = ImageDraw.Draw(image)
    draw.text((x, y), testo, font=font, fill="black")
    draw.text((x + 2, y + 2), testo, font=font, fill=colore)

if __name__ == "__main__":
    in_filename = "risorse/cartolina.jpg"
    index = in_filename.find(".") # Posizione del carattere "."
    out_filename = in_filename[:index] +"_finale.jpg"
    font_filename = "risorse/AlexBrush-Regular-OTF.otf"
    angolo = int(input("Angolo di rotazione in gradi? "))
    image = Image.open(in_filename)
    image = image.rotate(angolo) # Ruota l'immagine dell'angolo specificato
    scrivi("Agnese\ne Lorenzo", 20, 0, font_filename)
    scrivi("marzo 2017", 490, 0, font_filename, colore="red")
    scrivi("Buon compleanno", 365, 525, font_filename, colore="#82eae1")
    image.save(out_filename) # Salva l'immagine su file
    image.show() # Apre l'immagine nel visualizzatore di immagini predefinito
