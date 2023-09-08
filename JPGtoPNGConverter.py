import sys
import os
from PIL import Image

# grab first and second argument
JPGimage_path= sys.argv[1]
PNGimage_folder = sys.argv[2]

# check is the PNG folder excist, if not create it
if not os.path.exists(PNGimage_folder):
	os.makedirs(PNGimage_folder)

for filename in os.listdir(JPGimage_path):
	img = Image.open(f"{JPGimage_path}{filename}")
	clean_name = os.path.splitext(filename)[0]
	img.save(f"{PNGimage_folder}/{clean_name}.png","png")
