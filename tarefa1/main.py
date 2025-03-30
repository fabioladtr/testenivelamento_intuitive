from pdf_scraper import PDFScraper
from compressor import FileCompressor

pdf_scraper = PDFScraper()
pdf_links = pdf_scraper.buscar_pdfs("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")

lista = pdf_scraper.baixar_pdfs(pdf_links)
compressor = FileCompressor()
compressor.compactar(lista, "anexos.zip")