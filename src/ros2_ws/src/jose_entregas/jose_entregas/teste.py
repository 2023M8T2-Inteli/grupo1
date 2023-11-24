from openai import OpenAI
import re
import dotenv
import os

def msg(content):
    client = OpenAI()
    #openai.api_key = os.getenv('OPENAI_API_KEY')
    # completion = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo", 
    #     messages=[
    #         {"role": "system", "content": "Considere que você é um técnico de almoxarifado especializado em peças mecânicas e funcionamento fabril"},
    #         {"role": "user", "content": f"Preciso que me retorne a posição digitada a frente entre '()': {content}"}
    #     ])
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Considere que você é um técnico de almoxarifado especializado em peças mecânicas e funcionamento fabril"},
        {"role": "user", "content": f"Preciso que me retorne a posição digitada a frente entre '()': {content}"}
    ]
    )

    return completion.choices[0].message


# if __name__ == "__main__":
#     msg('(9,9,9,9)')

# python OneDrive\Documentos\GitHub\Jv_Pessoal\chatbot_LLM\chat_bot\bot.py
