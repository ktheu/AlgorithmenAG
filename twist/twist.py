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
 leider hat der vscode output keine utf8-codierung, 
 deswegen wird Ergebnis noch in eine datei geschrieben
'''
for line in lines:
    newline = twist(line)
    print(newline)
    fout.write(newline+'\n')

fout.close()
f.close()







 







