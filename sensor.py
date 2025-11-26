from abc import ABC, abstractmethod
import math


class Sensor(ABC):
    @abstractmethod
    def ler(self, agente, ambiente):
        """
        Lê o estado do ambiente do ponto de vista do agente.
        Retorna: Um dado processado (ex: uma matriz local, um vetor direção).
        """
        pass


# --- Sensor para o Problema do Farol (Direção) ---
class SensorDirecao(Sensor):
    """
    Retorna um vetor normalizado (dx, dy) indicando a direção do alvo (Farol).
    Conforme especificado no enunciado: "observam apenas a direção"[cite: 39].
    """

    def ler(self, agente, ambiente):
        pos_agente = agente.posicao  # (x, y)
        pos_alvo = ambiente.posicao_alvo  # O ambiente deve expor onde está o farol

        dx = pos_alvo[0] - pos_agente[0]
        dy = pos_alvo[1] - pos_agente[1]

        # Normalizar (retornar apenas a direção)
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        if distancia == 0:
            return (0, 0)
        return (dx / distancia, dy / distancia)


# --- Sensor para o Problema da Recoleção (Visão Local) ---
class SensorVisaoLocal(Sensor):
    """
    Retorna uma sub-grelha em redor do agente (ex: 3x3 ou 5x5).
    Responde à questão de design: "campo de visão limitado"[cite: 103].
    """

    def __init__(self, raio=1):
        self.raio = raio  # raio=1 dá uma grelha 3x3

    def ler(self, agente, ambiente):
        x, y = agente.posicao
        grelha_completa = ambiente.grelha  # O ambiente expõe a grelha (leitura)

        # Logica simples para extrair o quadrado à volta do agente
        # (Nota: Precisas de tratar limites do mapa na implementação final)
        x_min = max(0, x - self.raio)
        x_max = min(len(grelha_completa), x + self.raio + 1)
        y_min = max(0, y - self.raio)
        y_max = min(len(grelha_completa[0]), y + self.raio + 1)

        visao_local = []
        for i in range(x_min, x_max):
            linha = grelha_completa[i][y_min:y_max]
            visao_local.append(linha)

        return visao_local