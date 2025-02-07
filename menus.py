from teste import *
from groq import Groq
Iniciar=True
while Iniciar:
    print("Chat Bot Teste")
    print("[1-Adicionar Informação de Site]")
    pergunta=input("Qual A sua Pergunta?")
    if (pergunta.lower() == "x"):
        Iniciar=False
    if (pergunta == "1"):
        url_site=input("Qual link de site deseja adicionar a infomação?")
        informação_de_sites(url_site,memoria)
        print("Informação adicionada, agr faça uma pergunta sobre o que foi adicionado")
        #print(memoria)

    else:
        usuario_pergunta(memoria,pergunta)
        resposta = Bot(memoria,chat)
        print(resposta)


