from abc import ABC, abstractmethod


class Agente(ABC):
    def __init__(self, id_agente):
        self.id = id_agente
        self.sensores = []
        self.modo_aprendizagem = True
        self.percepcao_atual = None  # Guardar o que o agente vê
        self.posicao = (0, 0)

        # --- A LINHA QUE FALTAVA ---
        self.recompensa_acumulada = 0
        # ---------------------------

    def instala(self, sensor):
        self.sensores.append(sensor)

    def coletar_percepcoes(self, ambiente):
        """Recolhe informação de todos os sensores instalados"""
        dados_sensores = []
        for sensor in self.sensores:
            dados = sensor.ler(self, ambiente)
            dados_sensores.append(dados)

        self.percepcao_atual = dados_sensores
        return self.percepcao_atual

    @abstractmethod
    def age(self):
        """Devolve a ação a tomar"""
        pass

    @abstractmethod
    def avaliacao_estado_atual(self, recompensa: float):
        """Recebe feedback do ambiente"""
        pass