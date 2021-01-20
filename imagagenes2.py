from PIL import Image, ImageFilter

img = Image.open("./pokedex/astro.jpg ")
img.thumbnail((400, 400)) # modifica la imagen original, manteniendo el aspect ratio con los valores maximos
img.save("modificada.jpg")

print(img.size)
