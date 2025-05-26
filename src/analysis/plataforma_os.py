class PlataformaOSEstatistica:
    def __init__(self, dados):
        self.dados = dados if dados else []

    def _disponivel(self, valor):
        # Considera apenas 'True' (string) como disponível
        return valor.strip().lower() == "true" if valor else False

    def resumo(self):
        total = len(self.dados)
        if total == 0:
            print("Não há dados para analisar.")
            return

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

        for os, quantidade in plataformas.items():
            percentual = (quantidade / total) * 100 if total else 0
            print(f"{os}: {quantidade} jogos ({percentual:.2f}%) disponíveis.")

    def obter_resultados(self):
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
