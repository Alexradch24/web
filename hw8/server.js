const http = require('http')
const ws = require('ws')


const wss = new ws.WebSocketServer({ port: 3000 });

wss.on('connection', function connection(ws) {
    console.log('Соединено');
    ws.send('Подключено');

ws.on('message', function incoming(message) {
    console.log(`Получено сообщение: ${message}`);
  });

ws.on('error', function error(error){
    console.log(`Ошибка: ${error}`);
});

  ws.on('close', function close() {
    console.log('Соединение закрыто');
  });
});