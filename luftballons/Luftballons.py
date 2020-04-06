# -*- coding: utf-8 -*-
import itertools
datapath = 'Bwinf/luftballons/myLoesung/'
datapath = ''


def init_data(nr):
    '''
    nr: int, Nummer der Eingabedata
    k: laenge der lvm k >= 1
    returns: tupel lvm, ballons
        lvm: Liste mit der SchalenBelegung
        ballons: Liste mit den Ballons, die nachgefüllt werden.
    
    '''
    with open(datapath+'luftballons'+str(nr)+'.txt') as f:
       ballons = f.read().splitlines()
    ballons = [int(k) for k in ballons]
    lvm = ballons[:10]
    ballons = ballons[10:]
    return lvm,ballons


def bestwahl(lvm,target):
    '''
    returns: Tupel aus Liste und int
    Die Liste ist eine Liste der Indizes, mit der man die Summe target
    erreichen kann. Wenn target nicht genau erreicht wird, dann
    soll die Summe möglichst wenig über target sein. Wenn auch
    das nicht geht, soll die leere Liste zurückgegeben werden.
    Die Zahl ist die erreichte Summe (0 bei leerer Liste, wenn 
    alles gut geht target, sonst halt drüber).
    '''
    faecher = list(range(len(lvm)))  # Liste mit den Fächerindizes
    bestwahl = ()
    bestsumme = 0
    for i in range(len(lvm)):
        for x in itertools.combinations(faecher,i):
            summe = sum(lvm[k] for k in x)
            if summe == target:
                return list(x),target
            else:
                if (bestsumme == 0 and summe > target) or (target < summe < bestsumme):
                    bestsumme = summe
                    bestwahl = x
    return list(bestwahl), bestsumme    
            


def kippen_und_nachfuellen(fachnr,lvm,ballons):
    '''
    Aus dem Fach mit nr fachNr werden die Ballons in die schale gekippt,
    Die Schale wird dann mit der nächsten Zahl aus der Liste ballons
    aufgefüllt, falls da noch was drin ist. Sonst wird sie auf 0 gesetzt.
    fachnr, schale: int
    lvm, ballons: list
    returns: anzahl Ballons, die in die Schale gekippt wurden,
       ändert lvm und ballons
    '''
    anzahl_ballons = lvm[fachnr]
    if ballons: 
        lvm[fachnr] = ballons.pop(0)
    else:
        lvm[fachnr] = 0
    return anzahl_ballons
    

def schale_fuellen(lvm,ballons):
    target = 20
    schale = 0

    while schale < 20:
        print('lvm:',*lvm,'fuellliste:',*ballons)
        wahl, _ = bestwahl(lvm,target)
        if len(wahl) == 0:
            return 0
        fachnr = wahl[0]
        anzahl = kippen_und_nachfuellen(fachnr,lvm,ballons)
        target = target - anzahl
        schale += anzahl
        print('Kippe {} Ballons aus Fach {} aus: {} in der Schale'.format(anzahl,fachnr+1,schale))
    print('lvm:',*lvm,'fuellliste:',*ballons)    
    return schale


import unittest
class MyClassTest(unittest.TestCase):
    def test_init_data(self):
        lvm, ballons = init_data(1)
        self.assertListEqual(lvm,[5,3,8,3,6,2,8,4,2,2])
        self.assertListEqual(ballons,[9,1,3,11,6,4,7,5])
        wahl, summe = bestwahl(lvm,20)
        self.assertListEqual(wahl,[2,6,7])
        self.assertEqual(summe,20)
        fachnr = wahl[0]
        self.assertEqual(fachnr,2)
        anzahl = kippen_und_nachfuellen(fachnr,lvm,ballons)
        self.assertEqual(anzahl,8)

        
#if __name__ == '__main__':
 #   unittest.main()     

schale = 0    
verpackt = 0 
lvm, ballons = init_data(3)

while ballons or sum(lvm)+schale > 20:
    schale = schale_fuellen(lvm,ballons)
    verpackt+=schale
    if schale == 0:
        print('Keine weitere Füllung möglich')
        break
    print('Bisher verpackt:',verpackt)

print('Es wurden insgesamt {} Ballons verpackt. Der Rest ist {}'.format(verpackt,sum(lvm)))
    

#fachnr = wahl[0]

#print(schale,'#',*lvm,'#',*ballons)
#fill_lvm(a)
#get_faecher_indizes(a)
#print(*lvm)
#print(*ballons)


# print(lvm)
# tab = [[0]*10 for i in range(21)]
#
# '''
# tab[s][i] genau dann wenn sich die Summe s mit den Fächern 0..i erreichen lässt
# '''
# def ersteEins(tab,zeile):
#
#    for k in range(len(tab[0])):
#        if tab[zeile][k] == 1:
#            return k
#    return -1
#
#
# i = 0
# anzahl = lvm[i]
# print("im Fach {} sind {} Luftballone".format(i,anzahl))
# tab[anzahl][i]= 1
#
#
# for i in range(1,10):
#    anzahl = lvm[i]
#    print("im Fach {} sind {} Luftballone".format(i,anzahl))
#    tab[anzahl][i]= 1
#    for j in range(21):
#        if tab[j][i-1] == 1 and j+anzahl <= 20:
#            tab[j+anzahl][i] = 1
#            tab[j][i] = 1
#
#
# header = [i for i in range(10)]
# print(" ".rjust(2),':',*header)
#
# for i in range(21):
#    print(str(i).rjust(2),':',*tab[i])
#
#
#
#
# print(faecher)
