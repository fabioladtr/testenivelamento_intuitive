import os
import requests
from bs4 import BeautifulSoup

class PDFScraper:
    def __init__(self):
        pass

    def buscar_pdfs(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            print("Erro ao acessar a página!")
            return
        pdf_links=[]
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and href.endswith(".pdf") and "Anexo" in href:
                pdf_links.append(href)
        return pdf_links
    
    def baixar_pdfs(self, pdf_links):
        arquivos_pdfs = []
        pasta_anexos = "anexos"
        os.makedirs(pasta_anexos , exist_ok=True)
        for pdf_url in pdf_links:
            nome_pdf = pdf_url.split("/")[-1]
            caminho_pdf = os.path.join(pasta_anexos, nome_pdf)

            print(f"Baixando {nome_pdf}...")

            response = requests.get(pdf_url)
            if response.status_code == 200:
                with open(caminho_pdf, "wb") as f:
                    f.write(response.content)
                arquivos_pdfs.append(caminho_pdf)        
        return arquivos_pdfs