/* 
Desafio - Professora Furiosa

Uma professora de programação, cansada de que os estudantes cheguem tarde, decidiu que vai cancelar a aula se há poucos presentes.

Ela representa a entrada dos estudantes como um array de tempos de chegada tarde, em minutos. Por exemplo, se um estudante chegou 10 minutos atrasado, outro 5 minutos antes da hora, outro com 3 minutos de atraso, e outro pontual, poderá representar assim:

var alunosDaSegunda = [10, -5, 3, 0];

Com essa informação e a quantidade mínima de estudantes para que suceda o curso, a professora quer saber se a aula acontecerá. Por exemplo, supondo que a quantidade mínima de estudantes para que a aula aconteça é de 2 alunos, então o curso da segunda-feira se realizará, porque houve um estudante que foi pontual e um estudante que chegou cedo.

Escreva as seguintes funções: 1. acontece, que diz se a aula sucederá de acordo com o array dos estudantes que entraram. 2. aberturas, que utiliza um array com os arrays dos estudantes que entraram nos outros dias, e a quantidade mínima de estudantes, e diga quais os dias em que as aulas aconteceram e quais não.
*/

function acontece(dia, quantidade){
    var total = 0
    for(i = 0; i < dia.length ; i++){
        if(dia[i] <= 0 ){
            total += 1
        }
    } 
    return total >= quantidade
}

function aberturas(dias, quantidade){
    var aconteceu = []
    for(var i = 0; i < dias.length; i++){
        aconteceu.push(acontece(dias[i], quantidade))
    }
    return aconteceu
}


var a = [10, -5, 3, 0];
var b = [10, 5, 3, 0];
var c = [10, -5, 3, 0];
var d = [10, -2, 3, 0];
var e = [10, -4, 3, 0];
var f = [10, 6, 3, 0];

var li = [a, b, c, d, e, f]

console.log(aberturas(li, 2))
// console.log(acontece(a, 2))