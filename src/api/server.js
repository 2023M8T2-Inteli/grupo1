const net = require('net')
const crypto = require('crypto');
const { Client, LocalAuth  } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const client = new Client({
    authStrategy: new LocalAuth(
        {
            clientId:"pedro"
        }
    )
});


var users = {
    
}


function namefind(numero){
    if (users[numero]){
        console.log("User cadastrado ----> ", users[numero])
        return true
    }

}

var cadastrado ={

}


function validacao(numero){
    if (cadastrado[numero]){
        console.log("User cadastrado ----> ", users[numero])
        return false
    }
    else{
        cadastrado[numero] = "Em cadastro"
        return true
    }

}



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
        
    }
    else{
        //msg.reply('Oi eu sou o jose entregas!');
        if (msg.body){
            if (namefind(msg.from)){
                if (cadastrado[msg.from] == "Em cadastro" || cadastrado[msg.from] == "Pedido finalizado"){
                    msg.reply(`Olá ${users[msg.from]}, em que posso ajudar?`);
                    cadastrado[msg.from] = "Em uso"
                }else{
                    
                }
                
            }else{
                if (validacao(msg.from)){
                    console.log("Me envie seu nome completo:")
                    client.sendMessage(msg.from,"Me envie seu nome completo:");
                }
                else{
                    users[msg.from] = msg.body
                    client.sendMessage(msg.from,'Cadastro realizado com sucesso! Gostaria de realizar um pedido?');
                   

                }
            }
                
           
            console.log(msg.body);
            //console.log(msg)
            
        }
    }

});
 

// Supondo que você tenha o objeto MessageMedia

  

// const handleConnection = (conection) =>{
//     console.log(toString(conection))
// }

// const server = net.createServer(handleConnection)
// server.listen(4000,'127.0.0.1')

