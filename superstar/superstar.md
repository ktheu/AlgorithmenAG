## Superstar

37. Bundeswettbewerb Informatik - Runde 1 - A2

[Aufgabenstellung](./superstar.pdf)

[Lösungshinweise](./superstar_loesungshinweise.pdf)


#### Hinweise zu den Beispieldaten

[Beispieldaten](./beispieldaten/)

Zu dieser Aufgabe gibt es vier Textdateien mit Beispieleingaben, wobei die erste Datei das Beispiel in der Aufgabenstellung enthält.

Jede Datei enthält bis zu 5.000 Zeilen, und jede Zeile ist bis zu 500 Zeichen lang.

Dabei enthält:

* die erste Zeile die durch Leerzeichen voneinander getrennten Namen aus dem TeeniGram-Netzwerk,
* jede der folgenden Zeilen jeweils die Information „X Y“ über zwei beliebige Namen X und Y, wenn X Y folgt.

#### Überlegungen

Es kann entweder nur einen oder keinen superstar geben. Mit jeder Anfrage kann ein Kandidat ausgeschlossen werden:

```
folgt(x,y) = true => x kann nicht superkandidat sein
folgt(x,y) = false => y kann nicht superkandidat sein
```

Diese Anfrage kann man immer wieder machen, bis höchstens noch 1 Element übrigbleibt. Da man von dem übriggebliebenenn Element nicht weiß, ob man es mit allen anderen verglichen hat, oder nur mit einer Teilmenge, muss man also nochmal 
überprüfen, ob es wirklich superstar ist. Dazu muss man überprüfen, ob alle ihm folgen und ob er wirklich keinem anderen folgt. Wenn man sich die vorherigen Anfragen merkt, kann man sich doppelte Anfragen sparen

Die Folgen-Beziehung können wir als einen gerichteten, ungewichteten Graphen modellieren:

Wir holen aus der Datenstruktur immer zwei Elemente für die Anfrage heraus. Eines davon fällt als superstar weg, das andere fügen wir wieder ein. Wir wählen als Datenstruktur eine Schlange. (Wir könnten auch einen stack wählen, ob das zu weniger
oder mehr Abfragen führt, hängt von den Eingabedaten ab).

```
folgenMap[k] = Menge der Namen, denen k folgt
```

Das AnfrageMemo implementieren wir ebenfalls als dictionary, die Frage ist der key und die Antwort der value. 

#### Pseudocode

```
a = Liste mit den Mitgliedern
q = Kopie der Liste als Schlange
anfrageMemo = {}
folgenMap = dict mit namen als key und Menge der namen, denen key folgt, als value
zaehl = 0

def folgt(x,y):
     falls (x,y) in anfrageMemo, return dessen antwort
     sonst 
        print(Anfrage: folgt(x,y))
        zaehl++
        return x in folgenMap und y in folgenMap[x]    # dies ist eine Anfrage

def checkSuperstar(y):
    für alle x in a, die nicht y sind:
          falls folgt(y,x) oder !folgt(x,y); return False
    return True
   
while len(q) > 1:
    hole die ersten beiden Elemente x,y aus der Schlange:
    if folgt(x,y): 
         füge y wieder in die Schlange ein
         anfrageMemo[(x,y)] = true
    else:
         anfrageMemo[(x,y)] = false
         füge x wieder in die Schlange ein

hole verbleibendes element xs aus schlange q
istSuperstar = checkSuperstar(xs)

if (istSuperstar): print(xs ist superstar, zaehl Anfragen)
else: print(es gibt keinen superstar, zaehl Anfragen)
```

#### Python

```
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
f = open('./beispieldaten/superstar4.txt')
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

z1 = zaehl                    # Anzahl Abfragen nach der Suche
print(checkSuperstar(kandidat))
print('**** Anzahl Abfragen fuer die Suche ****',z1)
print('**** Anzahl Abfragen fuer die Ueberpruefung ****',zaehl-z1)
print('**** Gesamtzahl Abfragen ****', zaehl)

```

#### Ausgaben

Beispiel1:

```
Anfrage: Selena folgt Justin
Anfrage: Hailey folgt Justin
**** Kandidat ist Justin
Anfrage: Justin folgt Selena
Anfrage: Justin folgt Hailey
True
**** Anzahl Abfragen fuer die Suche **** 2
**** Anzahl Abfragen fuer die Ueberpruefung **** 2
**** Gesamtzahl Abfragen **** 4
```

Beispiel2:

```
Anfrage: Turing folgt Hoare
Anfrage: Dijkstra folgt Knuth
Anfrage: Codd folgt Hoare
Anfrage: Dijkstra folgt Codd
**** Kandidat ist Dijkstra
Anfrage: Turing folgt Dijkstra
Anfrage: Dijkstra folgt Turing
Anfrage: Hoare folgt Dijkstra
Anfrage: Dijkstra folgt Hoare
Anfrage: Knuth folgt Dijkstra
Anfrage: Codd folgt Dijkstra
True
**** Anzahl Abfragen fuer die Suche **** 4
**** Anzahl Abfragen fuer die Ueberpruefung **** 6
**** Gesamtzahl Abfragen **** 10

```   

Beispiel3:

```
Anfrage: Edsger folgt Jitse
Anfrage: Jorrit folgt Peter
Anfrage: Pia folgt Rineke
Anfrage: Rinus folgt Sjoukje
Anfrage: Jitse folgt Jorrit
Anfrage: Pia folgt Rinus
Anfrage: Jitse folgt Pia
**** Kandidat ist Jitse
Anfrage: Jitse folgt Edsger
False
**** Anzahl Abfragen fuer die Suche **** 7
**** Anzahl Abfragen fuer die Ueberpruefung **** 1
**** Gesamtzahl Abfragen **** 8
```

Beispiel4:

```
Anfrage: Hanna folgt Melker
Anfrage: Liv folgt Ellen
Anfrage: Ali folgt Lova
Anfrage: Vide folgt Freja
Anfrage: Melvin folgt Loke
Anfrage: Sigge folgt Milton
Anfrage: Sofia folgt Arvid
Anfrage: Albin folgt Sixten
Anfrage: Marta folgt Celine
Anfrage: Joel folgt Colin
Anfrage: Melissa folgt Jonathan
Anfrage: August folgt Frank
Anfrage: Jack folgt Folke
Anfrage: Tuva folgt Isabelle
Anfrage: Wilmer folgt Isabella
Anfrage: Signe folgt Leon
Anfrage: Noomi folgt Linnea
Anfrage: Bianca folgt Gabriel
Anfrage: Hedvig folgt Alvin
Anfrage: Milian folgt Idun
Anfrage: Alicia folgt Frans
Anfrage: Viggo folgt Noel
Anfrage: Axel folgt Siri
Anfrage: Majken folgt Theo
Anfrage: Emelie folgt Oscar
Anfrage: Olle folgt Casper
Anfrage: Ebbe folgt Samuel
Anfrage: John folgt Nils
Anfrage: Lykke folgt Emilia
Anfrage: Ville folgt Ella
Anfrage: Leo folgt Selma
Anfrage: Oliver folgt Clara
Anfrage: Thea folgt Alexander
Anfrage: Benjamin folgt Joline
Anfrage: Harry folgt Saga
Anfrage: Erik folgt Levi
Anfrage: Cleo folgt Vilgot
Anfrage: Lucas folgt Svea
Anfrage: Sebastian folgt Charlie
Anfrage: Penny folgt Rut
Anfrage: Hanna folgt Liv
Anfrage: Lova folgt Vide
Anfrage: Melvin folgt Milton
Anfrage: Arvid folgt Sixten
Anfrage: Celine folgt Joel
Anfrage: Melissa folgt August
Anfrage: Folke folgt Isabelle
Anfrage: Isabella folgt Leon
Anfrage: Noomi folgt Gabriel
Anfrage: Alvin folgt Milian
Anfrage: Frans folgt Noel
Anfrage: Axel folgt Majken
Anfrage: Emelie folgt Olle
Anfrage: Ebbe folgt John
Anfrage: Emilia folgt Ville
Anfrage: Selma folgt Clara
Anfrage: Alexander folgt Benjamin
Anfrage: Saga folgt Levi
Anfrage: Vilgot folgt Svea
Anfrage: Charlie folgt Rut
Anfrage: Hanna folgt Lova
Anfrage: Milton folgt Sixten
Anfrage: Celine folgt Melissa
Anfrage: Folke folgt Leon
Anfrage: Gabriel folgt Milian
Anfrage: Noel folgt Majken
Anfrage: Emelie folgt Ebbe
Anfrage: Emilia folgt Selma
Anfrage: Alexander folgt Saga
Anfrage: Vilgot folgt Charlie
Anfrage: Hanna folgt Sixten
Anfrage: Melissa folgt Folke
Anfrage: Gabriel folgt Noel
Anfrage: Emelie folgt Emilia
Anfrage: Saga folgt Charlie
Anfrage: Sixten folgt Folke
Anfrage: Noel folgt Emilia
Anfrage: Charlie folgt Folke
Anfrage: Noel folgt Folke
**** Kandidat ist Folke
Anfrage: Hanna folgt Folke
Anfrage: Folke folgt Hanna
Anfrage: Melker folgt Folke
Anfrage: Folke folgt Melker
Anfrage: Liv folgt Folke
Anfrage: Folke folgt Liv
Anfrage: Ellen folgt Folke
Anfrage: Folke folgt Ellen
Anfrage: Ali folgt Folke
Anfrage: Folke folgt Ali
Anfrage: Lova folgt Folke
Anfrage: Folke folgt Lova
Anfrage: Vide folgt Folke
Anfrage: Folke folgt Vide
Anfrage: Freja folgt Folke
Anfrage: Folke folgt Freja
Anfrage: Melvin folgt Folke
Anfrage: Folke folgt Melvin
Anfrage: Loke folgt Folke
Anfrage: Folke folgt Loke
Anfrage: Sigge folgt Folke
Anfrage: Folke folgt Sigge
Anfrage: Milton folgt Folke
Anfrage: Folke folgt Milton
Anfrage: Sofia folgt Folke
Anfrage: Folke folgt Sofia
Anfrage: Arvid folgt Folke
Anfrage: Folke folgt Arvid
Anfrage: Albin folgt Folke
Anfrage: Folke folgt Albin
Anfrage: Folke folgt Sixten
Anfrage: Marta folgt Folke
Anfrage: Folke folgt Marta
Anfrage: Celine folgt Folke
Anfrage: Folke folgt Celine
Anfrage: Joel folgt Folke
Anfrage: Folke folgt Joel
Anfrage: Colin folgt Folke
Anfrage: Folke folgt Colin
Anfrage: Folke folgt Melissa
Anfrage: Jonathan folgt Folke
Anfrage: Folke folgt Jonathan
Anfrage: August folgt Folke
Anfrage: Folke folgt August
Anfrage: Frank folgt Folke
Anfrage: Folke folgt Frank
Anfrage: Folke folgt Jack
Anfrage: Tuva folgt Folke
Anfrage: Folke folgt Tuva
Anfrage: Isabelle folgt Folke
Anfrage: Wilmer folgt Folke
Anfrage: Folke folgt Wilmer
Anfrage: Isabella folgt Folke
Anfrage: Folke folgt Isabella
Anfrage: Signe folgt Folke
Anfrage: Folke folgt Signe
Anfrage: Leon folgt Folke
Anfrage: Noomi folgt Folke
Anfrage: Folke folgt Noomi
Anfrage: Linnea folgt Folke
Anfrage: Folke folgt Linnea
Anfrage: Bianca folgt Folke
Anfrage: Folke folgt Bianca
Anfrage: Gabriel folgt Folke
Anfrage: Folke folgt Gabriel
Anfrage: Hedvig folgt Folke
Anfrage: Folke folgt Hedvig
Anfrage: Alvin folgt Folke
Anfrage: Folke folgt Alvin
Anfrage: Milian folgt Folke
Anfrage: Folke folgt Milian
Anfrage: Idun folgt Folke
Anfrage: Folke folgt Idun
Anfrage: Alicia folgt Folke
Anfrage: Folke folgt Alicia
Anfrage: Frans folgt Folke
Anfrage: Folke folgt Frans
Anfrage: Viggo folgt Folke
Anfrage: Folke folgt Viggo
Anfrage: Folke folgt Noel
Anfrage: Axel folgt Folke
Anfrage: Folke folgt Axel
Anfrage: Siri folgt Folke
Anfrage: Folke folgt Siri
Anfrage: Majken folgt Folke
Anfrage: Folke folgt Majken
Anfrage: Theo folgt Folke
Anfrage: Folke folgt Theo
Anfrage: Emelie folgt Folke
Anfrage: Folke folgt Emelie
Anfrage: Oscar folgt Folke
Anfrage: Folke folgt Oscar
Anfrage: Olle folgt Folke
Anfrage: Folke folgt Olle
Anfrage: Casper folgt Folke
Anfrage: Folke folgt Casper
Anfrage: Ebbe folgt Folke
Anfrage: Folke folgt Ebbe
Anfrage: Samuel folgt Folke
Anfrage: Folke folgt Samuel
Anfrage: John folgt Folke
Anfrage: Folke folgt John
Anfrage: Nils folgt Folke
Anfrage: Folke folgt Nils
Anfrage: Lykke folgt Folke
Anfrage: Folke folgt Lykke
Anfrage: Emilia folgt Folke
Anfrage: Folke folgt Emilia
Anfrage: Ville folgt Folke
Anfrage: Folke folgt Ville
Anfrage: Ella folgt Folke
Anfrage: Folke folgt Ella
Anfrage: Leo folgt Folke
Anfrage: Folke folgt Leo
Anfrage: Selma folgt Folke
Anfrage: Folke folgt Selma
Anfrage: Oliver folgt Folke
Anfrage: Folke folgt Oliver
Anfrage: Clara folgt Folke
Anfrage: Folke folgt Clara
Anfrage: Thea folgt Folke
Anfrage: Folke folgt Thea
Anfrage: Alexander folgt Folke
Anfrage: Folke folgt Alexander
Anfrage: Benjamin folgt Folke
Anfrage: Folke folgt Benjamin
Anfrage: Joline folgt Folke
Anfrage: Folke folgt Joline
Anfrage: Harry folgt Folke
Anfrage: Folke folgt Harry
Anfrage: Saga folgt Folke
Anfrage: Folke folgt Saga
Anfrage: Erik folgt Folke
Anfrage: Folke folgt Erik
Anfrage: Levi folgt Folke
Anfrage: Folke folgt Levi
Anfrage: Cleo folgt Folke
Anfrage: Folke folgt Cleo
Anfrage: Vilgot folgt Folke
Anfrage: Folke folgt Vilgot
Anfrage: Lucas folgt Folke
Anfrage: Folke folgt Lucas
Anfrage: Svea folgt Folke
Anfrage: Folke folgt Svea
Anfrage: Sebastian folgt Folke
Anfrage: Folke folgt Sebastian
Anfrage: Folke folgt Charlie
Anfrage: Penny folgt Folke
Anfrage: Folke folgt Penny
Anfrage: Rut folgt Folke
Anfrage: Folke folgt Rut
True
**** Anzahl Abfragen fuer die Suche **** 79
**** Anzahl Abfragen fuer die Ueberpruefung **** 151
**** Gesamtzahl Abfragen **** 230
```