const net = require('net')

const { Client } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const client = new Client();


client.on('qr', (qr) => {
    qrcode.generate(qr,{small:true})
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.initialize();

client.on('message', message => {
    console.log("MSG: ",message);
    a = async (audio)=>{
        console.log(audio.downloadMedia())
        let media = null
        try {
        media = await audio.downloadMedia()
        console.log("resposta: ",media)
        return media
        } catch (e) {
        console.log(e)
        }
    }

});


// const handleConnection = (conection) =>{
//     console.log(toString(conection))
// }

// const server = net.createServer(handleConnection)
// server.listen(4000,'127.0.0.1')

