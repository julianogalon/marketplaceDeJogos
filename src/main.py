from data.csv_importador import CSVImportador
from analysis.monetizacao import ModeloMonetizaçãoEstatistica
from analysis.ano_lancamento import AnoLancamentoEstatistica
from analysis.plataforma_os import PlataformaOSEstatistica

# Execução do Programa Principal para análise estatística:
importador = CSVImportador('/content/steam_games.csv')
#importador = CSVImportador('/content/steam_games_test.csv')
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
