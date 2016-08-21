# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 20:34:11 2016

@author: Julien
"""



import os
path = os.path.dirname(__file__) + "/Bilder/"# relative directory path

if not os.path.exists(path):
    os.makedirs(path)