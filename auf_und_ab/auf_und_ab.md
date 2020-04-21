## Auf und Ab

37. Bundeswettbewerb Informatik - Runde 1 - J1 

[Aufgabenstellung](./auf_und_ab.pdf)  -  [Spielbrett](./leiterspiel.pdf)


[Lösungshinweise](./auf_und_ab_loesungshinweise.pdf)


#### Pseudocode 

```
N = gewählte Schrittlänge
pos = aktuelle Position (0-100)
visited = set mit den schon besuchten feldern 
zaehl = 0   Anzahl Schritte

while pos != 100 and pos nicht in visited:
    zaehl += 1
    rücke von pos aus N Felder vor.
    if auf einem Leiterfeld: gehe auf andere Seite der Leiter

Wenn pos == 100: Gib N und die Anzahl der Züge aus
sonst: Gib aus, dass mit N das Ziel nicht erreicht werden kann und welches Feld doppelt besucht wird.

```

#### Python

```Python
leiter = {6:27, 14:19, 21:53, 31:42, 33:38, 46:62, 51:59, 57:96, 65:85, 68:80, 70:76, 92:98}

runter = {leiter[v]:v for v in leiter}
leiter.update(runter)

def aufUndAb(n):
    pos = 0
    visited = set()
    zaehl = 0

    while pos != 100 and pos not in visited:
        visited.add(pos)
        zaehl+=1
        pos = pos + n  
        if pos > 100:
            pos = 100 - (pos - 100)
        if pos in leiter:
            pos = leiter[pos]
  
    if pos == 100:
        print('Mit {} kann Ziel in {} Wuerfen erreicht werden:'.format(n,zaehl))
    else:
        print('Mit {} kann Ziel nicht erreicht werden. {} wird doppelt besucht.'.format(n,pos))
 
for n in range(1,7):
    aufUndAb(n)

```

#### Javascript


``` Javascript
let a = [[6, 27], [14, 19], [21, 53], [31, 42], [33, 38], [46, 62],
      [51, 59], [57, 96], [65, 85], [68, 80], [70, 76], [92, 98]];
let a1 = [...a].map(([x, y]) => [y, x]);
let leiter = new Map([...a, ...a1]);

function aufUndAb(n) {
    let pos = 0
    let visited = new Set();
    let zaehl = 0

    while (pos != 100 && !visited.has(pos)) {
        visited.add(pos)
        zaehl += 1
        pos = pos + n
        if (pos > 100) {
            pos = 100 - (pos - 100)
        }
        if (leiter.has(pos)) {
            pos = leiter.get(pos)
        }
    }
    
    if (pos === 100) {
        console.log(`Mit ${n} kann Ziel in ${zaehl} Wuerfen erreicht werden`);
    }
    else {
        console.log(`Mit ${n} kann Ziel nicht erreicht werden. ${pos} wird doppelt besucht.`);
    }
}

for (let n=1; n<=6; n++) {
    aufUndAb(n)
}

```

Ausgabe:

```
Mit 1 kann Ziel in 26 Wuerfen erreicht werden.
Mit 2 kann Ziel in 17 Wuerfen erreicht werden.
Mit 3 kann Ziel nicht erreicht werden. 92 wird doppelt besucht.
Mit 4 kann Ziel nicht erreicht werden. 97 wird doppelt besucht.
Mit 5 kann Ziel in 16 Wuerfen erreicht werden.
Mit 6 kann Ziel in 14 Wuerfen erreicht werden.

```
 



 

