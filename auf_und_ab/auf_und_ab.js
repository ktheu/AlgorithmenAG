
let a = [[6, 27], [14, 19], [21, 53], [31, 42], [33, 38], [46, 62], [51, 59], [57, 96], [65, 85], [68, 80], [70, 76], [92, 98]];
let a1 = [...a].map(([x, y]) => [y, x]);
let leiter = new Map([...a, ...a1]);

function aufUndAb(n) {
    let pos = 0
    let visited = new Set();
    let zaehl = 0

    while (pos != 100 && !visited.has(pos)) {
        visited.add(pos)
        zaehl += 1
        pos = pos + n
        if (pos > 100) {
            pos = 100 - (pos - 100)
        }
        if (leiter.has(pos)) {
            pos = leiter.get(pos)
        }
    }
    
    if (pos === 100) {
        console.log(`Mit ${n} kann Ziel in ${zaehl} Wuerfen erreicht werden`);
    }

    else {
        console.log(`Mit ${n} kann Ziel nicht erreicht werden. ${pos} wird doppelt besucht.`);
    }

}

for (let n=1; n<=6; n++) {
    aufUndAb(n)
}
 







