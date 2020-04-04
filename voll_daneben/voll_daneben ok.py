# tn = [7,10,14,16,18,19,20,24,26,29,30,32]
# M = 5

# tn = [7,10,14,16,18,19]
# M = 3

f = open('./beispieldaten/beispiel1.txt')
anz = len(f.readlines())
f.close()
f = open('./beispieldaten/beispiel1.txt')
tn = [int(f.readline()) for i in range(anz)]
M = 10


tn = [-10000000] + tn  
tn.sort()
N = len(tn)

def minAbstand(x,al):
    '''returns minimaler Abstand von x zu einer Zahl in al'''
    minabs = abs(x-al[0])
    for y in al:
        if abs(x-y) < minabs:
            minabs = abs(x-y)
    return minabs

def sumKosten(tn,al):
    '''summe der Kosten wenn al die gewählten Zahlen sind'''
    summe = 0
    for x in tn:
        summe+=minAbstand(x,al)
    return summe

def abschnitt(i,k):
    ''' kosten des abschnitts bis k, wenn nur der anfang und k gewählt wurden. '''
    tmp = tn[i:k+1]
    return sumKosten(tmp,[tmp[0],tmp[-1]])


def kosten0(k):
    ''' kosten von k bis zum Ende, wenn außer k keine weitere Zahl gewählt wurde '''
    tmp = tn[k:]
    return sumKosten(tmp,[tmp[0]])

import numpy as np
inf = 10000000
a = np.zeros((N,M+1),dtype=int) 
for i in range(N):
    a[i,0] = kosten0(i)

for m in range(1,M+1):
    for i in range(N):
        minKost = inf
        for k in range(i+1,N):
            if abschnitt(i,k) + a[k,m-1] < minKost:
                minKost = abschnitt(i,k) + a[k,m-1]
        a[i,m] = minKost

print(a)




 

