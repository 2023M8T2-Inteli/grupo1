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
 

var intent_dict = {
    "\\b^([Qq]uero|[Pp]reciso|[Ee]stou|[Oo]nde encontro|[Pp]rocuro)\\s+[a-zA-Z\\s]+\\s(.+)$": "control",
    "\\b[Vv][áa](?:\\spara)?\\s?[oa]?\\s(.+)": "go_to",
    "\\b[Mm]e\\sleve até\\s?[oa]?\\s(.+)": "go_to"
};


client.on('qr', (qr) => {
    qrcode.generate(qr,{small:true})
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.initialize();

client.on('message_create', async msg => {
    if(msg.hasMedia) {
        const media = await msg.downloadMedia();
        
    }
    else{
        //msg.reply('Oi eu sou o jose entregas!');
        if (msg.fromMe)
        {try {
            console.log(intent_dict[msg.body])
        } catch (error) {
            console.log("Ação não encontrada")
        }}
    }

});
 

// Supondo que você tenha o objeto MessageMedia

  

// const handleConnection = (conection) =>{
//     console.log(toString(conection))
// }

// const server = net.createServer(handleConnection)
// server.listen(4000,'127.0.0.1')

