from PIL import Image
import math
# Sama as NPCR both are used for sensitivity analysis two encrypted image is required


def uaci(loc1,loc2):
    image1 = Image.open(loc1)
    image2 = Image.open(loc2)
    pixel1=image1.load()
    pixel2=image2.load()
    width,height=image1.size
    value=0.0
    for y in range(0,height):
        for x in range(0,width):
            value=(abs(pixel1[x,y][0]-pixel2[x,y][0])/255)+value

    value=(value/(width*height))*100
    return value

#print(uaci("encrypted16.png","encrypted116.png"))

#decrypted image and original image


def rootmeansquareerror(loc1,loc2):
    image1 = Image.open(loc1)
    image2 = Image.open(loc2)
    pixel1 = image1.load()
    pixel2 = image2.load()
    width, height = image1.size
    value1 = 0.0
    value2=0.0
    value3=0.0

    #comparing of pixel values between two images
    for y in range(0,height):
        for x in range(0,width):
            value1=((pixel1[x,y][0]-pixel2[x,y][0])**2)+value1
            value2 = ((pixel1[x, y][1] - pixel2[x, y][1]) ** 2) + value2
            value3 = ((pixel1[x, y][2] - pixel2[x, y][2]) ** 2) + value3
    value1=value1/(height*width)

    return (value1+value2+value3)/3

# def psnr(rmse):
#     value=(math.log10(255)*20)-(math.log10(rmse)*10)
#     return value
#
