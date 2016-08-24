# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 07:42:46 2016

@author: Julien
"""

# zum Einlesen der Dateien
# noch im Aufbau derzeit ist die Datei nur zur Erinnerung

from PIL import Image
from CellMatrix import Grid
import Image_Creation as ic
import os


#bilddatei = "1920 x 1080 Modus 3 Chance 15 Ai 8 Bi 4 Aa 8 Ba 14 Iteration 19.png"
#aktiv_farbe = (255, 255, 255)
#
#
#original = Image.open(bilddatei)
#pix = original.load()
#
#hoehe = original.size[1]
#breite = original.size[0]
#
#im= Image.new('RGB', original.size)
#
#g = Grid(hoehe, breite, 1)
#
#for z in range(hoehe):
#    for s in range(breite):
#        if pix[s, z] == aktiv_farbe:
#            g.get_cell(z, s).activator = True
#        else: 
#            g.get_cell(z, s).activator = False
#            
#im.putdata(ic.convert2(g.grid, hoehe, breite))


print("Rendermodus 1 = Neues Bild erstellen")
print("Rendermodus 2 = Bild laden und weiter rendern")

rendermodus = input("Rendermodus: ")

if rendermodus == 1:
    breite = input("Breite: ") # wie breit ist das Bild? (in Pixel)
    hoehe = input("Höhe: ")    # wie hoch ist das Bild? (in Pixel)
    chance = input("Chance: ") # wie Hoch ist die Chance, dass eine Zelle ein
                               # Aktivator ist? (also: 1/chance)
    g = Grid(hoehe, breite, chance)
    im= Image.new('RGB', (breite, hoehe))


if rendermodus == 2:
    
    bilddatei = raw_input("Datei: ")
    aktiv_farbe = input("Farbe der Aktivatoren im Bild in der Form (r, g, b): ")
    voriteration = input("Wie viele Iterationen wurden bereits durchgeführt?: ")
    chance = input("Welche Chance bestand beim ersten generieren?: ")
        
    original = Image.open(bilddatei)
    pix = original.load()
    
    hoehe = original.size[1]
    breite = original.size[0]
    
    im= Image.new('RGB', original.size)
    
    g = Grid(hoehe, breite, 1)
    
    for z in range(hoehe):
        for s in range(breite):
            if pix[s, z] == aktiv_farbe:
                g.get_cell(z, s).activator = True
            else: 
                g.get_cell(z, s).activator = False
                



path = os.path.dirname(__file__) + "/Generierte Bilder/"

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

if rendermodus == 1:
    iterationen = input("Anzahl Iterationen: ") + 1
    voriteration = 1
    # Wie häufig wird der Algorithmus angewandt?
    
if rendermodus == 2:
    iterationen = input("Anzahl Iterationen: ") + voriteration +1
    

#%%

if modus == "1":
    
    path = path + '%i x %i Modus %s Radius %i/' \
           %(breite, hoehe, modus, radius)
           
    ic.create_path(path)
    
    if rendermodus == 1:
        im.putdata(ic.convert(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Radius %i Startbild.png' \
                %(breite, hoehe, modus, radius))        
    
    for i in range(voriteration, iterationen):
        g.scan(radius)
        g.write()        
        
        im.putdata(ic.convert(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Iteration %i.png' \
                %(breite, hoehe, modus, i))
                
#%%
                

elif modus == "2":
    
    path = path + '%i x %i Modus %s Chance %i Ri %i Ra %i/' \
            %(breite, hoehe, modus, chance, innenradius, aussenradius)
            
    ic.create_path(path)

    if rendermodus == 1:
        im.putdata(ic.convert2(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Chance %i Ri %i Ra %i Startbild.png' \
                %(breite, hoehe, modus, chance, innenradius, aussenradius))         
    
    for i in range(voriteration, iterationen):
        g.scan2(innenradius, aussenradius)
        g.write2()        
        
        im.putdata(ic.convert2(g.grid, hoehe, breite))
        im.save(path + \
                '%i x %i Modus %s Chance %i Ri %i Ra %i Iteration %i.png' \
                %(breite, hoehe, modus, chance, innenradius, \
                  aussenradius, i)) 
                
#%%
                
elif modus == "3":
    
    path = path + '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i/' \
            %(breite, hoehe, modus, chance, ai, bi, aa, ba)
            
    ic.create_path(path)
    
    if rendermodus == 1:
        im.putdata(ic.convert2(g.grid, hoehe, breite))
        folder = ''
        im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i ' \
                %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                'Startbild.png')         
    
    for i in range(voriteration, iterationen):
        g.scan3(ai, bi, aa, ba)
        g.write2()        
        
        im.putdata(ic.convert2(g.grid, hoehe, breite))
        im.save(path + \
                '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i' \
                %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                ' Iteration %i.png' %i)
                
#%%
                
elif modus == "4":
    
    path = path + '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i/' \
            %(breite, hoehe, modus, chance, ai, bi, aa, ba)
            
    ic.create_path(path)
    
    if rendermodus == 1:
        im.putdata(ic.convert2(g.grid, hoehe, breite))
        folder = ''
        im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i ' \
                %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                'Startbild.png')         
    
    for i in range(voriteration, iterationen):
        g.scan4(ai, bi, aa, ba)
        g.write2()        
        
        im.putdata(ic.convert2(g.grid, hoehe, breite))
        im.save(path + \
                '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i' \
                %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                ' Iteration %i.png' %i)

#%%         
    
elif modus == "a1":
    
    path = path + '%i x %i Modus %s Chance %i Ai %i Bi %i Wi %i' \
            %(breite, hoehe, modus, chance, ai, bi, wi) +\
            'Aa %i Ba %i Wa %i/' %(aa, ba, wa)
            
    ic.create_path(path)
    
    if rendermodus == 1:
        im.putdata(ic.convert2(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Wi %i' \
                %(breite, hoehe, modus, chance, ai, bi, wi) +\
                'Aa %i Ba %i Wa %i Startbild.png' %(aa, ba, wa))
    
    for i in range(voriteration, iterationen):
        g.scan_async1(ai, bi, wi, aa, ba, wa)
        g.write2()        
        
        im.putdata(ic.convert2(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Wi %i' \
                %(breite, hoehe, modus, chance, ai, bi, wi) +\
                ' Aa %i Ba %i Wa %i Iteration %i.png' %(aa, ba, wa, i))


#%%                  
                
elif modus == "a2":
    
    path = path + '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i ' \
            %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
            'Ausrichtung %i/' %ausrichtung
            
    ic.create_path(path)
    
    if rendermodus == 1:
        im.putdata(ic.convert2(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i ' \
                %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                'Ausrichtung %i Startbild.png' %ausrichtung)         
    
    for i in range(voriteration, iterationen):
        g._async2(ai, bi, aa, ba, ausrichtung)
        g.write2()        
        
        im.putdata(ic.convert2(g.grid, hoehe, breite))
        im.save(path + \
                '%i x %i Modus %s Chance %i Ai %i Bi %i Aa %i Ba %i' \
                %(breite, hoehe, modus, chance, ai, bi, aa, ba) +\
                ' Ausrichtung %i Iteration %i.png' %(ausrichtung, i))
  

              
#%%         
    
elif modus == "a3":
    
    path = path + '%i x %i Modus %s Chance %i Ai %i Bi %i Wi %i' \
            %(breite, hoehe, modus, chance, ai, bi, wi) +\
            'Aa %i Ba %i Wa %i/' %(aa, ba, wa)
            
    ic.create_path(path)
    
    if rendermodus == 1:
        im.putdata(ic.convert2(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Wi %i' \
                %(breite, hoehe, modus, chance, ai, bi, wi) +\
                'Aa %i Ba %i Wa %i Startbild.png' %(aa, ba, wa))
    
    for i in range(voriteration, iterationen):
        g._async3(ai, bi, wi, aa, ba, wa)
        g.write2()        
        
        im.putdata(ic.convert2(g.grid, hoehe, breite))
        im.save(path + '%i x %i Modus %s Chance %i Ai %i Bi %i Wi %i' \
                %(breite, hoehe, modus, chance, ai, bi, wi) +\
                ' Aa %i Ba %i Wa %i Iteration %i.png' %(aa, ba, wa, i))
    
    