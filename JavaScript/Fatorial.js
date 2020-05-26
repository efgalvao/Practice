/*
Escreva uma função fatorial, que calcule o fatorial de um número.
*/

function fatorial(n){
    var total = 1
    for(var i = 1; i <= n; i++ ){
        total = i * total
    } return total
}

console.log(fatorial(5))