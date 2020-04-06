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







 