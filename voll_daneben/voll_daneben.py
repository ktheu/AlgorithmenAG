# tn = [7,10,14,16,18,19,20,24,26,29,30,32]
# M = 5

# tn = [7,10,14,16,18,19]
# M = 3

inf = 10000 

f = open('./beispieldaten/beispiel3.txt')
tn = [int(x.rstrip('\n')) for x in f.readlines()]
tn = [-inf] + sorted(tn)
M = 10

N = len(tn)

def abschnitt(i,k):
    ''' kosten des abschnitts i-k, wenn nur i und k gewählt wurden. '''
    
    summe = 0
    for j in range(i,k+1):
        summe += min(tn[j]-tn[i],tn[k]-tn[j])
    return summe

def kosten0(k):
    ''' kosten von k bis zum Ende, wenn außer k keine weitere Zahl gewählt wurde '''
    summe = 0
    for i in range(k,len(tn)):
        summe+=tn[i]-tn[k]
    return summe
 
def kosten(i,m, memo):
    ''' kosten von i bis zum Ende, wenn außer i höchstens noch m Zahlen gewählt werden dürfen '''
    if m == 0: return kosten0(i)
    if (i,m) in memo: return memo[(i,m)]

    minKost = inf
    minIndx = -1
    for k in range(i+1,N):
        if abschnitt(i,k) + kosten(k,m-1,memo) < minKost:
             minKost = abschnitt(i,k) + kosten(k,m-1,memo)
             minIndx = k
    wahl[(i,m)] = minIndx   
    memo[(i,m)] = minKost
    
    return minKost 

wahl = {}
cost = kosten(0,M,{})

a = []
i = 0
for k in range(10):
    i = wahl[(i,M-k)]
    a.append(tn[i])
print(cost, a)




 



 

