#### main.py
# Programa principal para análise estatística de jogos da Steam
# Alterna entre modo produção e teste via argumento de linha de comando

import sys
from data.csv_importador import CSVImportador
from analysis.monetizacao import ModeloMonetizaçãoEstatistica
from analysis.ano_lancamento import AnoLancamentoEstatistica
from analysis.plataforma_os import PlataformaOSEstatistica

def main():
    """
    #### Execução do Programa Principal
    # Analisa percentuais de monetização, ano com mais lançamentos e distribuição por plataforma.
    # Utiliza arquivo diferente para dados de teste se '-teste' estiver em sys.argv.
    #
    # Exemplos de uso:
    #   $ python src/main.py
    #   $ python src/main.py -teste
    """
    # Verifica se foi passado '-teste' como argumento
    if '-teste' in sys.argv:
        arquivo_csv = '/content/steam_games_test.csv'
        print("Executando em modo TESTE")
    else:
        arquivo_csv = '/content/steam_games.csv'
        print("Executando em modo PRODUÇÃO")

    # Importa os dados do arquivo CSV
    importador = CSVImportador(arquivo_csv)
    dados = importador.importar()
    if not dados:
        print("Nenhum dado foi importado. Verifique o arquivo CSV.")
        return

    ### Pergunta 1: Percentual de jogos gratuitos e pagos
    analiseMonetizacao = ModeloMonetizaçãoEstatistica(dados)
    analiseMonetizacao.resumo()
    
    ### Pergunta 2: Ano(s) com mais lançamentos
    analiseLancamentoAno = AnoLancamentoEstatistica(dados)
    analiseLancamentoAno.mostrar_anos_mais_lancamentos()
    
    ### Pergunta 3: Distribuição por plataforma de SO
    analisePlataformaOS = PlataformaOSEstatistica(dados)
    analisePlataformaOS.resumo()

if __name__ == "__main__":
    main()
