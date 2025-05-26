class ModeloMonetizaçãoEstatistica:
    def __init__(self, dados):
        self.dados = dados if dados else []

    def percentual_gratuitos(self):
        total = len(self.dados)
        if total == 0:
            return 0.0
        gratuitos = 0
        for jogo in self.dados:
          price = jogo.get('Price', '').strip()
          if price == '' or price == '0.0':
                gratuitos += 1
        return (gratuitos / total) * 100

    def percentual_pagos(self):
        total = len(self.dados)
        if total == 0:
            return 0.0
        pagos = 0
        for jogo in self.dados:
            price = jogo.get('Price', '').strip()
            if price != '' and price != '0.0':
                pagos += 1
        return (pagos / total) * 100

    def resumo(self):
        gratuitos = self.percentual_gratuitos()
        pagos = self.percentual_pagos()
        print(f"Percentual de jogos gratuitos: {gratuitos:.2f}%")
        print(f"Percentual de jogos pagos: {pagos:.2f}%")
