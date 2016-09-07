# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:25:39 2016

@author: Julien
"""

from CellMatrix import Grid, max_wert
import os

def create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


def convert(matrix, zeilenlaenge, spaltenlaenge):
    """ int[][] -> (int r, int g, int b)[]
        Erstellt eine Tripelliste im rgb-Format aus einer 
        gegebenen Integermatrix anhand des Wertes"""
    temp = []
    for z in range(zeilenlaenge):
        for s in range(spaltenlaenge):
            temp.append(assign(matrix[z][s].wert))
    return temp
    
    
def convert2(matrix, zeilenlaenge, spaltenlaenge):
    """ int[][] -> (int r, int g, int b)[]
        Erstellt eine Tripelliste im rgb-Format aus einer 
        gegebenen Integermatrix anhand der Akivatoren"""
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