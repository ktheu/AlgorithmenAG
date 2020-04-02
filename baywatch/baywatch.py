dir = './Bwinf/bwinf37-runde1/j2-Baywatch/beispieldaten/'
file = 'baywatch6.txt'
#
# diese Lösung hält sich stark an den Pseudocode der Lösungshinweise
#
f = open(dir+file)
georg = f.readline().split()
karte = f.readline().split()
f.close

n = len(karte)
for i in range(n):
    nochKorrekt = True
    for j in range(n):
        indexGeorg = (i + j) % n
        indexKarte = j
        if georg[indexGeorg] != karte[indexKarte] and karte[indexKarte] != '?':
            nochKorrekt = False
            break
    if nochKorrekt:
        print('Verschiebung',i)
        for j in range(n):
            print( georg[(i+j) % n], end= ' ')
        print()

  
    