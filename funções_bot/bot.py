from langchain_core.messages import  SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader


def Bot (memoria,chat):
    comportamento_chat=[SystemMessage("Me trate como se eu fosse seu pai")]
    memoria+=comportamento_chat
    template = ChatPromptTemplate.from_messages (memoria)

    chain = template | chat
    return chain.invoke({}).content

#carregar informações de sites
def informação_de_sites (url_site,memoria):
    loader=WebBaseLoader(
        web_path=url_site,
        show_progress=True
    )

    lista=loader.load()
    info_site=[]

    for doc in lista:
        #adiciono ao vetor uma lista com tudo que eu posso acessar
        content=doc.page_content
        limpeza=content.replace("\n","")
        info_site.append(limpeza)
        # #assim eu fico livre para adicionar apenas aquilo que eu quero
        # print(docs[0].page_content)
        # print(docs[0].metadata)
    memoria +=info_site

