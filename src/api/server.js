const net = require('net')

const { Client, LocalAuth  } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const client = new Client({
    authStrategy: new LocalAuth(
        {
            clientId:"jv"
        }
    )
});
 



client.on('qr', (qr) => {
    qrcode.generate(qr,{small:true})
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.initialize();

client.on('message', async msg => {
    if(msg.hasMedia) {
        const media = await msg.downloadMedia();
        console.log(media)
    }
    else{
        message.reply('Oi eu sou o jose entregas!');
    }

});
 

// Supondo que você tenha o objeto MessageMedia

  

// const handleConnection = (conection) =>{
//     console.log(toString(conection))
// }

// const server = net.createServer(handleConnection)
// server.listen(4000,'127.0.0.1')

