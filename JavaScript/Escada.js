/*
Desafio - Escada

Queremos representar uma escada com altura variável, utilizando um array de strings.

Por exemplo, uma escada com altura 3, representaremos com o seguinte array:

var escada3 = [
 "  #",
 " ##",
 "###"
]

E uma escada com altura 5, da seguinte forma:

var escada5 = [
 "    #",
 "   ##",
 "  ###",
 " ####",
 "#####"
]
*/
function escada(n){
    var escada = []
    var vazio = " "
    var degraus = "#"
    for(var i = 1; i <= n; i++){
        var degrau = (vazio.repeat(n-i)) + (degraus.repeat(i))
        escada.push(degrau)
    }
    return escada
}

console.log(escada2(4))