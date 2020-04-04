tn = [7,10,14,16,18,19,20,24,26,29,30,32]
al = [10,24,30]

tn = [-10000] + tn + [10000]
al = [-10000] + al + [10000]

def getroffen(tn, al, d):
    '''
    tn, al - Liste der Teilnehmer / Al-Zahlen
    d - int zwischen 0 und 1000
    returns: liste der zahlen aus tn, die näher an d liegen als an irgendeiner anderen zahl aus al
    '''


def abstand(d, al):
    '''
    d: int,  0-1000
    al: list, Al-Zahlen
    returns: minimaler Abstand von d zu den Zahlen aus al
    '''
    return min([abs(x-d) for x in al])


def kostenabschnitt(tn,i,j):
 
    '''
    i, j - Indizes aus tn mit i < j
    tn[i], tn[j] sind die Ränder eines Intervalls 
    returns: summe der minimalen Abstände aller Zahlen im Intervall zu den Rändern
    '''
    kosten = 0
    for k in range(i,j+1):
        kosten += min(abs(tn[i]-tn[k]),abs(tn[k]-tn[j]))
    return kosten


def berechneOptimaleLoesung(tn,m):
    '''
    tn: sortierte Liste der Teilnehmewerte, incl. dummies
    m: int Anzahl der Werte für Al, 0 <= m <= len(tn)

    '''
    inf = float('inf')
    N = len(tn)
    tmp = [0]*m
    kosten = [tmp[:] for i in range(N)]  
    loesung = [tmp[:] for i in range(N)]  
 
    for i in range(N):
        kosten[i][0] = kostenabschnitt(tn,i,N-1)

    for l in range(m):
        for i in range(N):
            kosten[i][l] = inf
            for j in range(i+1,N-1):
                if kostenabschnitt(tn,i,j) + kosten[j][l-1] < kosten[i][l]:
                    loesung[i][l] = j
                    kosten[i][l] = kostenabschnitt(tn,i,j) + kosten[j][l-1]
    

    ausgabe = []
    i = 0
    for l in range(m-1,-1,-1):
        i = loesung[i][l]
        ausgabe.append(tn[i])

    return ausgabe, kosten[0][m-1]



print(berechneOptimaleLoesung(tn,3))

