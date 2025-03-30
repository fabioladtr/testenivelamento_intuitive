import os
import zipfile

class FileCompressor:
    def __init__(self):
        pass

    def compactar(self, arquivos, nome_zip):
        with zipfile.ZipFile(nome_zip, "w") as zipf:
            for arquivo in arquivos:
                zipf.write(arquivo, os.path.basename(arquivo))
        print(f"Arquivos compactados em {nome_zip}")
