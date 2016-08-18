# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:25:39 2016

@author: Julien
"""

from PIL import Image
from CellMatrix import Grid, Zelle, max_wert

#import numpy as np
#import scipy.misc as smp
#
## Create a 1024x1024x3 array of 8 bit unsigned integers
#data = np.zeros( (1024,1024,3), dtype=np.uint8 )
#
#data[512,512] = [254,0,0]       # Makes the middle pixel red
#data[512,513] = [0,0,255]       # Makes the next pixel blue
#
#img = smp.toimage( data )       # Create a PIL image
#img.show()                      # View in default viewer

def convert(matrix, zeilenlaenge, spaltenlaenge):
    """ int[][] -> (int r, int g, int b)[]
        Erstellt eine Tripelliste im rgb-Format aus einer 
        gegebenen Integermatrix"""
    temp = []
    for z in range(zeilenlaenge):
        for s in range(spaltenlaenge):
            temp.append(assign(matrix[z][s].wert))
    return temp
    

def assign(wert):
    """ int wert -> (int r, int g, int b)
        ordnet einem Integer Wert einer bestimmenten Farbe im rgb-Fomat zu"""
    # der int wert muss auf einen Dezimalwert zwischen [0, 1] gemappt werden
    if wert > 0:
        return (255, 0, 0)
    return (0, 0, 255)


def assign2(wert):
    """ int wert -> (int r, int g, int b)
        ordnet einem Integer Wert einer bestimmenten Farbe im rgb-Fomat zu"""
    # der int wert muss auf einen Dezimalwert zwischen [0, 1] gemappt werden
    m = max_wert
    a = (wert+m)/(float(max_wert)*2)
    return (255*a, 0, 255*(1-a))


#%%

if __name__ == "__main__":
    """Autmomatisierter Aufruf der Klassen. Vergleiche mit Java 'main'"""

    breite = 1024
    hoehe = 1024   
    radius = 3
    iterationen = 10

    g = Grid(hoehe, breite, radius)
    #g.print_grid()
    im= Image.new('RGB', (breite, hoehe))

    im.putdata(convert(g.grid, hoehe, breite))
    im.save('test.png')
    
    for i in range(iterationen):
        
        g.scan()
        g.write()
        
        im.putdata(convert(g.grid, hoehe, breite)) #benötigt eine liste mit tripeln (r, g, b)
        im.save('test%i.png' %i)

