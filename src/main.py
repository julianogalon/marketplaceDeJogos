import sys
from data.csv_importador import CSVImportador
from analysis.monetizacao import ModeloMonetizaçãoEstatistica
from analysis.ano_lancamento import AnoLancamentoEstatistica
from analysis.plataforma_os import PlataformaOSEstatistica

# Execução do Programa Principal para análise estatística:
def main():
    # Verifica se foi passado '-teste' como argumento
    if '-teste' in sys.argv:
        arquivo_csv = '/content/steam_games_test.csv'
        print("Executando em modo TESTE")
    else:
        arquivo_csv = '/content/steam_games.csv'
        print("Executando em modo PRODUÇÃO")

importador = CSVImportador(arquivo_csv)
dados = importador.importar()

# Pergunta 1
analiseMonetizacao = ModeloMonetizaçãoEstatistica(dados)
analiseMonetizacao.resumo()

# Pergunta 2
analiseLancamentoAno = AnoLancamentoEstatistica(dados)
analiseLancamentoAno.mostrar_anos_mais_lancamentos()

# Pergunta 3
analisePlataformaOS = PlataformaOSEstatistica(dados)
analisePlataformaOS.resumo()

if __name__ == "__main__":
    main()
