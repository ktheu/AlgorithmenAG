const fs = require('fs');
let f = fs.readFileSync('./beispieldaten/baywatch1.txt', 'utf-8');

let input = f.split('\r\n');
let georg = input[0].split(' ')
let karte = input[1].split(' ')


function schieb(a, k) {
    /*
     a: Liste,
     k: schiebeZahl, 0 <= k < len(a)
     returns: Liste, um k verschoben, d.h. die vorderen k Elemente wurden 
         nacheinander nach hinten versetzt.
    */
    let n = a.length;
    return [...Array(n).keys()].map((x) => a[(x + k) % n]);
}


function passt(a, b) {
    /*
    a: Liste mit Fragezeichen an manchen Stellen, b: Liste
    returns True, falls a gleich b an allen nicht-Fragezeichen Stellen
    */
    for (let i = 0; i < a.length; i++) {
        if (a[i] != '?' && a[i] != b[i]) return false;
    }
    return true;
}

for (let k = 0; k < karte.length; k++) {
    if (passt(karte, schieb(georg, k))) {
        console.log('Verschiebung', k)
        console.log(schieb(georg,k).join(' '))
    }
}
