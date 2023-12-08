from os import environ
from dotenv import load_dotenv
from twilio.rest import Client
from openai import OpenAI

load_dotenv()

cliente = OpenAI(api_key=environ.get("OPENAI_API_KEY"))

completion = cliente.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Você é um bot que somente fala sim ou não."},
    {"role": "user", "content": "Diga sim ou não."},
  ]
)

body = completion.choices[0].message.content

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
    twilio.send_whatsapp(body=body, from_='whatsapp:'+ environ.get('FROM_NUMBER'), to='whatsapp:'+ environ.get('TO_NUMBER'))