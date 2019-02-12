from PIL import Image
import random
import os

os.chdir('C:\\Users\\banban\\Desktop\\bchallenge\\pc\\basicChallenge\\imgs')

# make the picture of result
def ansPicture():
    dark_list = [(47, 79, 79),(105, 105, 105),(112, 128, 144),(72,61,139),(0, 0, 0),(139, 119 ,101),(139, 90 ,43),(0, 100, 0),(	25,25,112),(128,0,128)]
    imgs = Image.open('heart.png')
    width, height = imgs.size
    dark_img = imgs

    for y in range(height):
        for x in range(width):
            pixel = imgs.getpixel((x, y))
            # print(pixel)
            if pixel == (255, 255, 255,255):
                dark_img.putpixel((x, y), random.choice(dark_list))
        # break
    dark_img.save('pink_heart.png')

def quesPicture():
    # make the html picture
    img = Image.open('pink_heart.png')
    width, height = img.size
    pheart = img
    for y in range(height):
        colors = [img.getpixel((x,y)) for x in range(width)]
        plist = [c for c in colors if c == (255,0,255,255)]
        pink_len = len(plist)
        rest_color = colors[pink_len:]
        random.shuffle(rest_color)
        i = random.randint(0,width)
        mix_colors = rest_color[:i] + [(255,0,255)]*pink_len + rest_color[i:]
        # print(mix_colors)
        # break
        for x in range(width):
            pheart.putpixel((x,y), mix_colors[x])
    pheart.save("pheart.png")

ansPicture()
quesPicture()






