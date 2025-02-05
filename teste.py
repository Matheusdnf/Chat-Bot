import os
#interação com as ia 
from langchain_groq import ChatGroq

api_key = "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"
os.environ["GROQ_API_KEY"] = api_key  

chat = ChatGroq(model="llama-3.3-70b-versatile")

resposta = chat.invoke("Voce fala portugues?")
print(resposta.content)

# x= input("Alguma coisa:")
# while (x != "x"):
#     print("oi")
#     x=input("Continuar?:")

