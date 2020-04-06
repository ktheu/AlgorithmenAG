# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 12:49:57 2017

@author: khthe_000
"""
def ersteEins(tab,zeile):
    '''
    tab: eine matrix mit n Zeilen und m Spalten 
    zeile: 0 <= zeile < n
    returns: den spaltenindex, in der in Zeile zeile zum erstenmal
    eine 1 vorkommt. -1 falls in der Zeile keine 1 vorkommt.
    
    '''
 
    for k in range(len(tab[0])):
        if tab[zeile][k] == 1:
            return k
    return -1

def showMatrix(tab):
    rows = len(tab)
    cols = len(tab[0])
    print("{:1}  ".format(" "),end = '')
 
    for j in range(cols):
        print("{:3}".format(j),end = '')
    print()
    print("-"*cols*4)
    for i in range(rows):
        print("{:1} :".format(i),end = '')
        for j in range(cols):
            print("{:3}".format(tab[i][j]),end = '')
        print()
    
    

def makeSum(a,summe):
    '''
    a: Liste mit positiven ganzen Zahlen
    summe: eine positive ganze Zal
    returns: tupel (True, Liste mit Indizes der Werte, die summe ergeben)
                   (False, leere Liste), wenn summe nicht zusammengesetzt werden kann.
    '''
    n = len(a)
    tab = [[0]*n for i in range(summe+1)] # für jede Zahl <= summe eine Zeile
    
    tab[a[0]][0]= 1   # mit dem Index 0 lässt sich nur zu a[0] aufsummieren
    
    # tab[s][i] == 1:  wenn sich die Summe s mit den Indizes 0..i erreichen lässt
    
    for i in range(1,n):
        zahl = a[i]  
    
        tab[zahl][i]= 1
        for j in range(summe+1):
            if tab[j][i-1] == 1 and j+zahl <= summe:
                tab[j+zahl][i] = 1
                tab[j][i] = 1
    
    result = []
    
    showMatrix(tab)

    noch = summe
    for i in range(n):
         k = ersteEins(tab,noch)
         result.append(k)
         noch -= a[k]

         if noch == 0:
             return True,result

         if noch < 0: 
             return False,noch
    return False,noch

    
            
 
a = [1,3,4,6]   
makeSum(a,9)

