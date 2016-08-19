# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 12:52:13 2016

@author: Julien
"""

#    def parallel_scan(self):
#        """ void -> void
#            lässt jede Zelle nach Aktivatoren/Inhibitoren in 
#            ihrer Umgebung zählen"""
#        threads = []
#        for z in range(self.zeilenlaenge):
#            for s in range(self.spaltenlaenge): 
#                
#                t = threading.Thread(target = self.grid[z][s].zaehle, \
#                                     args = (self.radius, ))
#                threads.append(t)
#                t.start()
#                
#        for thread in threads:
#                thread.join()
#
#        
#    def parallel_write(self):
#        """ void -> void
#            Verändert alle Zellen basierend auf ihrem letzten Scan"""
#        threads = []
#        for z in range(self.zeilenlaenge):
#            for s in range(self.spaltenlaenge): 
#                
#                t = threading.Thread(target = self.grid[z][s].update)
#                threads.append(t)
#                t.start()
#                
#        for thread in threads:
#                thread.join()