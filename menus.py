from teste import *
Iniciar=True
while Iniciar:
    print("Chat Bot Teste")
    pergunta=input("Qual A sua Pergunta?")
    if (pergunta.lower() == "x"):
        Iniciar=False
    else:
        usuario_pergunta(memoria,pergunta)
        resposta = Bot(memoria,chat)
        print(resposta)


