# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:25:39 2016

@author: Julien
"""

from PIL import Image
from CellMatrix import Grid, max_wert

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
    
def convert2(matrix, zeilenlaenge, spaltenlaenge):
    """ int[][] -> (int r, int g, int b)[]
        Erstellt eine Tripelliste im rgb-Format aus einer 
        gegebenen Integermatrix"""
    temp = []
    for z in range(zeilenlaenge):
        for s in range(spaltenlaenge):
            temp.append(assign2(matrix[z][s].activator))
    return temp
    

def assign(wert):
    """ int wert -> (int r, int g, int b)
        ordnet einem Integer Wert einer bestimmenten Farbe im rgb-Fomat zu"""
    # der int wert muss auf einen Dezimalwert zwischen [0, 1] gemappt werden
    if wert > 0:
        return (255, 0, 0)
    return (0, 0, 255)


def assign_gradet(wert):
    """ int wert -> (int r, int g, int b)
        ordnet einem Integer Wert einer bestimmenten Farbe im rgb-Fomat zu"""
    # der int wert muss auf einen Dezimalwert zwischen [0, 1] gemappt werden
    m = max_wert
    a = (wert+m)/(float(max_wert)*2)
    return (255*a, 0, 255*(1-a))

def assign2(act):
    """ boolean act -> (int r, int g, int b)
        ordnet einem boolschen Wert einer bestimmenten Farbe im rgb-Fomat zu"""
    if act == 1:
        return (255, 255, 255)
    return (0, 0, 0)

#%%

if __name__ == "__main__":
    """Autmomatisierter Aufruf der Klassen. Vergleiche mit Java 'main'"""

    breite = input("Breite: ") # wie breit ist das Bild? (in Pixel)
    hoehe = input("Höhe: ")    # wie hoch ist das Bild? (in Pixel)
    chance = input("Chance: ") # wie Hoch ist die Chance, dass eine Zelle ein
                               # Aktivator ist? (also: 1/chance)
    print("\n1: keine Aktivatoren, nur Werte")
    print("2: Mit Aktivatoren und Innen- und Außenradius")    
    while True:        
        modus = input("Modus: ") #    
        
        if modus == 1:
            radius = input("Radius: ")
            # wie groß ist der Radius, wenn man ein einzelnes Quadrat betrachtet
            break            
            
        if modus == 2:
            innenradius = input("Innenradius: ")
            # Innenradius, für doppelten Kreis
            aussenradius = input("Außenradius: ")      
            # Außenradius, für doppelten Kreis
            break
        
    iterationen = input("Anzahl Iterationen: ")
    # Wie häufig wird der Algorithmus angewandt?
    
    
    g = Grid(hoehe, breite, chance)
    im= Image.new('RGB', (breite, hoehe))


    
    
    if modus == 1:
        

        im.putdata(convert2(g.grid, hoehe, breite))
        im.save('Generiert %i x %i Modus %i Radius %i Startbild.png' \
                %(breite, hoehe, modus, radius))        
        
        for i in range(iterationen):
            g.scan(radius)
            g.write()        
            
            im.putdata(convert(g.grid, hoehe, breite))
            im.save('Generiert %i x %i Modus %i Iteration %i.png' \
                    %(breite, hoehe, modus, i))

    elif modus == 2:
    
        im.putdata(convert2(g.grid, hoehe, breite))
        im.save('Generiert %i x %i Modus %i Ri %i Ra %i Startbild.png' \
                %(breite, hoehe, modus, innenradius, aussenradius))         
        
        for i in range(iterationen):
            g.scan2(innenradius, aussenradius)
            g.write2()        
            
            im.putdata(convert2(g.grid, hoehe, breite))
            im.save('Generiert %i x %i Modus %i Ri %i Ra %i Iteration %i.png' \
                    %(breite, hoehe, modus, innenradius, aussenradius, i)) 