"""Programma per convertire un'immagine in negativo"""
from PIL import Image

if __name__ == "__main__":
    in_filename = "risorse/kingfisher.jpg"
    index = in_filename.find(".") # Posizione del carattere "."
    out_filename = in_filename[:index] +"_negativo.png"
    image = Image.open(in_filename)
    pixels = list(image.getdata())

    for i in range(len(pixels)):
        r, g, b = pixels[i]
        media = (r + g + b) // 3
        media_inversa = 255 - media
        pixels[i] = (media_inversa, media_inversa, media_inversa)

    image.putdata(pixels)
    image.save(out_filename)
    image.show() # Apre l'immagine nel visualizzatore di immagini predefinito

    out_filename = in_filename[:index] +"_inversa.png"
    image = Image.open(in_filename)
    pixels = list(image.getdata())

    for i in range(len(pixels)):
        r, g, b = pixels[i]
        pixels[i] = (255 - r, 255 - g, 255 - b)

    image.putdata(pixels)
    image.save(out_filename)
    image.show() # Apre l'immagine nel visualizzatore di immagini predefinito
