import time
from ambiente import Ambiente
from agente import Agente


class MotorDeSimulacao:
    def __init__(self, ambiente: Ambiente):
        self.ambiente = ambiente
        self.agentes = []
        self.passo_atual = 0
        self.max_passos = 100

    def adicionar_agente(self, agente: Agente):
        self.agentes.append(agente)

    def lista_agentes(self) -> list:
        return self.agentes

    def executar(self):
        print("--- Início da Simulação ---")

        # Ciclo de simulação
        while self.passo_atual < self.max_passos:
            print(f"\nPasso {self.passo_atual}")

            # 1. Atualizar o ambiente
            self.ambiente.atualizacao()

            # 2. Ciclo de decisão dos agentes
            for agente in self.agentes:
                # --- AQUI ENTRA O TEU CÓDIGO NOVO ---
                # Fase de Percepção: O agente usa sensores para ler o ambiente
                percepcao = agente.coletar_percepcoes(self.ambiente)
                # ------------------------------------

                # O agente decide a ação com base no que os sensores viram
                acao = agente.age()
                print(f"Agente {agente.id} viu {percepcao} e escolheu: {acao}")

                # O ambiente processa a ação e devolve recompensa
                recompensa = self.ambiente.agir(acao, agente)

                # O agente aprende com o resultado
                agente.avaliacao_estado_atual(recompensa)

            self.passo_atual += 1

        print("--- Fim da Simulação ---")