## Twist


37. Bundeswettbewerb Informatik - Runde 1 - A2

[Aufgabenstellung](./twist.pdf)

[Lösungshinweise](./twist_loesungshinweise.pdf)


#### Hinweise zu den Beispieldaten

[Beispieldaten](./beispieldaten/)

Zu dieser Aufgabe gibt es fünf Textdateien mit Beispieleingaben zum Twisten, wobei die erste Datei das Beispiel in der Aufgabenstellung enthält.

Jede Datei enthält in einer oder mehreren Zeilen den jeweiligen Text zum Twisten.

Die Textdatei woerterliste.txt enthält eine lange Liste deutscher Wörter (ein Wort pro Zeile); wir erwarten natürlich nicht, dass diese oder eine andere Wörterliste alle möglichen Wörter umfasst, die in einem Text vorkommen können.

Die Textdatei enttwist.txt enthält das Twist-Beispiel in der Aufgabenstellung zum Enttwisten.


#### Überlegungen

Twisten: Mit einem regulären Ausdruck werden die Indizes aller Wörte mit mindestens Länge 4 gefunden und diese werden
dann getwistet.

Enttwisten: Die mitgelieferte woerterliste musste noch ergänzt werden. 
Es wird ein dict erstellt, dass die Normalform eines Wortes mit Länge >=4 dem Wort in der woerterliste zuordnet:
Normalform = kleiner Anfangsbuchstabe, dann sortierte mittlere Buchstaben, dann der Schlussbuchstabe.



#### Python

twisten:
```
def twist(s):
    '''
    s: eine Zeile Text
    returns: alle Wörter in s mit mindestens Länge 4 werden getwisted
    '''
    for m in re.finditer(regex,s):
        i ,j = m.start(0), m.end(0)
        tmp = list(s[i+1:j-1])
        random.shuffle(tmp)
        st = ''.join(tmp)
        s = s[:i+1] + st + s[j-1:]
    return s

import re, random
f = open('./beispieldaten/twist5.txt',encoding='utf-8')
fout = open('./output.txt',"w",encoding='utf-8')
lines = [x.rstrip('\n') for x in f.readlines()]
regex = r'[a-zA-ZüäöÜÄÖß]{4,}'

'''
 leider in vscode der output keine utf8-codierung, 
 deswegen wird das Ergebnis noch in eine datei geschrieben
'''
for line in lines:
    newline = twist(line)
    print(newline)
    fout.write(newline+'\n')

fout.close()
f.close()
```
-----

enttwisten
```
def enttwist(s):
    '''
    s: eine Zeile mit Text
    returns: enttwistete Zeile
    '''    
    for m in re.finditer(regex,s):
        i ,j = m.start(0), m.end(0)
        if j-i <=3: continue
        w = s[i:j]
        w1 = wmap[normalize(w)]
        if w[0].isupper(): w1 = w1[0].upper()+w1[1:]
        s = s[:i]+w1+s[j:]
    return s

def normalize(s):
    ''' s: String aus Buchstaben des deutschen Alphabets mit mindestens Länge 4
    returns: der erste und letzte Buchtabe werden beibehalten, der erste als Kleinbuchstabe
    die inneren Buchstaben werden sortiert. '''
    s0 = s[0].lower()
    sm = ''.join(sorted(list(s[1:-1])))
    return s0+sm+s[-1]

import re 
regex = r'[a-zA-ZüäöÜÄÖß]+'     # Buchstaben des deutschen Alphabets 1-*

# word-map: den normalisierten Formen werden die Wörte aus der Wortliste zugeordnet
fw = open('./beispieldaten/woerterliste.txt',encoding='utf-8')
worte = [x.rstrip() for x in fw.readlines()]
wmap = { normalize(w) : w for w in worte}

f = open('./beispieldaten/enttwist.txt',encoding='utf-8')
fout = open('./output.txt',"w",encoding='utf-8')
lines = [x.rstrip('\n') for x in f.readlines()]
 
for line in lines:
    newline = enttwist(line)
    print(newline)
    fout.write(newline+'\n')
```
