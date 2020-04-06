# -*- coding: utf-8 -*-
import itertools


def init_data(nr):
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
    lvm = ballons[:10]
    ballons = ballons[10:]
    return lvm,ballons

def nextfach(target,lvm,ballons):
    '''
    ermittelt das nächste fach der lvm, das ausgeleert wird, um target zu erreichen. 
    Wenn target mit den Inhalten nicht genau erreicht werden kann, wird
    ein target genommen, dass nur minimal größer ist.
    Wenn das target überhaupt nicht erreicht werden kann und es noch
    ballons zum nachfüllen gibt, wird der Index der lvm mit den wenigsten
    Ballons zurückgegeben.
    Wenn es keine Nachfüllballons mehr gibt und in der lvm das target
    nicht erreicht werden kann, wird -1 zurückgegeben.
    '''
    n = len(lvm)
    bestsumme = sum(lvm)
    bestcombi = lvm
    for i in range(1,n+1):
        for x in itertools.combinations(lvm,i):
            summe = sum(x)
            if summe == target:
                mini = max(x)
                return lvm.index(mini)
            elif target < summe < bestsumme:
                bestsumme = summe
                bestcombi = x
    if bestsumme > target:
        return lvm.index(min(bestcombi))
    if bestsumme < target and ballons:
        return lvm.index(min(lvm))
    return -1

   
def schale_fuellen(lvm,ballons,info):
    '''
    returned den inhalt der schale, bei dem versuch, immer genau
    20 zu erreichen. Wenn dies nicht erreicht wird, wird eine größere
    Zahl zurückgegeben. Wenn es unmöglich ist, die Schale bis
    zu mindestens 20 aufzufüllen, wird -1 zurückgegeben.
    '''
    target = 20
    schale = 0
    fach = 0
    while fach >= 0 and schale < 20:
        fach = nextfach(target,lvm,ballons)
        if fach == -1:
            if info:
                print('Keine Füllung mehr möglich')
            return -1
        #print('lvm:',*lvm,'fuellliste:',*ballons)
        anzahl = lvm[fach]
        if info:
            print('Kippe {} Ballons aus Fach {}'.format(lvm[fach],fach))
        schale += anzahl
        target -= anzahl
        if ballons:
           lvm[fach] = ballons.pop(0)
        else:
           lvm[fach] = 0
    return schale
 

def verpacke(nr,info=False):   
    lvm,ballons = init_data(nr)
    verpackt = 0
    pack = {}    # protokolliert die Verpackungen
    while True:
       a = schale_fuellen(lvm,ballons,info)
       if a == -1:
           break
       verpackt += a   
        
       if a in pack:
           pack[a]+=1
       else:
           pack[a]=1
       if info:
           print('Es werden verpackt: ',a)
    print(i,pack,'verpackt',verpackt,'Rest',sum(lvm))

for i in range(1,8):
    verpacke(i) 







