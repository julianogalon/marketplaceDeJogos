from datetime import datetime
from collections import Counter

class AnoLancamentoEstatistica:
    def __init__(self, dados):
        self.dados = dados

    def _extrair_ano(self, data_str):
        """
        Tenta converter a data para datetime e extrair o ano.
        Aceita formatos como 'Jul 19, 2018', '2018-07-19', '2018', etc.
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
        anos = self.anos_com_mais_lancamentos()
        if not anos:
            print("Não foi possível identificar anos de lançamento nos dados.")
        elif len(anos) == 1:
            print(f"O ano com mais lançamentos é: {anos[0]}")
        else:
            print(f"Os anos com mais lançamentos são: {', '.join(map(str, anos))}")
