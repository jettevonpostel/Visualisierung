# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:50:50 2016

@author: Jette von Postel & Julien Stengel
"""
# Alle Angaben im Grid werden in der Reihenfolge Zeile|Spalte durchgeführt

import random as rd
import math as m


max_wert = 10 # globale Angabe wie hoch der Betrag der Wert
              # einer Zelle maximal werden kann 

def randact(chance):
    """ void -> boolean
        randact steht für random Activator        
        gibt zufällig einen Boolschen Wert zurück, wobei die höhere 
        Wahrscheinlichkeit bei False liegt"""
    if rd.randint(1, chance) != 1:
        return False
    return True

#%%

class Grid:
    
    def __init__(self, zeilenlaenge, spaltenlaenge, chance):
        """ int zeilenlänge, int spaltenlänge, int chance
            Stellt die Grundstruktur zur Erzeugung der Patterns"""
        self.zeilenlaenge = zeilenlaenge
        self.spaltenlaenge = spaltenlaenge
        self.grid = []     # Zeile | Spalte
        
        for z in range(zeilenlaenge):
            zeile = []
            
            for s in range(spaltenlaenge):
                zeile.append(Zelle(self, z, s, rd.randint(-1, 1), \
                                   randact(chance)))
                
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
            
    def print_grid2(self):
        """ void -> void
            gibt den derzeitigen Stand der Dinge in der Konsole aus
            mit der Platzierung der Aktivatoren"""
        for z in range(self.zeilenlaenge):
            zeilenausgabe = ""
            for s in range(self.spaltenlaenge):
                zeilenausgabe = zeilenausgabe + "|%i %3i "\
                                %(self.grid[z][s].activator, \
                                  self.grid[z][s].wert)
            print(zeilenausgabe + "|")
            print "-" + (self.spaltenlaenge*7)*"-"
            
    
    def get_cell(self, zeile, spalte):
        """ int zeile, int spalte -> Zelle
            gibt Zelle an absoluter Position zurück"""
        return self.grid[zeile][spalte]        
            
    def scan(self, radius):
        """ int radius -> void
            lässt jede Zelle nach Aktivatoren/Inhibitoren in 
            ihrer Umgebung zählen"""
        for z in range(self.zeilenlaenge):
            for s in range(self.spaltenlaenge): 
                self.grid[z][s].zaehle(radius)
                
    def scan2(self, ri, ra):
        """ int ri, int ra -> void
            lässt jede Zelle nach Aktivatoren/Inhibitoren in 
            ihrer Umgebung zählen"""
        for z in range(self.zeilenlaenge):
            for s in range(self.spaltenlaenge): 
                self.grid[z][s].zaehle2(ri, ra)
                
    def write(self):
        """ void -> void
            Verändert alle Zellen basierend auf ihrem letzten Scan"""
        for z in range(self.zeilenlaenge):
            for s in range(self.spaltenlaenge): 
                self.grid[z][s].update()

    def write2(self):
        """ void -> void
            Verändert alle Zellen basierend auf ihrem letzten Scan"""
        for z in range(self.zeilenlaenge):
            for s in range(self.spaltenlaenge): 
                self.grid[z][s].update2()
            
       

#%%
        
class Zelle:
    
    def __init__(self, grid, zeile, spalte, wert, activator):
        """" Grid grid, int zeile, int spalte, int wert, bool activator
             Zelle wird zur Bevölkerung des Grids benutzt"""
        
        self.grid = grid
        self.zeile = zeile
        self.spalte = spalte
        self.counter = 0
        self.wert = wert
        self.activator = activator

 
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
                    
    def zaehle2(self, ri, ra):
        """ int ri, int ra -> void
            updated den derzeitigen Stand der umliegenden Aktivatoren 
            basierend auf der Interpretation von Young; Mit einem inneren 
            Radius für Aktivatoren und einem äußeren für Inhibitoren"""
        self.counter = 0
        for z in range((-1)*ra, ra+1):
            for s in range((-1)*ra, ra+1):
                
                if self.in_range(z,s) and m.sqrt(abs(z)**2 + abs(s)**2) <= ra:
                    temp = self.nachbar(z,s)
                    
                    #print "Betrachte: ", temp.zeile, temp.spalte, \
                    #      " Aktiv: ", temp.activator
                    
                    if temp.activator and m.sqrt(abs(z)**2 + abs(s)**2) > ri:
                        self.counter -=1
                        #print "-"
                        
                    elif temp.activator and m.sqrt(abs(z)**2 + abs(s)**2) <= ri:
                        self.counter +=1     
                        #print "+"
                    
                    
    def max_update(self):
        """ int radius -> void
            Updated den Wert abhängig vom derzeitigen Counter und maximalen
            Aktivatorwert"""
        if self.counter < 0:
            self.wert = self.counter % (max_wert*(-1))
        else:
            self.wert = self.counter % max_wert
            
    def update(self):
        """ void -> void
            Updated den Wert abhängig vom derzeitigen Counter"""
        self.wert = self.counter
            
    def update2(self):
        """ void -> void
            Updated den Wert abhängig vom derzeitigen Counter"""
        if self.counter != 0:
            self.wert = self.counter
            
            if self.wert > 0:
                self.activator = True
            elif self.wert < 0:
                self.activator = False
    
    
    
#%% 
    
if __name__ == "__main__":
    """Autmomatisierter Aufruf der Klassen. Vergleiche mit Java 'main'"""
    g = Grid(7,10)
    g.print_grid2()
    print("\n")
   
    for i in range(20):
        g.scan2(2, 3)
        #g.parallel_scan()
        
        g.write2()
        #g.parallel_write()        
        
        g.print_grid2()
        print("\n")
