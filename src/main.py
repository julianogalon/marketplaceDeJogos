from data.csv_importador import CSVImportador
from analysis.monetizacao import ModeloMonetizacaoEstatistica
from analysis.ano_lancamento import AnoLancamentoEstatistica
from analysis.plataforma_os import EstatisticaPlataformaOS
from analysis.estatistica_linhas import EstatisticaLinhasCSV

# Execução do Programa Principal para análise estatística:
importador = CSVImportador('../steam_games.csv')
dados = importador.importar()

analiseMonetizacao = ModeloMonetizacaoEstatistica(dados)
analiseMonetizacao.resumo()

analiseLancamentoAno = AnoLancamentoEstatistica(dados)
analiseLancamentoAno.mostrar_anos_mais_lancamentos()

analisePlataformaOS = EstatisticaPlataformaOS(dados)
analisePlataformaOS.resumo()
