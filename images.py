from PIL import Image,ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.save('grayPikachu.png','png') # I converted the images to .png because it support the above filters, we may get errors using the jpg format

