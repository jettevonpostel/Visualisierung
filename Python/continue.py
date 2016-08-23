# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 07:42:46 2016

@author: Julien
"""

# zum Einlesen der Dateien
# noch im Aufbau derzeit ist die Datei nur zur Erinnerung

from PIL import Image
from CellMatrix import Grid, Zelle

im = Image.open("100 x 100 Modus 4 Chance 14 Ai 5 Bi 5 Aa 10 Ba 10 Iteration 9.png") #Can be many different formats.
pix = im.load()
print im.size #Get the width and hight of the image for iterating over


im = Image.open("1920 x 1080 Modus 3 Chance 15 Ai 8 Bi 4 Aa 8 Ba 14 Iteration 19.png") #Can be many different formats.
pix = im.load()
print im.size # (breite, höhe)

print pix[1920-1, 1080-1] # (r, g, b)


# -erstelle neues Grid


#print pix[x,y] #Get the RGBA Value of the a pixel of an image
#pix[x,y] = value # Set the RGBA Value of the image (tuple)