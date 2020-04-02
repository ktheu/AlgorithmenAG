## Baywatch

37. Bundeswettbewerb Informatik - Runde 1 - J2

[Aufgabenstellung](./baywatch.pdf)


#### Hinweise zu den Beispieldaten

[Beispieldaten](./beispieldaten/)

Zu dieser Aufgabe gibt es sechs Textdateien mit Beispieleingaben für verschiedene Amöben-Inseln, wobei die erste Datei das Beispiel für die Insel „Big Amoeba“ in der Aufgabenstellung enthält.

Jede Datei enthält:

* in der ersten Zeile durch Leerzeichen voneinander getrennte Ziffern von 1 bis maximal 9, die die unterschiedlichen Beschaffenheiten einer vollständigen Landzungen-Liste von George repräsentieren (1: Wald, 2: Wiese, 3: Häuser, 4: Wüste, 5: See, 6: Sumpf, 7: Reisfeld, 8: Berg, 9: Vulkankrater),
* in der zweiten Zeile die unvollständige Landzungen-Liste von Longstock mit einzelnen Fragezeichen für unbekannte Beschaffenheiten an Stelle von Ziffern wie im Beispiel in der Aufgabenstellung.

Jede Zeile kann bis zu 500 Zeichen umfassen.


#### Pseudocode

```
kartenliste = Liste von der Landkarte mit Fragezeichen
georgliste = vollständige Liste von Georg
 
für alle möglichen Verschiebungen k:
    wenn um k verschobene georgliste auf kartenliste passt:
        gib verschobe georgliste aus
        beende das Programm

```        
 


#### Welche Funktionen bieten sich an?

```
def schieb(a, k):
    '''
    a: Liste,
    k: schiebeZahl, 0 <= k < len(a)
    returns: Liste, um k verschoben, d.h. die vorderen k Elemente wurden 
        nacheinander nach hinten versetzt.
    '''

```


```
def passt(a,b):
    '''
    a: Liste mit Fragezeichen an manchen Stellen, b: Liste
    returns True, falls a gleich b an allen nicht-Fragezeichen Stellen
    ''' 

```

#### Notizen

Da es Fragezeichen gibt, werden die Daten der Listen als String eingelesen.


### Python

```
file = './beispieldaten/baywatch2.txt'
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
```

### Javascript



```
const fs = require('fs');
let f = fs.readFileSync('./beispieldaten/baywatch1.txt', 'utf-8');

let input = f.split('\r\n');
let georg = input[0].split(' ')
let karte = input[1].split(' ')


function schieb(a, k) {
    /*
     a: Liste,
     k: schiebeZahl, 0 <= k < len(a)
     returns: Liste, um k verschoben, d.h. die vorderen k Elemente wurden 
         nacheinander nach hinten versetzt.
    */
    let n = a.length;
    return [...Array(n).keys()].map((x) => a[(x + k) % n]);
}


function passt(a, b) {
    /*
    a: Liste mit Fragezeichen an manchen Stellen, b: Liste
    returns True, falls a gleich b an allen nicht-Fragezeichen Stellen
    */
    for (let i = 0; i < a.length; i++) {
        if (a[i] != '?' && a[i] != b[i]) return false;
    }
    return true;
}

for (let k = 0; k < karte.length; k++) {
    if (passt(karte, schieb(georg, k))) {
        console.log('Verschiebung', k)
        console.log(schieb(georg,k).join(' '))
    }
}
```


Ausgabe für baywatch1.txt

```
Verschiebung 12
3 1 1 2 3 4 1 5 1 2 6 4 5
```
