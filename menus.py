from teste import *
from groq import Groq

Iniciar=True
while Iniciar:
    print("Chat Bot Teste")
    print("[1-Adicionar PDF]")
    pergunta=input("Qual A sua Pergunta?")
    
    if (pergunta.lower() == "x"):
        Iniciar=False
    if (pergunta=="1"):
        informacao_pdf(memoria)
    else:
        usuario_pergunta(memoria,pergunta)
        resposta = Bot(memoria,chat)
        print(resposta)


