# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:50:50 2016

@author: jettevonpostel
"""

import random as rd

class Grid:
    
    def __init__(self, zeilenlaenge, spaltenlaenge, radius):
        self.zeilenlaenge = zeilenlaenge
        self.spaltenlaenge = spaltenlaenge
        self.radius = radius
        self.grid = []     
        
        for s in range(spaltenlaenge):
                        
            spalte = []
            
            for z in range(zeilenlaenge):
                spalte.append(Zelle(self, z, s, rd.randint(-1, 1)))
                
            self.grid.append(spalte)
            
    def print_grid(self):
        for s in range(self.spaltenlaenge):
            zeilenausgabe = ""
            for z in range(self.zeilenlaenge):
                zeilenausgabe = zeilenausgabe + '| ' + str(self.grid[s][z].wert) + " "
            print(zeilenausgabe + "|")
    
    def give_cell(self, zeile, spalte):
        return self.grid[spalte][zeile]        
            
    def scan(self):
        for s in range(self.spaltenlaenge):            
            for z in range(self.zeilenlaenge):
                self.grid[s][z].zaehle(self.radius)
        
    def write(self):
        for s in range(self.spaltenlaenge):            
            for z in range(self.zeilenlaenge):
                self.grid[s][z].update()

            
                

#%%
        
class Zelle:
    
    def __init__(self, grid, zeile, spalte, wert):
        self.grid = grid
        self.zeile = zeile
        self.spalte = spalte
        self.counter = 0
        self.wert = wert
        
    def nachbar(self, zeile, spalte):
        return self.grid.give_cell(self.zeile + zeile, self.spalte + spalte)
        
    def in_range(self, spalte, zeile):
        if self.spalte + spalte > self.grid.spaltenlaenge -1 or \
        self.spalte + spalte < 0 or \
        self.zeile + zeile > self.grid.zeilenlaenge -1 or \
        self.zeile + zeile < 0:
            return False
        return True
        
    
    def zaehle(self, radius):
        self.counter = 0
        r = radius
        for s in range((-1)*r, r+1):
            for z in range((-1)*r, r+1):
                if not(self.in_range(s,z)):
                    break
                temp = self.nachbar(z,s)
                if temp.wert > 0:
                    self.counter +=1
                elif temp.wert < 0:
                    self.counter -=1
                    
    def update(self):
        self.wert = self.counter%6
    
#%%    
if __name__ == "__main__":
    g = Grid(5,5,1)
    g.print_grid()
    print("\n")
#==============================================================================
#     
#     for i in range(10):
#         g.scan()
#         g.write()
#         g.print_grid()
#         print("\n")
#==============================================================================
