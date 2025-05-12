import os
#interação com as ia 
from langchain_groq import ChatGroq



from funções_bot.bot import *
from pergunta_usuario.usuario import usuario_pergunta

memoria=[]

api_key = "chave_api"
os.environ["GROQ_API_KEY"] = api_key
chat = ChatGroq(
    model="llama-3.3-70b-versatile",
    max_retries=3,
    temperature=2
)





