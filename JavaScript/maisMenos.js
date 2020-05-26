/*
Desafio - Mais Menos

Necessitamos uma função maisMenos que receba um array e retorne outro com os seguintes três números:

    na primeira posição, a fração de números que são positivos
    na segunda posição, a fração de números que são zero
    na última posição, a fração de números que são negativos

Por exemplo, maisMenos([1, 2, 0, -1]) deveria retornar [0.5, 0.25, 0.25], devido a que há 50% de positivos, 25% de zeros, e 25% de negativos.
*/

function maisMenos(lista){
    var positivos = 0
    var zeros = 0
    var negativos = 0
    var resultado = []
    for(var i = 0; i < lista.length; i++){
        if(lista[i] > 0){
            positivos += 1
        } else if(lista[i] < 0){
            negativos += 1
        } else {zeros += 1}
    }
    resultado.push(positivos/lista.length);
    resultado.push(zeros/lista.length);
    resultado.push(negativos/lista.length)
    return resultado
}


var a = [1,2,3,4,0,0,-1,-2]
console.log(maisMenos(a))