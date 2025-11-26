import random
from ambiente import Ambiente


class AmbienteFarol(Ambiente):
    def __init__(self, largura=10, altura=10):
        self.largura = largura
        self.altura = altura
        self.posicao_alvo = (largura - 1, altura - 1)
        self.posicoes_agentes = {}

    def iniciar_agente(self, agente):
        """Coloca o agente no início (0,0)"""
        self.posicoes_agentes[agente.id] = (0, 0)
        agente.posicao = (0, 0)

    def observacao_para(self, agente):
        return self

    def atualizacao(self):
        pass

    def agir(self, accao, agente) -> float:
        x, y = self.posicoes_agentes[agente.id]

        novo_x, novo_y = x, y
        if accao == "Norte":
            novo_y -= 1
        elif accao == "Sul":
            novo_y += 1
        elif accao == "Oeste":
            novo_x -= 1
        elif accao == "Este":
            novo_x += 1

        # Verificar limites
        novo_x = max(0, min(self.largura - 1, novo_x))
        novo_y = max(0, min(self.altura - 1, novo_y))

        # Atualizar estado
        self.posicoes_agentes[agente.id] = (novo_x, novo_y)
        agente.posicao = (novo_x, novo_y)

        # Verificar se chegou ao alvo
        if (novo_x, novo_y) == self.posicao_alvo:
            return 100.0

        return -1.0