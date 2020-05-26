/*
Queremos escrever uma função naipeDeTruco, que dado um naipe, devolva uma lista de strings, uma por cada carta desse naipe seguindo as cartas do truco:

 naipeDeTruco("espadas")
["1 de espadas", "2 de espadas", "3 de espadas" ..., "12 de espadas"]

Lembre-se que as cartas de truco incluem todas as cartas numeradas de 1 a 12, com exceção das cartas 8 e 9

*/


function naipeDeTruco(naipe){
    var lista = []
    for( var i = 1; i < 13; i++){
        var n = i
        if(n !== 8 && n !== 9){
        var carta = i + " de " + naipe
           lista.push(carta)
    }
}
    return lista
}
    
console.log(naipeDeTruco("ouro"))
console.log(naipeDeTruco("espadas"))
console.log(naipeDeTruco("copas"))
console.log(naipeDeTruco("Paus"))
