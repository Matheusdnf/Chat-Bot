from langchain_core.messages import  SystemMessage
from langchain_core.prompts import ChatPromptTemplate

def Bot (memoria,chat):
    comportamento_chat=[SystemMessage("Me trate como se eu fosse seu pai")]
    memoria+=comportamento_chat
    template = ChatPromptTemplate.from_messages (memoria)

    chain = template | chat
    return chain.invoke({}).content