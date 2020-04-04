# tn = [7,10,14,16,18,19,20,24,26,29,30,32]
# M = 5

# tn = [7,10,14,16,18,19]
# M = 3

inf = 10000 

f = open('./beispieldaten/beispiel2.txt')
tn = [int(x.rstrip('\n')) for x in f.readlines()]
tn = [-inf] + sorted(tn)
M = 10

N = len(tn)



def minAbstand(x,a):
    '''minimaler Abstand von x zu einer Zahl in a'''
    return min([abs(x-y) for y in a])


def sumKosten(tn,a):
    '''summe der Kosten für tn wenn a die gewählten Zahlen sind'''
    return sum([minAbstand(x,a) for x in tn])


def abschnitt(i,k):
    ''' kosten des abschnitts i-k, wenn nur i und k gewählt wurden. '''
    tmp = tn[i:k+1]
    return sumKosten(tmp,[tmp[0],tmp[-1]])


def kosten0(k):
    ''' kosten von k bis zum Ende, wenn außer k keine weitere Zahl gewählt wurde '''
    tmp = tn[k:]
    return sumKosten(tmp,[tmp[0]])

# import numpy as np

# a = np.zeros((N,M+1),dtype=int) 

# for i in range(N):
#     a[i,0] = kosten0(i)    

# for m in range(1,M+1):
#     for i in range(N):
#         minKost = inf
#         for k in range(i+1,N):
#             if abschnitt(i,k) + a[k,m-1] < minKost:
#                 minKost = abschnitt(i,k) + a[k,m-1]
#         a[i,m] = minKost

# print(a)

 
def kosten(i,m, memo):
    if m == 0: return kosten0(i)
    if (i,m) in memo: return memo[(i,m)]

    minKost = inf
    for k in range(i+1,N):
        if abschnitt(i,k) + kosten(k,m-1,memo) < minKost:
             minKost = abschnitt(i,k) + kosten(k,m-1,memo)
    memo[(i,m)] = minKost
    return minKost 

print(kosten(0,M,{}))



 

