const net = require('net');
const path = require('path');

const request = '{"method": "floor", "params": [3.14], "param_types": ["int"], "id": 1}';

const SERVER_PATH = path.join(__dirname, 'socket_file');

const client = net.createConnection(SERVER_PATH, () => {
    console.log('Connected to server');
    client.write(request);
});

client.on('data', (data) => {
    console.log('Received: ', data.toString());
    client.end();
});

client.on('end', () => {
    console.log('Disconnected from server');
});