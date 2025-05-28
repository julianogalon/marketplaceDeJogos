#### AnoLancamentoEstatistica
# Classe para análise do ano com maior número de lançamentos em um conjunto de dados de jogos
from datetime import datetime
from collections import Counter

class AnoLancamentoEstatistica:
    def __init__(self, dados):
        """
        ### Inicializa a classe com a lista de dados (dicionários) dos jogos
        # dados: lista de dicionários, cada um representando um jogo
        """
        self.dados = dados

    def _extrair_ano(self, data_str):
        """
        ### Extrai o ano de uma string de data em diferentes formatos
        # Aceita formatos como 'Jul 19, 2018', '2018-07-19', '2018', etc.
        # Retorna o ano como inteiro ou None se não conseguir extrair.

        Exceções:
        - Caso data_str seja vazia, retorna None.
        - Se nenhum formato for compatível, tenta extrair os últimos 4 dígitos caso sejam números.

        Exemplos (doctest):
        >>> est = AnoLancamentoEstatistica([])
        >>> est._extrair_ano('Jul 19, 2018')
        2018
        >>> est._extrair_ano('2018-07-19')
        2018
        >>> est._extrair_ano('2018')
        2018
        >>> est._extrair_ano('19/07/2018')
        2018
        >>> est._extrair_ano('') is None
        True
        >>> est._extrair_ano(None) is None
        True
        >>> est._extrair_ano('Data desconhecida') is None
        True
        """
        if not data_str or data_str.strip() == "":
            return None
        formatos = [
            "%b %d, %Y",  # Ex: Jul 19, 2018
            "%B %d, %Y",  # Ex: July 19, 2018
            "%Y-%m-%d",   # Ex: 2018-07-19
            "%d/%m/%Y",   # Ex: 19/07/2018
            "%Y",         # Ex: 2018
        ]
        for fmt in formatos:
            try:
                return datetime.strptime(data_str.strip(), fmt).year
            except:
                continue
        # Tenta pegar apenas o ano se o texto terminar em 4 dígitos
        if data_str.strip()[-4:].isdigit():
            return int(data_str.strip()[-4:])
        return None

    def anos_com_mais_lancamentos(self):
        """
        ### Retorna uma lista com o(s) ano(s) com maior número de lançamentos
        # Se não encontrar nenhum ano, retorna lista vazia.

        Exemplos (doctest):
        >>> dados = [
        ...     {'Release date': '2018-07-19'},
        ...     {'Release date': '2018'},
        ...     {'Release date': 'Jul 19, 2017'},
        ...     {'Release date': '2017'},
        ...     {'Release date': '2018-07-19'}
        ... ]
        >>> est = AnoLancamentoEstatistica(dados)
        >>> est.anos_com_mais_lancamentos()
        [2018]
        >>> dados2 = [{'Release date': '2017'}, {'Release date': '2018'}]
        >>> est2 = AnoLancamentoEstatistica(dados2)
        >>> sorted(est2.anos_com_mais_lancamentos())
        [2017, 2018]
        """
        anos = []
        for jogo in self.dados:
            data = jogo.get('Release date', '').strip()
            ano = self._extrair_ano(data)
            if ano:
                anos.append(ano)
        if not anos:
            return []

        contagem = Counter(anos)
        maior = max(contagem.values())
        anos_maximos = [ano for ano, total in contagem.items() if total == maior]
        return anos_maximos

    def mostrar_anos_mais_lancamentos(self):
        """
        ### Exibe o(s) ano(s) com mais lançamentos no formato legível
        # Utiliza anos_com_mais_lancamentos para buscar o(s) ano(s).
        # Se não encontrar anos, informa que não foi possível identificar.

        Exemplo (doctest):
        >>> dados = [{'Release date': '2017'}, {'Release date': '2018'}, {'Release date': '2018'}]
        >>> est = AnoLancamentoEstatistica(dados)
        >>> est.mostrar_anos_mais_lancamentos()
        O ano com mais lançamentos é: 2018
        """
        anos = self.anos_com_mais_lancamentos()
        if not anos:
            print("Não foi possível identificar anos de lançamento nos dados.")
        elif len(anos) == 1:
            print(f"O ano com mais lançamentos é: {anos[0]}")
        else:
            print(f"Os anos com mais lançamentos são: {', '.join(map(str, anos))}")
