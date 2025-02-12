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
    # Carregar o conteúdo da página com requests
    print(f"Carregando a página: {url_site}")
    response = requests.get(url_site)
    
    # Garantir que a requisição foi bem-sucedida

    # posso adicioanr um bloco try exception -> erro que dará requests.exceptions.HTTPError
    if (response.status_code == 200):
        print(response)
        content = response.text  
        print(content)
        print(f"Conteúdo da página carregado com sucesso.")
    else:
        print(f"Falha ao carregar a página, status code: {response.status_code}")
        # ver oq pode ser melhor nesse caso tenha dado error 
        return []

    # Parse com BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Encontrando as tags <main> e <body>
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

    # Verifica se a tag <main> foi encontrada e processa o texto
    if main_content:
        print("Conteúdo da tag <main> encontrado:")
        info_site.append(clean_text(main_content))  # Extraí o texto limpo da tag <main>
    else:
        print("Tag <main> não encontrada.")

    # Verifica se a tag <body> foi encontrada e processa o texto


    # Adicionando as informações ao vetor 'memoria'
    memoria += info_site

    # Exibir o conteúdo final processado
    print(f"\nConteúdo completo processado (apenas texto limpo):")
    for i, chunk in enumerate(info_site):  # Exibe todo o conteúdo processado
        print(f"Texto Extraído (Chunk {i}):\n{chunk}\n")
    
    return info_site

