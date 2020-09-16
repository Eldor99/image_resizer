import sys
import os
import random
from PIL import Image

image_file = sys.argv[1]
height = sys.argv[2]
width = sys.argv[3]
random = random.randint(0,1000)

if not os.path.exists('new'):
	os.makedirs('new')


img = Image.open(f'{image_file}')
resize = img.resize((int(height),int(width)))
resize.save(f'new/resized{random}.jpg','JPEG')
