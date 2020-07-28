from PIL import Image
import random

"""
Generate random patterns blocks of for use with pattern dithering

Args:
    s: The width (and height) of pattern blocks to be generated

Returns:
    A 2D array of pattern blocks. The array will have (s*s)+1 elements corresponding to each shade
"""
def generate_random_pattern_blocks(s):
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

"""
Put a square block of pixels starting at a given top-left corner position

Args:
    img: PIL Image object for the pixels to be put in
    x: x-coordinate of top-left corner of block
    y: y-coordinate of top-left corner of block
    s: Width of the block
    pixels: Array of pixels to be placed (should contain s*s elements)
"""
def put_pixels(img, x, y, s, pixels):
    for i in range(s):
        for j in range(s):
            img.putpixel((x*s+i, y*s+j), pixels[i*s+j])

def main():
    OUTPUT_WIDTH=256
    DITHER_SCALE=2
    BLOCKS = generate_random_pattern_blocks(DITHER_SCALE)

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

if __name__ == "__main__":
    main()