#### CSVImportador
# Classe para importar dados de arquivos CSV utilizando DictReader do módulo csv

import csv

class CSVImportador:
    def __init__(self, nome_arquivo):
        """
        ### Inicializa a classe com o nome do arquivo CSV a ser importado
        # nome_arquivo: string com o caminho do arquivo CSV
        """
        self.nome_arquivo = nome_arquivo
        self.dados = []

    def importar(self):
        """
        ### Importa os dados do arquivo CSV para uma lista de dicionários
        # Retorna a lista de dicionários com os dados importados.
        # Em caso de erro de arquivo não encontrado, imprime mensagem e retorna None.
        # Em caso de outra exceção, imprime a mensagem do erro e retorna None.

        Exemplo (doctest):
        >>> import os
        >>> arquivo_exemplo = 'exemplo.csv'
        >>> with open(arquivo_exemplo, 'w', encoding='utf-8') as f:
        ...     _ = f.write('Nome,Idade\\nJoao,30\\nMaria,25\\n')
        >>> imp = CSVImportador(arquivo_exemplo)
        >>> dados = imp.importar()
        >>> isinstance(dados, list)
        True
        >>> dados[0]['Nome']
        'Joao'
        >>> os.remove(arquivo_exemplo)
        """
        try:
            with open(self.nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.DictReader(arquivo_csv)
                self.dados = [linha for linha in leitor_csv]
            return self.dados
        except FileNotFoundError:
            # Exceção específica para arquivo não encontrado
            print(f"Erro: O arquivo '{self.nome_arquivo}' não foi encontrado.")
            return None
        except Exception as e:
            # Outras exceções ao tentar ler o arquivo CSV
            print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")
            return None
