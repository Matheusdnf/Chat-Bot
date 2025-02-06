from langchain_core.messages import HumanMessage

def usuario_pergunta(memoria,pergunta):
    pergunta_usuario=[HumanMessage(pergunta)]
    memoria+=pergunta_usuario

