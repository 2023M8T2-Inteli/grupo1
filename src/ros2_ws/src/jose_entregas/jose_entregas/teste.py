import openai
import re
import dotenv
import os



content = "A equipe de operação de um forno industrial relata variações significativas nas temperaturas durante os ciclos de produção. Em alguns casos, o forno atinge temperaturas superiores ou inferiores às configurações programadas, resultando em produtos finais com características indesejadas. Não há indícios visuais de danos externos no sistema de aquecimento."


def main():
    openai.api_key = os.getenv('OPENAI_API_KEY')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou outro modelo
    messages=[
        {"role": "system", "content": "Considere que você é um técnico de almoxarifado especializado em peças mecânicas e funcionamento fabril"},
        {"role": "user", "content": f"Preciso que para cada problema relacionado ao mundo fabril você me forneça uma solução de que peça estou precisando para solucionar de forma breve, curta e em todos as suas respostas a palavra 'essa peça' deve estar antes da peça que você me recomendar. {content}"}
    ])

    print(completion.choices[0].message)


if __name__ == "__main__":
    main()

# python OneDrive\Documentos\GitHub\Jv_Pessoal\chatbot_LLM\chat_bot\bot.py

