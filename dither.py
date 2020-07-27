from PIL import Image

OUTPUT_WIDTH=256
DITHER_SCALE=2

# 0 = black, 1 = white
BANDS = [[0,0,0,0],
         [1,0,0,0],
         [1,0,1,0],
         [1,1,1,0],
         [1,1,1,1]]

def put_pixels(img, x, y, s, values):
    for i in range(s):
        for j in range(s):
            img.putpixel((x*s+i, y*s+j), values[i*s+j])

img = Image.open("input_img.jpeg")

scale = OUTPUT_WIDTH/img.width
img = img.resize((OUTPUT_WIDTH, int(img.height*scale)))

dithered_img = Image.new('1', (img.width*2, img.height*2))

for x in range(img.width):
    for y in range(img.height):
        shade = sum(img.getpixel((x,y)))
        band_size = 766 / ((DITHER_SCALE*DITHER_SCALE)+1)
        i=0
        while i < DITHER_SCALE*DITHER_SCALE+1:
            if shade < band_size*(i+1):
                put_pixels(dithered_img, x, y, DITHER_SCALE, BANDS[i])
                i = 999
            else:
                i = i+1

img.show()
dithered_img.show()