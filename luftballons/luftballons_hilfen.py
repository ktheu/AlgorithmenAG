# -*- coding: utf-8 -*-
import itertools


def eingabe(nr):
    '''
    nr: int, Nummer der Eingabedaten
    returns: tupel (lvm, ballons)
        lvm: Liste mit der Schalenbelegung
        ballons: Liste mit den Ballons, die nachgefüllt werden.
    '''
    #datapath = 'Bwinf/luftballons/myLoesung/'
    datapath = ''
    with open(datapath+'luftballons'+str(nr)+'.txt') as f:
       ballons = f.read().splitlines()
    ballons = [int(k) for k in ballons]
    return ballons

#ballons = eingabe(1)
#print(ballons)

def kombies():
    a = [1,2,5,2]
    for i in range(1,len(a)+1):
        for x in itertools.combinations(a,i):
            print(list(x))


kombies()


