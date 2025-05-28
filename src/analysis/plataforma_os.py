#### PlataformaOSEstatistica
# Classe para análise da distribuição de jogos em diferentes plataformas de sistema operacional

class PlataformaOSEstatistica:
    def __init__(self, dados):
        """
        ### Inicializa a classe com a lista de dados dos jogos
        # dados: lista de dicionários, cada um representando um jogo
        """
        self.dados = dados if dados else []

    def _disponivel(self, valor):
        """
        ### Verifica se o valor indica disponibilidade para uma plataforma
        # Considera apenas o valor 'True' (string, case-insensitive) como disponível.
        # Retorna True se disponível, False caso contrário.

        Exemplo (doctest):
        >>> est = PlataformaOSEstatistica([])
        >>> est._disponivel('True')
        True
        >>> est._disponivel('false')
        False
        >>> est._disponivel('')
        False
        >>> est._disponivel(None)
        False
        """
        return valor.strip().lower() == "true" if valor else False

    def resumo(self):
        """
        ### Imprime resumo da distribuição de jogos por plataforma (Windows, Mac, Linux, Outras Plataformas)
        # Calcula quantidade e percentual de jogos disponíveis para cada plataforma.
        # 'Outras Plataformas' inclui jogos que não estão em nenhuma das três principais.

        Exemplo (doctest):
        >>> dados = [
        ...   {'Windows': 'True', 'Mac': '', 'Linux': ''},
        ...   {'Windows': '', 'Mac': 'True', 'Linux': ''},
        ...   {'Windows': '', 'Mac': '', 'Linux': ''}]
        >>> est = PlataformaOSEstatistica(dados)
        >>> est.resumo()
        Windows: 1 jogos (33.33%) disponíveis.
        Mac: 1 jogos (33.33%) disponíveis.
        Linux: 0 jogos (0.00%) disponíveis.
        Outras Plataformas: 1 jogos (33.33%) disponíveis.
        """
        total = len(self.dados)
        if total == 0:
            print("Não há dados para analisar.")
            return

        plataformas = {"Windows": 0, "Mac": 0, "Linux": 0, "Outras Plataformas": 0}
        for jogo in self.dados:
            # Para cada plataforma, verifica se está disponível
            disponiveis = {
                os: self._disponivel(jogo.get(os, ""))
                for os in ["Windows", "Mac", "Linux"]
            }
            # Se ao menos uma plataforma principal disponível, soma
            if any(disponiveis.values()):
                for os, disponivel in disponiveis.items():
                    if disponivel:
                        plataformas[os] += 1
            else:
                # Caso não esteja disponível em nenhuma das três, conta como "Outras Plataformas"
                plataformas["Outras Plataformas"] += 1

        for os, quantidade in plataformas.items():
            percentual = (quantidade / total) * 100 if total else 0
            print(f"{os}: {quantidade} jogos ({percentual:.2f}%) disponíveis.")

    def obter_resultados(self):
        """
        ### Retorna um dicionário com a contagem e percentual de jogos por plataforma
        # Útil para uso programático.

        Exemplo (doctest):
        >>> dados = [
        ...   {'Windows': 'True', 'Mac': '', 'Linux': ''},
        ...   {'Windows': '', 'Mac': 'True', 'Linux': ''},
        ...   {'Windows': '', 'Mac': '', 'Linux': ''}]
        >>> est = PlataformaOSEstatistica(dados)
        >>> r = est.obter_resultados()
        >>> r['Windows']['quantidade']
        1
        >>> round(r['Mac']['percentual'], 2)
        33.33
        >>> r['Outras Plataformas']['quantidade']
        1
        """
        total = len(self.dados)
        plataformas = {"Windows": 0, "Mac": 0, "Linux": 0, "Outras Plataformas": 0}
        for jogo in self.dados:
            disponiveis = {
                os: self._disponivel(jogo.get(os, ""))
                for os in ["Windows", "Mac", "Linux"]
            }
            if any(disponiveis.values()):
                for os, disponivel in disponiveis.items():
                    if disponivel:
                        plataformas[os] += 1
            else:
                plataformas["Outras Plataformas"] += 1

        resultados = {}
        for os, quantidade in plataformas.items():
            percentual = (quantidade / total) * 100 if total else 0
            resultados[os] = {"quantidade": quantidade, "percentual": percentual}
        return resultados
