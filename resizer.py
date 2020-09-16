from PIL import Image

img = Image.open('./image/pikachu.jpg')
resize = img.resize((300,300))
resize.save('resized.jpg','JPEG')