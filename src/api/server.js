const net = require('net')


const handleConnection = (conection) =>{
    console.log(toString(conection))
}

const server = net.createServer(handleConnection)
server.listen(4000,'127.0.0.1')