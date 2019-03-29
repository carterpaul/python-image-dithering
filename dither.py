from PIL import Image

img = Image.open("input_img.jpeg")
size = img.size

img = img.convert(mode='L', dither=0).resize((size[0]//4, size[1]//4))
