

class Rechteck:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.genehmigt = False

    def __str__(self):
        return '{} {} {} {}'.format(self.x1, self.y1, self.x2, self.y2)
 
    def linksVon(self, other):
        return max(self.x1, self.x2) <= min(other.x1, other.x2)

    def unterhalbVon(self, other):
        return max(self.y1, self.y2) <= min(other.y1, other.y2)

    def kollidiertMit(self, other):
        return not (self.linksVon(other) or other.linksVon(self)
                    or self.unterhalbVon(other) or other.unterhalbVon(self))


r1 = Rechteck(2, 3, 5, 5)
r2 = Rechteck(1, 2, 4, 4)
r3 = Rechteck(3, 1, 6, 3)

rechtecke = [r1, r2, r3]
r1.genehmigt = True
for j in range(1, len(rechtecke)):
    rechtecke[j].genehmigt = True
    for i in range(j):
        if rechtecke[i].genehmigt and rechtecke[i].kollidiertMit(rechtecke[j]):
            rechtecke[j].genehmigt = False
            break

for r in rechtecke:
    entscheidung = "genehmigt" if r.genehmigt else "abgelehnt"
    print(r, entscheidung)
