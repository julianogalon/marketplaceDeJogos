import csv

class CSVImportador:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.dados = []

    def importar(self):
        try:
            with open(self.nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.DictReader(arquivo_csv)
                self.dados = [linha for linha in leitor_csv]
            return self.dados
        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.nome_arquivo}' não foi encontrado.")
            return None
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")
            return None
