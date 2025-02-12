#busca padrões em string
import re
from groq import APIStatusError
#retornar o error da api
from langchain_core.messages import  SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
import requests
from bs4 import BeautifulSoup


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



def informação_de_sites(url_site, memoria):
    print(f"Carregando a página: {url_site}")
    response = requests.get(url_site)
    
    # posso adicioanr um bloco try exception -> erro que dará requests.exceptions.HTTPError
    try:
        if (response.status_code == 200):
            print(response)
            content = response.text  
            print(content)
            print("Acesso a informação conseguida com sucesso.")
    except requests.exceptions.HTTPError as e:
            print("Erro na requizição {e}")
    finally:
        print("Falha ao fazer o carregamento da página")

    # Parse com BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Encontrando as tags <main> 
    main_content = soup.find('main')  # Busca a tag <main>

    # Lista para armazenar o conteúdo extraído
    info_site = []

    # Função para limpar e extrair texto
    def clean_text(tag):
        # Remover as tags de imagem, vídeo, link, estilização e script
        for unwanted_tag in tag.find_all(['img', 'video', 'a', 'style', 'script','footer']):
            unwanted_tag.decompose()  # Remove a tag indesejada

        # Remover atributos como 'class' e 'id' para não extrair estilização
        for element in tag.find_all(True):  # True significa todas as tags
            del element['class']
            del element['id']

        # Extrair e retornar o texto limpo
        return tag.get_text(separator=" ", strip=True)

    if main_content:
        print("Conteúdo da tag <main> encontrado:")
        info_site.append(clean_text(main_content))  # Extraí o texto limpo da tag <main>
    else:
        print("Tag <main> não encontrada.")


    memoria += info_site

    # print(f"\nConteúdo completo processado (apenas texto limpo):")
    # for i, chunk in enumerate(info_site):  # Exibe todo o conteúdo processado
    #     print(f"Texto Extraído (Chunk {i}):\n{chunk}\n")

