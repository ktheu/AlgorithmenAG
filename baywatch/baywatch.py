 
file = './beispieldaten/baywatch1.txt'
f = open(file)
georg = f.readline().split()
karte = f.readline().split()

def schieb(a, k):
    '''
    a: Liste,
    k: schiebeZahl, 0 <= k < len(a)
    returns: Liste, um k verschoben, d.h. die vorderen k Elemente wurden 
        nacheinander nach hinten versetzt.
    '''
    return [a[ (i+k) % len(a)] for i in range(len(a))]

 
def passt(a,b):
    '''
    a: Liste mit Fragezeichen an manchen Stellen, b: Liste
    returns True, falls a gleich b an allen nicht-Fragezeichen Stellen
    ''' 
    for x,y  in zip(a,b):
        if x != '?' and x != y: return False
    return True

for k in range(len(karte)):
    if passt(karte, schieb(georg,k)):
        print('Verschiebung',k)
        print(*schieb(georg,k))

 

  
    