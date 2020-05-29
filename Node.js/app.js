/*
var Dog = require('./cachorro');

//console.log(Dog.nome)
//console.log(Dog.idade)
//Dog.latir()

//-----------------------------------------//

var EventEmitter = require('events')

var emmiter = new EventEmitter();

emmiter.on('meu_evento', function(number){;
        console.log('Trying to learn Node.js', number )
});

emmiter.emit('meu_evento', 101)
--------------------------------------------


var EventEmitter = require('events')
class Cao extends EventEmitter{
    latir(){
        console.log('Au Au')}}
    
var Rex = new Cao()

Rex.on('Bell', Rex.latir);
Rex.once('Bell2', Rex.latir);

Rex.emit('Bell')
Rex.emit('Bell2')
Rex.emit('Bell2')
Rex.removeListener('Bell', Rex.latir)
Rex.emit('Bell')
Rex.emit('Bel2l')
*/

var fs = require('fs');

fs.writeFile('myfile.txt', 'Hello World!', function (err) {
        if (err) throw err;
        console.log('Saved!');
      }); 