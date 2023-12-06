const userService = require("../services/user.service")

var users = {
    
}


var cadastrado = {

}

const namefind = (numero) => {
    if (users[numero]){
        console.log("User cadastrado ----> ", users[numero])
        return true
    }
    return  false

}

const validacao = (numero) => {
    if (cadastrado[numero]){
        console.log("User cadastrado")
        return false
    }
    else{
        cadastrado[numero] = "Em cadastro"
        return true
    }

}

const manager = async (msg, client) =>{
    try {
        if (msg.hasMedia) {
            const media = await msg.downloadMedia();
            const dataBase64 = media.data
            //client.sendMessage(msg.from,'Media Detectada');
            console.log("Midia verificada")
            
            
            // console.log(media)
            // console.log(dataBase64)
            // userService.require_iten(dataBase64,users)
            // userService.create(dataBase64.toString(), users)
            userService.sendBase64(msg, media, users, cadastrado)
            return //console.log(dataBase64.toString())
        }

        if (namefind(msg.from)){
            userService.require_iten(msg,client,users, cadastrado);
            
        }else{
            if (validacao(msg.from)){
                console.log("Acabo de ver que você não está cadastrado na minha base, me envie seu nome completo:")
                //client.sendMessage(msg.from,"Me envie seu nome completo:");
            }
            else{
                cadastrado[msg.from] == "Em cadastro"
                userService.create(msg,users); // Tirar o users depois
                //client.sendMessage(msg.from,'Cadastro realizado com sucesso! Gostaria de realizar um pedido?');
                console.log('Cadastro realizado com sucesso! Gostaria de realizar um pedido?')
            }
        }

      } catch (error) {
        return console.log(error)  //client.sendMessage(msg.from,'Houve um erro ao processar sua requisição');
      }

}

module.exports = {
    manager

};