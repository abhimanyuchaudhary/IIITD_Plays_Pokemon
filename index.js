const fs = require('fs');
var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var port = process.env.PORT || 3000;
var msg = ' ';
app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
    fs.appendFile('file.txt', msg, (err) => {  
        if (err) throw err;
        console.log('Message saved!');
    });
  });
  
});

http.listen(3000, '0.0.0.0', function(){
  console.log('listening on *:' + port);
});
