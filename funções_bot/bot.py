#busca padrões em string
import re
from groq import APIStatusError
#retornar o error da api
from langchain_core.messages import  SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def Bot (memoria,chat):
    comportamento_chat=[SystemMessage("Me trate como se eu fosse seu pai")]
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

#carregar informações de sites
def informação_de_sites (url_site,memoria):
    loader=WebBaseLoader(
        web_path=url_site,
        show_progress=True
    )

    splitter = RecursiveCharacterTextSplitter(
    chunk_size=6000,
    chunk_overlap=0,
)
    lista=loader.load()
    info_site=[]
    
    for doc in lista:
        #adiciono ao vetor uma lista com tudo que eu posso acessar
        content=doc.page_content
        limpeza=content.replace("\n","")
        chucks=splitter.split_text(limpeza)
        for chunk in chucks:
            info_site.append(chunk)

        # #assim eu fico livre para adicionar apenas aquilo que eu quero
        # print(docs[0].page_content)
        # print(docs[0].metadata)
    memoria +=info_site
