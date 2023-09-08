from PIL import Image,ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
crooked = filtered_img.rotate(90)
crooked.save("rotetedPikachu.png","png")
resized = filtered_img.resize((300,300))
resized.save("resizedPikachu.png","png")
resized.show()
filtered_img.save('grayPikachu.png','png') # I converted the images to .png because it support the above filters, we may get errors using the jpg format
filtered_img.show() # it will show us the image

box=(100,100,400,400)
region = filtered_img.crop(box)
filtered_img.save("CroppedPikachu.png",'png')