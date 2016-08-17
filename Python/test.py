# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:08:30 2016

@author: jettevonpostel
"""

def test():
    a = []
    for j in range(4):
        b = []
        for i in range(4):
            b.append(i)
        a.append(b)
        
    print(a)