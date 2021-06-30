"""Programma che converte un'immagine RGB in bianco e nero e in scala di grigi"""
from PIL import Image, ImageFont, ImageDraw

def scrivi2(image, testo, x, y, font_filename, colore1="black", colore2="red"):
    """Disegna un testo a partire da (x, y) col font indicato"""
    font = ImageFont.truetype(font_filename, 60) # Font con tipo e dimensione
    draw = ImageDraw.Draw(image)
    draw.text((x, y), testo, font=font, fill=colore1)
    draw.text((x + 1, y + 1), testo, font=font, fill=colore2)

if __name__ == "__main__":
    in_filename = "risorse/agnese.jpg"
    index = in_filename.find(".") # Posizione del carattere "."
    basename = in_filename[:index]
    font_filename = "risorse/AlexBrush-Regular-OTF.otf"
    image = Image.open(in_filename)

    imageGrey = image.convert('L') # Crea un'immagine in scala di grigi...
    # ...quindi, la scritta non sarà in giallo, ma in un grigio chiaro
    scrivi2(imageGrey, "Scala di grigi", 50, 350, font_filename, colore2="yellow")
    imageGrey.save(basename +"_Grey.png")

    imageBW = image.convert('1') # Converte l'immagine in bianco e nero
    imageBW = imageBW.convert('RGB') # Riconverte l'immagine in RGB così che...
    # ...il testo che verrà disegnato da scrivi2() manterrà i colori specificati
    scrivi2(imageBW, "Bianco\ne nero", 15, 30, font_filename, colore1="grey")
    imageBW.save(basename +"_BW.png")

    imageBW.show() # Apre l'immagine nel visualizzatore di immagini predefinito
    imageGrey.show() # Apre l'immagine nel visualizzatore di immagini predefinito

