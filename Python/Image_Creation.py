# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:25:39 2016

@author: Julien
"""

from PIL import Image
from CellMatrix import Grid, max_wert
import os

def create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


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


#def assign_gradet(wert):
#    """ int wert -> (int r, int g, int b)
#        ordnet einem Integer Wert einer bestimmenten Farbe im rgb-Fomat zu"""
#    # der int wert muss auf einen Dezimalwert zwischen [0, 1] gemappt werden
#    m = max_wert
#    a = (wert+m)/(float(max_wert)*2)
#    return (255*a, 0, 255*(1-a))


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
    print("2: Mit Aktivatoren und Innen- und Außenradius (Kreis)") 
    print("3: Mit Aktivatoren und Innen- und Außenradius (Ellipse)")
    print("4: Mit Aktivatoren und Innen- und Außenradius (Rechteck)")
    print("a1: Mit Aktivatoren und Innen- und Außenradius (Rotierte Rechtecke)")
    print("a2: Mit Aktivatoren und Innen- und Außenradius (Halbe Ellipse)")
    print("a3: Mit Aktivatoren und Innen- und Außenradius (Rotierte Ellipsen)")    
    
    while True:        
        modus = raw_input("Modus: ")    
        
        if modus == "1":
            radius = input("Radius: ")
            # wie groß ist der Radius, wenn man ein einzelnes Quadrat betrachtet
            break            
            
        if modus == "2":
            innenradius = input("Innenradius: ")
            # Innenradius, für doppelten Kreis
            aussenradius = input("Außenradius: ")      
            # Außenradius, für doppelten Kreis
            break
        
        if modus == "3":
            ai = input("Horizontale Innenhauptachse: ")
            bi = input("Vertikale Innenhauptachse: ")
            aa = input("Horizontale Außenhauptachse: ")
            ba = input("Vertikale Außenhauptachse: ")
            break
    
        if modus == "4":
            ai = input("Horizontale Innenseitenhälfte: ")
            bi = input("Vertikale Innenseitenhälfte: ")
            aa = input("Horizontale Außenseitenhälfte: ")
            ba = input("Vertikale Außenseitenhälfte: ")
            break        
        
        if modus == "a1":
            ai = input("Horizontaler Innenradius: ")
            bi = input("Vertikaler Innenradius: ")
            wi = input("Winkel des Innenrechtecks: ")
            aa = input("Horizontaler Außenradius: ")
            ba = input("Vertikaler Außenradius: ")
            wa = input("Winkel des Außenrechtecks: ")
            break
        
        if modus == "a2":
            ai = input("Horizontale Innenhauptachse: ")
            bi = input("Vertikale Innenhauptachse: ")
            aa = input("Horizontale Außenhauptachse: ")
            ba = input("Vertikale Außenhauptachse: ")
            ausrichtung = input("Ausrichtung: ")
            break
        
        if modus == "a3":
            ai = input("Horizontale Innenhauptachse: ")
            bi = input("Vertikale Innenhauptachse: ")
            wi = input("Winkel der Innenellipse: ")
            aa = input("Horizontale Außenhauptachse: ")
            ba = input("Vertikale Außenhauptachse: ")
            wa = input("Winkel der Außenellipse: ")
            break
        
    iterationen = input("Anzahl Iterationen: ")
    # Wie häufig wird der Algorithmus angewandt?
    
    
    g = Grid(hoehe, breite, chance)
    im= Image.new('RGB', (breite, hoehe))

    path = os.path.dirname(__file__) + "/Generierte Bilder/"

#%%
    
    if modus == "1":
        
        path = path + '%i x %i Modus %s Radius %i/' \
               %(breite, hoehe, modus, radius)
               
        create_path(path)
        
        im.putdata(convert(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Radius %i Startbild.png' \
                %(breite, hoehe, modus, radius))        
        
        for i in range(iterationen):
            g.scan(radius)
            g.write()        
            
            im.putdata(convert(g.grid, hoehe, breite))
            im.save(path + '%i x %i Modus %s Iteration %i.png' \
                    %(breite, hoehe, modus, i))
                    
#%%
                    

    elif modus == "2":
        
        path = path + '%i x %i Modus %s Chance %i Ri %i Ra %i/' \
                %(breite, hoehe, modus, chance, innenradius, aussenradius)
                
        create_path(path)
    
        im.putdata(convert2(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Chance %i Ri %i Ra %i Startbild.png' \
                %(breite, hoehe, modus, chance, innenradius, aussenradius))         
        
        for i in range(iterationen):
            g.scan2(innenradius, aussenradius)
            g.write2()        
            
            im.putdata(convert2(g.grid, hoehe, breite))
            im.save(path + \
                    '%i x %i Modus %s Chance %i Ri %i Ra %i Iteration %i.png' \
                    %(breite, hoehe, modus, chance, innenradius, \
                      aussenradius, i)) 
                    
#%%
                    
    elif modus == "3":
        
        path = path + '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i/' \
                %(breite, hoehe, modus, chance, ai, bi, aa, ba)
                
        create_path(path)
        
        im.putdata(convert2(g.grid, hoehe, breite))
        folder = ''
        im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i ' \
                %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                'Startbild.png')         
        
        for i in range(iterationen):
            g.scan3(ai, bi, aa, ba)
            g.write2()        
            
            im.putdata(convert2(g.grid, hoehe, breite))
            im.save(path + \
                    '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i' \
                    %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                    ' Iteration %i.png' %i)
                    
#%%
                    
    elif modus == "4":
        
        path = path + '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i/' \
                %(breite, hoehe, modus, chance, ai, bi, aa, ba)
                
        create_path(path)
        
        im.putdata(convert2(g.grid, hoehe, breite))
        folder = ''
        im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i ' \
                %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                'Startbild.png')         
        
        for i in range(iterationen):
            g.scan4(ai, bi, aa, ba)
            g.write2()        
            
            im.putdata(convert2(g.grid, hoehe, breite))
            im.save(path + \
                    '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i' \
                    %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                    ' Iteration %i.png' %i)

#%%         
        
    elif modus == "a1":
        
        path = path + '%i x %i Modus %s Chance %i Ai %i Bi %i Wi %i' \
                %(breite, hoehe, modus, chance, ai, bi, wi) +\
                'Aa %i Ba %i Wa %i/' %(aa, ba, wa)
                
        create_path(path)
        
        im.putdata(convert2(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Wi %i' \
                %(breite, hoehe, modus, chance, ai, bi, wi) +\
                'Aa %i Ba %i Wa %i Startbild.png' %(aa, ba, wa))
        
        for i in range(iterationen):
            g.scan_async1(ai, bi, wi, aa, ba, wa)
            g.write2()        
            
            im.putdata(convert2(g.grid, hoehe, breite))
            im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Wi %i' \
                    %(breite, hoehe, modus, chance, ai, bi, wi) +\
                    ' Aa %i Ba %i Wa %i Iteration %i.png' %(aa, ba, wa, i))


#%%                  
                    
    elif modus == "a2":
        
        path = path + '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i ' \
                %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                'Ausrichtung %i/' %ausrichtung
                
        create_path(path)
        
        im.putdata(convert2(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i ' \
                %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                'Ausrichtung %i Startbild.png' %ausrichtung)         
        
        for i in range(iterationen):
            g._async2(ai, bi, aa, ba, ausrichtung)
            g.write2()        
            
            im.putdata(convert2(g.grid, hoehe, breite))
            im.save(path + \
                    '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i' \
                    %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                    ' Ausrichtung %i Iteration %i.png' %(ausrichtung, i))
  

                  
#%%         
        
    elif modus == "a3":
        
        path = path + '%i x %i Modus %s Chance %i Ai %i Bi %i Wi %i' \
                %(breite, hoehe, modus, chance, ai, bi, wi) +\
                'Aa %i Ba %i Wa %i/' %(aa, ba, wa)
                
        create_path(path)
        
        im.putdata(convert2(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Wi %i' \
                %(breite, hoehe, modus, chance, ai, bi, wi) +\
                'Aa %i Ba %i Wa %i Startbild.png' %(aa, ba, wa))
        
        for i in range(iterationen):
            g._async3(ai, bi, wi, aa, ba, wa)
            g.write2()        
            
            im.putdata(convert2(g.grid, hoehe, breite))
            im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Wi %i' \
                    %(breite, hoehe, modus, chance, ai, bi, wi) +\
                    ' Aa %i Ba %i Wa %i Iteration %i.png' %(aa, ba, wa, i))
        
        
