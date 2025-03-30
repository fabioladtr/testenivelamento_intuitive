from tabula import read_pdf
import pandas as pd

class PDFExtractor:
    def __init__(self):
        pass

    def extrair_tabela(self, caminho_pdf):
        tabelas = read_pdf(caminho_pdf, pages='3-181', multiple_tables=True, lattice=True)
        print(f"Tabelas encontradas: {len(tabelas)}")        
        # Combinar todas as tabelas em um único DataFrame
        tabela = pd.concat(tabelas, ignore_index=True)    
        # Limpar e ajustar o DataFrame combinado
        tabela = tabela.dropna(how='all')  # Remove linhas completamente vazias
        tabela.columns = [col.strip() for col in tabela.columns]  # Remove espaços nos nomes das colunas
        return tabela