## Landnahme


34. Jugendwettbewerb Informatik - J1

[Aufgabenstellung](./landnahme.pdf)

[Lösungshinweise](./landnahme_loesungshinweise.pdf)


#### Python

```
class Koordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '('+str(self.x)+'/'+str(self.y)+')'
    
class Rechteck:
    def __init__(self, ecke1, ecke2):
        self.ecke1 = ecke1
        self.ecke2 = ecke2
        self.genehmigt = False
        
    def __str__(self):
        entscheidung = "genehmigt"
        if not self.genehmigt:
            entscheidung = "abgelehnt"
        return str(self.ecke1) + " " + str(self.ecke2) + " " + entscheidung
        
    def links(self):
        '''
        returns: die x-Koordinate der linken Seite
        '''
        return min(self.ecke1.x,self.ecke2.x)
    
    def rechts(self):
        '''
        returns: die x-Koordinate der rechten Seite
        '''
        return max(self.ecke1.x,self.ecke2.x)
    
    def oben(self):
        '''
        returns: die y-Koordinate der oberen Seite
        '''
        return max(self.ecke1.y,self.ecke2.y) 
        
    def unten(self):
        '''
        returns: die y-Koordinate der oberen Seite
        '''
        return min(self.ecke1.y,self.ecke2.y)
    
    def rechtsVon(self,other):
        '''
        other: Rechteck
        returns: True, wenn dieses Rechteck rechts von other
        '''
        return other.rechts() <= self.links()
    
    def linksVon(self,other):
        '''
        other: Rechteck
        returns: True, wenn dieses Rechteck rechts von other
        '''
        return self.rechts() <= other.links()
    
    def oberhalbVon(self,other):
        '''
        other: Rechteck
        returns: True, wenn dieses Rechteck rechts von other
        '''
        return other.oben() <= self.unten()
    
    def unterhalbVon(self,other):
        '''
        other: Rechteck
        returns: True, wenn dieses Rechteck rechts von other
        '''
        return self.oben() <= other.unten()
    
    def kollidiertMit(self,other):
        return not (self.rechtsVon(other) or self.linksVon(other)
                    or self.oberhalbVon(other) or self.unterhalbVon(other))

    def genehmige(self):
        self.genehmigt = True

r1 = Rechteck(Koordinate(2,3),Koordinate(5,5))
r2 = Rechteck(Koordinate(1,2),Koordinate(4,4))
r3 = Rechteck(Koordinate(3,1),Koordinate(6,3))

liste = [r1,r2,r3]
r1.genehmige()
for j in range(1,len(liste)):
   for i in range(j):
       if not liste[j].kollidiertMit(liste[i]):
           liste[j].genehmige()

for r in liste:
   print(r)


```

Ausgabe:

```
(2/3) (5/5) genehmigt
(1/2) (4/4) abgelehnt
(3/1) (6/3) genehmigt
```
