def folgt(x,y):
    if (x,y) in anfrageMemo: return anfrageMemo[(x,y)]
    global zaehl
    print('Anfrage: {} folgt {}'.format(x,y))
    zaehl += 1
    antwort =  x in folgenMap and y in folgenMap[x] 
    anfrageMemo[(x,y)] = antwort
    return antwort

def checkSuperstar(y):
    for x in a:
        if x != y and (not folgt(x,y) or folgt(y,x)):
            return False
    return True


from collections import deque
f = open('./beispieldaten/superstar1.txt')
daten = [s.strip() for s in f.readlines()]

a = daten.pop(0).split()    
zaehl = 0

folgenMap = {}     
for d in daten:
    x,y = d.split()
    if x in folgenMap:
        folgenMap[x].add(y)
    else:
        folgenMap[x] = {y}

anfrageMemo = {}   
q = deque(a)
while len(q) > 1:
    x = q.popleft()
    y = q.popleft()
    if folgt(x,y):
        q.append(y)
    else:
        q.append(x)

kandidat = q[0]
print('**** Kandidat ist {}'.format(kandidat))

z1 = zaehl                  # Anzahl Abfragen nach der Suche
print(checkSuperstar(kandidat))
print('**** Anzahl Abfragen fuer die Suche ****',z1)
print('**** Anzahl Abfragen fuer die Ueberpruefung ****',zaehl-z1)
print('**** Gesamtzahl Abfragen ****', zaehl)





