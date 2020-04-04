tn = [7,10,14,16,18,19,20,24,26,29,30,32]
m = 5
# tn = [7,10,14,16,18,19]
# m = 3

# f = open('./beispieldaten/beispiel2.txt')
# anz = len(f.readlines())
# f.close()
# f = open('./beispieldaten/beispiel2.txt')
# tn = [int(f.readline()) for i in range(anz)]
# m = 10

def minAbstand(x,a):
    '''returns minimaler Abstand von x zu einer Zahl in al'''
    minabs = abs(x-a[0])
    for y in a:
        if abs(x-y) < minabs:
            minabs = abs(x-y)
    return minabs

def sumKosten(tn,a):
    '''summe der Kosten wenn al die gewählten Zahlen sind'''
    summe = 0
    for x in tn:
        summe+=minAbstand(x,a)
    return summe
 
from itertools import *
inf = float('inf')

minKost = inf
minA    = None
for a in combinations(tn,m):
    if  sumKosten(tn,a) < minKost:
        minKost = sumKosten(tn,a)
        minA = a

print(minKost, minA)