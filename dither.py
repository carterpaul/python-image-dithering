from PIL import Image
import random

OUTPUT_WIDTH=256
DITHER_SCALE=3

def generate_blocks(s):
    blocks = []
    for i in range((s*s)+1):
        indeces = random.sample(range(s*s), i)
        block = []
        for j in range((s*s)):
            if j in indeces:
                block.append(1)
            else:
                block.append(0)
        blocks.append(block)
    return blocks

BLOCKS = generate_blocks(DITHER_SCALE)
print(BLOCKS)

def put_pixels(img, x, y, s, values):
    for i in range(s):
        for j in range(s):
            img.putpixel((x*s+i, y*s+j), values[i*s+j])

img = Image.open("input_img.jpeg")

scale = OUTPUT_WIDTH/img.width
img = img.resize((OUTPUT_WIDTH, int(img.height*scale)))

dithered_img = Image.new('1', (img.width*DITHER_SCALE, img.height*DITHER_SCALE))

for x in range(img.width):
    for y in range(img.height):
        shade = sum(img.getpixel((x,y)))
        band_size = 766 / ((DITHER_SCALE*DITHER_SCALE)+1)
        i=0
        while i < DITHER_SCALE*DITHER_SCALE+1:
            if shade < band_size*(i+1):
                put_pixels(dithered_img, x, y, DITHER_SCALE, BLOCKS[i])
                i = 999
            else:
                i = i+1

img.show()
dithered_img.show()