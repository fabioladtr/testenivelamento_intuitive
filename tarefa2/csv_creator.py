import os

class CSVCreator:
    def __init__(self):
        pass

    def salvar_em_csv(self, tabela):
        os.makedirs("csv", exist_ok=True)
        csv_path = "csv/tabela.csv"
        # Salvar o DataFrame combinado em um único arquivo CSV
        tabela.to_csv(csv_path, index=False, sep=',', encoding='utf-8')
        print(f"Tabelas combinadas salvas como {csv_path}")
        return csv_path