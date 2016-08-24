# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:50:50 2016

@author: Jette von Postel & Julien Stengel
"""
# Alle Angaben im Grid werden in der Reihenfolge Zeile|Spalte durchgeführt

#%%
#===========================Imports und Generelles=============================
#
#%%

import random as rd
import numpy as np


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
    
def runde(x):
    """float x -> int x
       rundet die Kommazahle auf die betraglich weitest außen
       liegende Stelle vom Ursprung aus gesehen"""
    return int(round(x))

#    if x == 0:
#        return 0
#    if x%1 == 0:
#        return int(x)
#    elif x > 0:
#        return int(round(x+0.5))
#    elif x < 0:
#        return int(round(x-0.5))


#%%
#=============================neue Klasse======================================
#
#%%

class Grid:
    
    def __init__(self, zeilenlaenge, spaltenlaenge, chance):
        """ int zeilenlänge, int spaltenlänge, int chance
            Stellt die Grundstruktur zur Erzeugung der Patterns"""
        self.zeilenlaenge = zeilenlaenge
        self.spaltenlaenge = spaltenlaenge
        self.grid = np.ndarray((zeilenlaenge, spaltenlaenge), \
                                dtype = np.object)
        
        for z in range(zeilenlaenge):
            for s in range(spaltenlaenge):
                self.grid[z][s] = Zelle(self, z, s, rd.randint(-1, 1), \
                                        randact(chance))
                
    
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
                
    def scan3(self, ai, bi, aa, ba):
        """ int ai, int bi, int aa, int ba -> void
            lässt jede Zelle nach Aktivatoren/Inhibitoren in 
            ihrer Umgebung zählen
            Zu beachten: ai <= aa & bi <= ba """
        for z in range(self.zeilenlaenge):
            for s in range(self.spaltenlaenge): 
                self.grid[z][s].zaehle3(ai, bi, aa, ba)
                
    def scan4(self, ai, bi, aa, ba):
        """ int ai, int bi, int aa, int ba -> void
            lässt jede Zelle nach Aktivatoren/Inhibitoren in 
            ihrer Umgebung zählen
            Zu beachten: ai <= aa & bi <= ba """
        for z in range(self.zeilenlaenge):
            for s in range(self.spaltenlaenge): 
                self.grid[z][s].zaehle4(ai, bi, aa, ba)
                
    def scan_async1(self, ai, bi, wi, aa, ba, wa):
        """ int ai, int bi, int wi, int aa, int ba, int wa -> void
            lässt jede Zelle nach Aktivatoren/Inhibitoren in 
            ihrer Umgebung zählen
            Zu beachten: ai <= aa & bi <= ba """
        for z in range(self.zeilenlaenge):
            for s in range(self.spaltenlaenge): 
                self.grid[z][s].zaehle_async1(ai, bi, wi, aa, ba, wa)                
                
    def scan_async2(self, ai, bi, aa, ba, ausrichtung):
        """ int ai, int bi, int aa, int ba, int ausrichtung -> void
            lässt jede Zelle nach Aktivatoren/Inhibitoren in 
            ihrer Umgebung zählen
            
            Zu beachten: ai <= aa & bi <= ba 

            Wahl der Ausrichtung: 1 => Hälfte zeigt nach oben        
                                  2 => Hälfte zeigt nach rechts
                                  3 => Hälfte zeigt nach unten
                                  4 => Hälfte zeigt nach links"""

        for z in range(self.zeilenlaenge):
            for s in range(self.spaltenlaenge): 
                self.grid[z][s].zaehle_async2(ai, bi, aa, ba, ausrichtung)
                
                
    def scan_async3(self, ai, bi, wi, aa, ba, wa):
        """ int ai, int bi, int wi, int aa, int ba, int wa -> void
            lässt jede Zelle nach Aktivatoren/Inhibitoren in 
            ihrer Umgebung zählen
            Zu beachten: ai <= aa & bi <= ba """
        for z in range(self.zeilenlaenge):
            for s in range(self.spaltenlaenge): 
                self.grid[z][s].zaehle_async3(ai, bi, wi, aa, ba, wa)
                
                
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
#=============================neue Klasse======================================
#
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

#%%
    
    def zaehle(self, radius):
        """ int radius -> void
            updated den derzeitigen Stand der umliegenden Aktivatoren
            in einem gegebenen Radius"""
        
        self.counter = 0
        r = radius
        for z in range(-r, r+1):
            for s in range(-r, r+1):            
                
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
            basierend auf der Interpretation von Young; mit einem inneren 
            Radius für Aktivatoren und einem äußeren für Inhibitoren"""
        self.counter = 0
        for z in range(-ra, ra+1):
            for s in range(-ra, ra+1):
                
                if self.in_range(z,s) and (z**2 + s**2 <= ra**2):
                    temp = self.nachbar(z,s)
                    
                    #print "Betrachte: ", temp.zeile, temp.spalte, \
                    #      " Aktiv: ", temp.activator
                    
                    if temp.activator and (z**2 + s**2 > ri**2):
                        self.counter -=1
                        #print "-"
                    elif temp.activator and (z**2 + s**2 <= ri**2):
                        self.counter +=1     
                        #print "+"
                        
                        
    def zaehle3(self, ai, bi, aa, ba):
        """ int ai, int bi, int aa, int ba -> void
        
            Zu beachten: ai <= aa & bi <= ba 
            Wobei ein "echt weniger" bevorzugt ist, weil das Bild sonst einfach 
            einfarbig wird
            
            updated den derzeitigen Stand der umliegenden Aktivatoren 
            basierend auf der Interpretation von Young; bei der eine Ellipse
            der Berechnung zu Grunde liegt. 
            
            ai und bi sind die Hauptachsen der inneren Ellipse und aa und ba 
            sind die Hauptachsen der äußeren Ellipse
            ai und aa liegen dabei auf der Horizontalen und bi und ba auf der
            Vertikalen.
            Berechnungen gehen von der Formel (x/a)²+(y/b)²=1 aus."""
            
        self.counter = 0
        for y in range(-ba, ba+1):        # y ist hierbei die Zeile
            for x in range(-aa, aa+1):    # x ist hierbei die Spalte
            
                if self.in_range(y,x) and ((x/aa)**2 + (y/ba)**2 <= 1):
                    temp = self.nachbar(y,x)
                    
                    inside = ((x/ai)**2 + (y/bi)**2 <= 1) # true wenn sich
                    # (x|y) innerhalb der Innenllipse befindet
                    
                    if temp.activator and not inside:
                        self.counter -=1
                        
                    elif temp.activator and inside:
                        self.counter +=1
                        
                        
    def zaehle4(self, ai, bi, aa, ba):
        """ int ai, int bi, int wi, int aa, int ba, int wa -> void"""
        self.counter = 0
        for z in range(-ba, ba+1):
            for s in range(-aa, aa+1):
            
                if self.in_range(z,s):
                    temp = self.nachbar(z,s)
                    
                    inside = (z <= bi) and (s <= ai) # true wenn sich
                    # z und s innerhalb des Innenrechtecks befinden
                    
                    if temp.activator and not inside:
                        self.counter -=1
                        
                    elif temp.activator and inside:
                        self.counter +=1
  
#%%                      
                        
    def zaehle_async1(self, ai, bi, wi, aa, ba, wa):
        """ int ai, int bi, int wi, int aa, int ba, int wa -> void

            wi und wa sind die Größen der Winkel, um den die jeweilige 
            Ellipse gegen den Uhrzeigersinn rotiert wurde. wa und wi sind im
            Gradmaß anzugeben
            
            Zu beachten: ai <= aa & bi <= ba"""        
        
        self.counter = 0
        
        alpha = np.radians(wa) # Winkel der Rotation rad
        cosalpha = np.cos(alpha)
        sinalpha = np.sin(alpha)
        
        beta = np.radians(wi)
        cosbeta = np.cos(beta)
        sinbeta = np.sin(beta)
        
        for y in range(-ba, ba+1):            
            for x in range(-aa, aa+1):
                
                if y <= bi and x <= ai:
                    xd = x*cosbeta - y*sinbeta
                    yd = x*sinbeta + y*cosbeta
                    
                    xr = runde(xd)                    
                    yr = runde(yd)
                    
                    if self.in_range(yr, xr):
                        if self.nachbar(yr, xr).activator:
                            self.counter += 1
                            
                else:
                    xd = x*cosalpha - y*sinalpha
                    yd = x*sinalpha + y*cosalpha                        

                    xr = runde(xd)                    
                    yr = runde(yd)
                    
                    if self.in_range(yr, xr):
                        if self.nachbar(yr, xr).activator:
                            self.counter -= 1
                
        
#%%
                        
    def zaehle_async2(self, ai, bi, aa, ba, ausrichtung):
        """ int ai, int bi, int aa, int ba, int ausrichtung -> void

            Wahl der Ausrichtung: 1 => Hälfte zeigt nach oben        
                                  2 => Hälfte zeigt nach rechts
                                  3 => Hälfte zeigt nach unten
                                  4 => Hälfte zeigt nach links
            
            Zu beachten: ai <= aa & bi <= ba 
            Wobei ein "echt weniger" bevorzugt ist, weil das Bild sonst einfach 
            einfarbig wird
            
            updated den derzeitigen Stand der umliegenden Aktivatoren 
            basierend auf der Interpretation von Young; bei der eine halbe
            Ellipse der Berechnung zu Grunde liegt. 
            
            ai und bi sind die Hauptachsen der inneren Ellipse und aa und ba 
            sind die Hauptachsen der äußeren Ellipse
            ai und aa liegen dabei auf der Horizontalen und bi und ba auf der
            Vertikalen.
            Berechnungen gehen von der Formel (x/a)²+(y/b)²=1 aus.
            """
        if ausrichtung == 1:
            b1 = (-1)*aa
            b2 = aa+1
            h1 = (-1)*ba
            h2 = 1
            
        if ausrichtung == 2:
            b1 = 0
            b2 = aa+1
            h1 = (-1)*ba
            h2 = ba+1
    
        if ausrichtung == 3:
            b1 = (-1)*aa
            b2 = aa+1
            h1 = 0
            h2 = ba+1        
        
        if ausrichtung == 4:
            b1 = (-1)*aa
            b2 = 1
            h1 = (-1)*ba
            h2 = ba+1
            
        self.counter = 0
        for y in range(h1, h2):        # y ist hierbei die Zeile
            for x in range(b1, b2):    # x ist hierbei die Spalte
            
                if self.in_range(y,x) and ((x/aa)**2 + (y/ba)**2 <= 1):
                    temp = self.nachbar(y,x)
                    
                    inside = ((x/ai)**2 + (y/bi)**2 <= 1) # true wenn sich
                    # (x|y) innerhalb der Innenllipse befindet
                    
                    if temp.activator and not inside:
                        self.counter -=1
                        
                    elif temp.activator and inside:
                        self.counter +=1
        
#%%          

    def zaehle_async3(self, ai, bi, wi, aa, ba, wa):
        """ int ai, int bi, int wi, int aa, int ba, int wa -> void

            wi und wa sind die Größen der Winkel, um den die jeweilige 
            Ellipse gegen den Uhrzeigersinn rotiert wurde. wa und wi sind im
            Gradmaß anzugeben
            
            Zu beachten: ai <= aa & bi <= ba
            
            updated den derzeitigen Stand der umliegenden Aktivatoren 
            basierend auf der Interpretation von Young; bei der eine halbe
            Ellipse der Berechnung zu Grunde liegt. 
            
            ai und bi sind die Hauptachsen der inneren Ellipse und aa und ba 
            sind die Hauptachsen der äußeren Ellipse
            ai und aa liegen dabei auf der Horizontalen und bi und ba auf der
            Vertikalen.
            Berechnungen gehen von der Formel (x/a)²+(y/b)²=1 aus.
            """
        
        # Zunächst muss eine Box um die Ellipse zum Iterieren gefunden werden
        
        self.counter = 0
        
        alpha = np.radians(wa) # Winkel der Rotation rad
        cosalpha = np.cos(alpha)
        sinalpha = np.sin(alpha)
        
        beta = np.radians(wi)
        cosbeta = np.cos(beta)
        sinbeta = np.sin(beta)
        
        for y in range(-ba, ba+1):            
            for x in range(-aa, aa+1):
                
                if ((x/ai)**2 + (y/bi)**2 <= 1):
                    xd = x*cosbeta - y*sinbeta
                    yd = x*sinbeta + y*cosbeta
                    
                    xr = runde(xd)                    
                    yr = runde(yd)
                    
                    if self.in_range(yr, xr):
                        if self.nachbar(yr, xr).activator:
                            self.counter += 1
                            
                elif ((x/aa)**2 + (y/ba)**2 <= 1):
                    xd = x*cosalpha - y*sinalpha
                    yd = x*sinalpha + y*cosalpha                        

                    xr = runde(xd)                    
                    yr = runde(yd)
                    
                    if self.in_range(yr, xr):
                        if self.nachbar(yr, xr).activator:
                            self.counter -= 1
        
#%%  
        
#    def zaehle_async_opp(self, ar, br, al, bl):

#%%        
                
                    
    def max_update(self): #derzeit nicht benutzt
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
#=============================Main (Test)======================================
#
#%%
    
if __name__ == "__main__":
    """Autmomatisierter Aufruf der Klassen. Vergleiche mit Java 'main'"""
    g = Grid(7, 10, 12)
    g.print_grid2()
    print("\n")
   
#    for i in range(20):
#        g.scan4(2, 1, 5, 3, 1)
#        #g.parallel_scan()
#        
#        g.write2()
#        #g.parallel_write()        
#        
#        g.print_grid2()
#        print("\n")
