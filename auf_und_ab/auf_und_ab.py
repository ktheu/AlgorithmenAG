
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
        print('Mit {} kann Ziel in {} Wuerfen erreicht werden.'.format(n,zaehl))
      
    else:
        print('Mit {} kann Ziel nicht erreicht werden. {} wird doppelt besucht.'.format(n,pos))
 
for n in range(1,7):
    aufUndAb(n)







