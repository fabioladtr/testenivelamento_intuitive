import sys
import os
sys.path.append(os.path.abspath(".."))  # Precisei colocar isso para resolver o import na linha 7

from pdf_extrator import PDFExtractor
from csv_creator import CSVCreator
from tarefa1.compressor import FileCompressor

pdf_extrator = PDFExtractor()
tabela = pdf_extrator.extrair_tabela("../tarefa1/anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf")

csv_creator = CSVCreator()
tabela_path = csv_creator.salvar_em_csv(tabela)

compressor = FileCompressor()
compressor.compactar([tabela_path], "Teste_Fabiola_Dutra.zip")