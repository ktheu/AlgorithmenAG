# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 18:54:10 2017

@author: khthe_000
"""

def showMatrix(tab):
    rows = len(tab)
    cols = len(tab[0])
    for i in range(rows):
        for j in range(cols):
            a = tab[i][j]
            print("{:4}".format(tab[i][j]),end = '')
        print()
        
tab = [[1,2],[3,4]]
showMatrix(tab)
