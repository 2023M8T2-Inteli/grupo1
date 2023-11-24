from datetime import datetime

log = {
    0: {'user-prompt': 'example'},
    1: {'system-response': 'example'},
}

#Setar a data e hora atual como chave dentro das chaves de 'respostas do sistema e prompts do usuario'

#def getDateTime():
#    now = datetime.now
#
#    dd-mm-yy H:M:S
#    dt_string = '{}/{}/{}'.format(now.day, now.month, now.year)
#    return str(dt_string)

def getUserPrompt(prompt):
    return print(prompt)


def getSysResponse(response):
    count = len(log)
    updateLog = {
        count: {
            'system-response': response
        }
    }
    log.update(updateLog)
    return log
