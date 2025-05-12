#busca padrões em string
import re
from groq import APIStatusError
#retornar o error da api
from langchain_core.messages import  SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader

def Bot (memoria,chat):
    comportamento_chat=[SystemMessage("Você é um agente ia que irá responder dúvidas sobre o curso de bsi, seja o mais formal,e só responda as perguntas baseadas no pdf carregado, não busque na sua base de dados")]
    memoria+=comportamento_chat
    template = ChatPromptTemplate.from_messages (memoria)
    chain = template | chat

    try:
        return chain.invoke({}).content
    except APIStatusError as e:
        # a partir do nome requested busca todos os números a sua frente
        match = re.search(r'Requested (\d+)', str(e))
        if match:
            #group acessa uma parte específica do texto
            requested_value = int(match.group(1))  # Converte para inteiro
            if (requested_value > 6000):
                print("Não será possível fazer a requizição disso")
        else:
            print("Não foi possível encontrar o valor de Requested.")



def informacao_pdf(memoria):
    caminho = "./pdfs/"
    

    loader = PyPDFDirectoryLoader(path=caminho)
    conteudo_pdf = loader.load()
    print(conteudo_pdf)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=9000, chunk_overlap=0)
    
    load_pdf = []

    for doc in conteudo_pdf:
        chunks = text_splitter.split_text(doc.page_content)
        load_pdf.extend(chunks)

    memoria.extend(load_pdf)
