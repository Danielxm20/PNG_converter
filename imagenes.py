from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')

filtered_img = img.filter(ImageFilter.SHARPEN)

filtered_img.save("blur.png", 'png')

grey_img = img.convert('L') # convierte la imagen a gris
rotar = grey_img.rotate(180) # gira la imagen en grados
rotar = grey_img.resize((300,300)) # cambia el tamaño, el tamaño deseado se pasa como tupla 
rotar.save("grey.png", 'png')
#grey_img.show() # abre la imageb

box = (100, 100, 400, 400)
region = grey_img.crop(box) # recorta la imagen 
region.save("recortado.png", 'png')

print(img)
print(img.format)
print(img.size)
print(img.mode)
#print(dir(img))