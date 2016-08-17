# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:50:50 2016

@author: jettevonpostel
"""

class Grid:
    
    def __init__(self, zeilenlaenge, spaltenlaenge, radius):
        self.zeilenlaenge = zeilenlaenge
        self.spaltenlaenge = spaltenlaenge
        self.radius = radius
        self.grid = []     
        
        for s in range(spaltenlaenge):
                        
            spalte = []
            
            for z in range(zeilenlaenge):
                spalte.append(Zelle(self, z, s))
                
            self.grid.append(spalte)
            
    

            
                

#%%
        
class Zelle:
    
    def __init__(self, grid, zeile, spalte):
        self.grid = grid
        self.zeile = zeile
        self.spalte = spalte
        
    
    
    
    