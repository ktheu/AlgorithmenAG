let a = [1,2,3,4,5];
n = a.length;
let k = 2;
let b = [...Array(n).keys()].map( (x) => a[(x+k)%n]);
console.log(b)
 