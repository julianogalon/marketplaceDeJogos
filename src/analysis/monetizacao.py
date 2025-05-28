#### ModeloMonetizaçãoEstatistica
# Classe para análise de monetização de jogos (percentual de gratuitos e pagos)

class ModeloMonetizaçãoEstatistica:
    def __init__(self, dados):
        """
        ### Inicializa a classe com a lista de dados dos jogos
        # dados: lista de dicionários, cada um representando um jogo
        """
        self.dados = dados if dados else []

    def percentual_gratuitos(self):
        """
        ### Calcula o percentual de jogos gratuitos na base de dados
        # Considera gratuito se 'Price' é '' ou '0.0'.
        # Retorna 0.0 se a lista está vazia.

        Exemplo (doctest):
        >>> dados = [{'Price': '0.0'}, {'Price': '10.0'}, {'Price': ''}]
        >>> estat = ModeloMonetizaçãoEstatistica(dados)
        >>> round(estat.percentual_gratuitos(), 2)
        66.67
        """
        total = len(self.dados)
        if total == 0:
            return 0.0  # Evita divisão por zero
        gratuitos = 0
        for jogo in self.dados:
            price = jogo.get('Price', '').strip()
            if price == '' or price == '0.0':
                gratuitos += 1
        return (gratuitos / total) * 100

    def percentual_pagos(self):
        """
        ### Calcula o percentual de jogos pagos na base de dados
        # Considera pago se 'Price' diferente de '' e diferente de '0.0'.
        # Retorna 0.0 se a lista está vazia.

        Exemplo (doctest):
        >>> dados = [{'Price': '0.0'}, {'Price': '10.0'}, {'Price': ''}]
        >>> estat = ModeloMonetizaçãoEstatistica(dados)
        >>> round(estat.percentual_pagos(), 2)
        33.33
        """
        total = len(self.dados)
        if total == 0:
            return 0.0  # Evita divisão por zero
        pagos = 0
        for jogo in self.dados:
            price = jogo.get('Price', '').strip()
            if price != '' and price != '0.0':
                pagos += 1
        return (pagos / total) * 100

    def resumo(self):
        """
        ### Exibe o percentual de jogos gratuitos e pagos
        # Imprime os valores calculados em percentual.
        # Usa os métodos percentual_gratuitos e percentual_pagos.

        Exemplo (doctest):
        >>> dados = [{'Price': '0.0'}, {'Price': '10.0'}, {'Price': ''}]
        >>> estat = ModeloMonetizaçãoEstatistica(dados)
        >>> estat.resumo()
        Percentual de jogos gratuitos: 66.67%
        Percentual de jogos pagos: 33.33%
        """
        gratuitos = self.percentual_gratuitos()
        pagos = self.percentual_pagos()
        print(f"Percentual de jogos gratuitos: {gratuitos:.2f}%")
        print(f"Percentual de jogos pagos: {pagos:.2f}%")
