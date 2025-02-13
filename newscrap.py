import requests
from bs4 import BeautifulSoup
import openai
import os
import time
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("AVISO: OPENAI_API_KEY não encontrada no arquivo .env!")
    exit(1)

URL = "https://g1.globo.com/"

def coletar_noticias():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Erro ao acessar o site")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    noticias = []
    
    for item in soup.find_all("a", class_="feed-post-link"):  
        titulo = item.get_text().strip()
        link = item["href"]
        noticias.append({"titulo": titulo, "link": link})
    
    return noticias

def extrair_conteudo(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Erro ao acessar a notícia."
    
    soup = BeautifulSoup(response.text, "html.parser")
    paragrafos = soup.find_all("p")
    texto = " ".join([p.get_text() for p in paragrafos])
    return texto[:2000]  

def resumir_noticia(texto):
    if not texto or texto == "Erro ao acessar a notícia.":
        return "Não foi possível obter o resumo."

    client = openai.OpenAI(api_key=api_key)

    tentativas = 3 
    for tentativa in range(tentativas):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "Resuma o seguinte texto:"}, {"role": "user", "content": texto[:1000]}],  
                max_tokens=100  
            return response.choices[0].message.content.strip()

        except openai.RateLimitError:
            print(f"Limite de requisições excedido. Tentando novamente em 2 minutos... ({tentativa + 1}/{tentativas})")
            time.sleep(120)  
    return "Não foi possível obter o resumo após várias tentativas."


if __name__ == "__main__":
    print("Iniciando o scraper de notícias...")
    noticias = coletar_noticias()
    if not noticias:
        print("Nenhuma notícia encontrada.")
    else:
        for i, noticia in enumerate(noticias[:5]):
            print(f"{i+1}. {noticia['titulo']}")
            print(f"   🔗 {noticia['link']}")

            conteudo = extrair_conteudo(noticia['link'])
            resumo = resumir_noticia(conteudo)

            print(f"   📝 Resumo: {resumo}\n")
            time.sleep(2)
    print("Finalizado.")
