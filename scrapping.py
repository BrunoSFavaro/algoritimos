import requests
from bs4 import BeautifulSoup

# URL da página a extrair os textos
url = 'https://istqb-glossary.page/pt/' 

# Requisição para a página
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parsear o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos os links que contêm os títulos dos artigos (title is-size-5)
    titulos = soup.find_all('a', class_='title is-size-5')

    # Imprimir os títulos extraídos
    for titulo in titulos:
        print(titulo.get_text())
else:
    print(f'Erro ao acessar a página. Status code: {response.status_code}')
