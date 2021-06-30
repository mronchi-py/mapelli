"""Programma per convertire un'immagine in scala di grigi"""
from PIL import Image

if __name__ == "__main__":
    in_filename = "risorse/lorenzo.jpg"
    index = in_filename.find(".") # Posizione del carattere "."
    out_filename = in_filename[:index] +"_grey.png"
    image = Image.open(in_filename)
    pixels = list(image.getdata())

    for i in range(len(pixels)):
        r, g, b = pixels[i]
        media = (r + g + b) // 3
        pixels[i] = (media, media, media)

    image.putdata(pixels)
    image.save(out_filename)
    image.show() # Apre l'immagine nel visualizzatore di immagini predefinito
