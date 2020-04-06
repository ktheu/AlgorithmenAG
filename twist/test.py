import re, random


s = "Der Twist (Englisch twist = Drehung, Verdrehung) war ein Modetanz im 4/4-Takt,"
#b = [(m.start(0), m.end(0)) for m in re.finditer(regex, s)]
regex = r'[a-zA-ZüäöÜÄÖß]{4,}'
for m in re.finditer(regex,s):
    i ,j = m.start(0), m.end(0)
    print(i,j)

      


