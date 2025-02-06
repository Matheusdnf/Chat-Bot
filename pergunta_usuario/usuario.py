from langchain_core.messages import HumanMessage

def usuario_pergunta(memoria):
    pergunta_usuario=[HumanMessage("fale sobre aviões")]

    memoria+=pergunta_usuario

