from os import environ
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class User_input:
    def __init__(self):
        self.body = input("Digite a mensagem: ")

    def get_body(self):
        return self.body

class Twilio:
    def __init__(self):
        self.account_sid = environ.get("ACCOUNT_SID")
        self.auth_token = environ.get("AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)
    
    def send_whatsapp(self, body, from_, to):
        try:
            message = self.client.messages.create(
                                            body=body,
                                            from_=from_,
                                            to=to
                                            )
            print("Mensagem enviada com sucesso!")
        except Exception as e:
            print("Erro ao enviar mensagem: ", e)

if __name__ == "__main__":
    twilio = Twilio()
    user_input = User_input()
    body = user_input.get_body()
    twilio.send_whatsapp(body=body, from_='whatsapp:+14155238886', to='whatsapp:+553188370651')