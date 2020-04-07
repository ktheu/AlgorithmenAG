import itertools

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



f = open('./beispieldaten/luftballons7.txt')
a = [int(x.rstrip('\n')) for x in f.readlines()]
lvm = a[:10]
ballons = a[10:]

schale = 0    
verpackt = 0 
while ballons or sum(lvm)+schale >= 20:      # solange es noch Ballons gibt oder (falls es keine mehr gibt) 
                                            # wenigstens noch so viele im Spiel sind, dass es für eine Packung reicht
    schale = schale_fuellen(lvm,ballons)
    verpackt+=schale
    if schale == 0:
        print('Keine weitere Füllung möglich')
        break
    print('Bisher verpackt:',verpackt)

print('Es wurden insgesamt {} Ballons verpackt. Der Rest ist {}'.format(verpackt,sum(lvm)))
    

