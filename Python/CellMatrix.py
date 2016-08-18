# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:50:50 2016

@author: Jette von Postel & Julien Stengel
"""
# Alle Angaben im Grid werden in der Reihenfolge Zeile|Spalte durchgeführt

import random as rd


max_wert = 10 # globale Angabe wie hoch der Betrag der Wert einer Zelle maximal
             # werden kann 


#%%

class Grid:
    
    def __init__(self, zeilenlaenge, spaltenlaenge, radius):
        """ int zeilenlänge, int spaltenlänge, int radius
            Stellt die Grundstruktur zur Erzeugung der Patterns"""
        self.zeilenlaenge = zeilenlaenge
        self.spaltenlaenge = spaltenlaenge
        self.radius = radius
        self.grid = []     # Zeile | Spalte
        
        for z in range(zeilenlaenge):
            zeile = []
            
            for s in range(spaltenlaenge):
                zeile.append(Zelle(self, z, s, rd.randint(-1, 1)))
                
            self.grid.append(zeile)
            
    
    def print_grid(self):
        """ void -> void
            gibt den derzeitigen Stand der Dinge in der Konsole aus"""
        for z in range(self.zeilenlaenge):
            zeilenausgabe = ""
            for s in range(self.spaltenlaenge):
                zeilenausgabe = zeilenausgabe + "| %3i "\
                                %self.grid[z][s].wert
            print(zeilenausgabe + "|")
            print "-" + (self.spaltenlaenge*6)*"-"
    
    def get_cell(self, zeile, spalte):
        """ int zeile, int spalte -> Zelle
            gibt Zelle an absoluter Position zurück"""
        return self.grid[zeile][spalte]        
            
    def scan(self):
        """ void -> void
            lässt jede Zelle nach Aktivatoren/Inhibitoren in 
            ihrer Umgebung zählen"""
        for z in range(self.zeilenlaenge):
            for s in range(self.spaltenlaenge): 
                self.grid[z][s].zaehle(self.radius)
        
    def write(self):
        """ void -> void
            Verändert alle Zellen basierend auf ihrem letzten Scan"""
        for z in range(self.zeilenlaenge):
            for s in range(self.spaltenlaenge): 
                self.grid[z][s].update()

            
                

#%%
        
class Zelle:
    
    def __init__(self, grid, zeile, spalte, wert):
        """"Zelle wird zur Bevölkerung des Grids benutzt"""
        
        self.grid = grid
        self.zeile = zeile
        self.spalte = spalte
        self.counter = 0
        self.wert = wert

 
    def nachbar(self, zeile, spalte):
        """ int zeile, int spalte -> Zelle
            Findet den Nachbar relativ zum eigenen Index und gibt dessen 
            Refferenz.
            Z.B. gibt (-1, 2) die zelle ein weiter oben 
            und zwei weiter rechts"""
        
        return self.grid.get_cell(self.zeile + zeile, self.spalte + spalte)
        
        
    def in_range(self, zeile, spalte):
        """ int zeile, int spalte -> Boolean 
            Gibt an, ob es eine Zelle relativ zu dieser gibt"""
        
        if self.spalte + spalte > self.grid.spaltenlaenge -1 or \
        self.spalte + spalte < 0 or \
        self.zeile + zeile > self.grid.zeilenlaenge -1 or \
        self.zeile + zeile < 0:
            return False
        return True
        
    
    def zaehle(self, radius):
        """ int radius -> void
            updated den derzeitigen Stand der umliegenden Aktivatoren
            in einem gegebenen Radius"""
        
        self.counter = 0
        r = radius
        for z in range((-1)*r, r+1):
            for s in range((-1)*r, r+1):            
                
                if not(self.in_range(z,s)):                    
                    pass
                
                else:
                    temp = self.nachbar(z,s)
    
                    if temp.wert > 0:
                        self.counter +=1
                    elif temp.wert < 0:
                        self.counter -=1
                    
                    
    def max_update(self):
        """ int radius -> void
            Updated den Wert abhängig vom derzeitigen Counter und maximalen
            Aktivatorwert"""
        if self.counter < 0:
            self.wert = self.counter % (max_wert*(-1))
        else:
            self.wert = self.counter % max_wert
            
    def update(self):
        """ int radius -> void
            Updated den Wert abhängig vom derzeitigen Counter"""
        self.wert = self.counter
    
    
    
#%% 
    
if __name__ == "__main__":
    """Autmomatisierter Aufruf der Klassen. Vergleiche mit Java 'main'"""
    g = Grid(7,10,1)
    g.print_grid()
    print("\n")
   
    for i in range(20):
        g.scan()
        g.write()
        g.print_grid()
        print("\n")
