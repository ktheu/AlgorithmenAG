from itertools import combinations
from collections import deque

def bestwahl(lvm,target):
    '''
    returns: index des Elements, das für target gewählt werden soll

    Falls mit einer Kombination das target genau getroffen wird, wird er
    Index des größten Elements der Kombination zurückgegeben.

    Falls das target nicht genau getroffen wird, wird der Index des kleinesten Elements der
    Kombination zurückgegeben, die möglichst wenig über der 20 ist.

    Falls mit allen Zahlen das target nicht ereicht wird, wird der Index mit der kleinsten Zahl > 0
    zurückgegeben.
    
    '''

    if sum(lvm) < target:             # target kann nicht erreicht werden
        return lvm.index(min(lvm))    

    bestwahl = None
    bestsumme = -1

    for i in range(1,11):
        for x in combinations(lvm,i):
            summe = sum(x)
            if summe == target:             # target wird genau erreicht
                return lvm.index(max(x))  
            if 20 < summe < bestsumme:
                bestsumme = summe
                bestwahl = x
    
    if bestsumme == -1:                     # target wird nicht erreicht 
        return lvm.index(min([x for x in lvm if x > 0])) 
    else:
        return lvm.index(min(bestwahl))     # wert über target wurde erreicht

f = open('./beispieldaten/luftballons1.txt')
a = [int(x.rstrip('\n')) for x in f.readlines()]
lvm = a[:10]
ballons = a[10:]  
ballons = deque(ballons)          # Schlange

schale = 0    
verpackt = 0 
target = 20
while ballons or schale + sum(lvm) >= 20:  
    i = bestwahl(lvm,target)
    anzahl = lvm[i]
    if (ballons):
        lvm[i] = ballons.popleft()
    else:
        lvm[i] = 0
    target -= anzahl
    schale += anzahl
    verpackt += anzahl
    if schale >= 20:
        print("Verpacke {} Ballons".format(schale))
        target = 20
        schale = 0

print('Es wurden insgesamt {} Ballons verpackt. Der Rest ist {}'.format(verpackt,sum(lvm)))
    

