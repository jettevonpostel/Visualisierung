# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 22:24:12 2016

@author: Julien
"""
from PIL import Image
import Image_Creation as ic

def adapting_path(path):
    temp = list(path)
    i = 0
    for b in temp:
        if b == '\\':
            temp[i] = '/'
        i += 1
    return ''.join(temp)
    

#bildpfad = raw_input("Pfad: ")
bildpfad = r'E:\Eigene Dateien\GitHub\Visualisierung\Python\Generierte Bilder\1920 x 1080 Modus 2 Chance 20 Ri 6 Ra 11'
bildpfad = adapting_path(bildpfad)

bilddatei = raw_input("Datei: ")

#aktiv_farbe = input("Farbe der Aktivatoren im Bild in der Form (r, g, b): ")
aktiv_farbe = (255, 255, 255)
#aktiv_neu = input("Ersetzende Farbe in der Form (r, g, b): ")
aktiv_neu = (202, 128, 1)

#inhib_farbe = input("Farbe der Inhibitoren im Bild in der Form (r, g, b): ")
inhib_farbe = (0, 0, 0)
#inhib_neu = input("Ersetzende Farbe in der Form (r, g, b): ")
inhib_neu = (255, 247, 0)
    
original = Image.open(bildpfad + '/' + bilddatei)
pix = original.load()



hoehe = original.size[1]
breite = original.size[0]

im = Image.new('RGB', original.size)

image_list = []

for h in range(hoehe):
    for b in range(breite):
        
        if pix[b, h] == aktiv_farbe:
            image_list.append(aktiv_neu)
            
        elif pix[b, h] == inhib_farbe:
            image_list.append(inhib_neu)
        
        else:
            image_list.append(pix[b, h])


ic.create_path(bildpfad + '/farb/')

im.putdata(image_list)
im.save(bildpfad + '/farb/' + bilddatei)

