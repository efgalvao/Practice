/*
Desafio - Produto

Necessitamos uma função produto que receba um array de números e retorne o produto: o resultado de multiplicar todos os elementos entre si.

Por exemplo, produto([1, 4, 7]) deve retornar 28, que é 1 * 4 * 7.
*/
function produto(lista){
    var total = 1
    for(i = 0; i < lista.length; i++){
        total = total * lista[i]
    }
    return total
}

