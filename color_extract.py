#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
data: 2020/4/3
author: dilake@weierai.com
describe: extract main color from image
'''
from PIL import Image
import numpy as np
import time

def HSVDistance(hsv_1,hsv_2):
    H_1,S_1,V_1 = hsv_1
    H_2,S_2,V_2 = hsv_2
    R=100
    angle=30
    h = R * math.cos(angle / 180 * math.pi)
    r = R * math.sin(angle / 180 * math.pi)
    x1 = r * V_1 * S_1 * math.cos(H_1 / 180 * math.pi)
    y1 = r * V_1 * S_1 * math.sin(H_1 / 180 * math.pi)
    z1 = h * (1 - V_1)
    x2 = r * V_2 * S_1 * math.cos(H_2 / 180 * math.pi)
    y2 = r * V_2 * S_1 * math.sin(H_2 / 180 * math.pi)
    z2 = h * (1 - V_2)
    dx = x1 - x2
    dy = y1 - y2
    dz = z1 - z2
    return math.sqrt(dx * dx + dy * dy + dz * dz)

def ColourDistance(rgb_1, rgb_2):
     R_1,G_1,B_1 = rgb_1
     R_2,G_2,B_2 = rgb_2
     rmean = (R_1 +R_2 ) / 2
     R = R_1 - R_2
     G = G_1 -G_2
     B = B_1 - B_2
     return math.sqrt((2+rmean/256)*(R**2)+4*(G**2)+(2+(255-rmean)/256)*(B**2))


def get_theme_color(image):
    image = image.convert('RGBA')
    im = image.quantize().getpalette()
    #print(im)
    im = np.array(im).reshape((-1, 3))
    #print(im.shape)
    theme_rgb = im[0]
    return theme_rgb

image  = Image.open('1.png')
start = time.time()
theme_rgb = get_theme_color(image)
end = time.time()
print(theme_rgb,image.width, image.height,end-start)

#def color_extract(image):
