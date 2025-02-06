import os
#interação com as ia 
from langchain_groq import ChatGroq

from funções_bot.bot import Bot
from pergunta_usuario.usuario import usuario_pergunta

memoria=[]

api_key = "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"
os.environ["GROQ_API_KEY"] = api_key
chat = ChatGroq(model="llama-3.3-70b-versatile")





