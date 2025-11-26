from simulador import MotorDeSimulacao
from ambiente_farol import AmbienteFarol
from agente import Agente
from sensor import SensorDirecao


# --- Agente Específico para o Farol ---
class AgenteFarol(Agente):
    def age(self):
        # Verificar se temos percepção válida
        if not self.percepcao_atual:
            return "Norte"

        direcao = self.percepcao_atual[0]  # (dx, dy)
        dx, dy = direcao

        # Lógica para seguir o vetor
        if abs(dx) > abs(dy):
            if dx > 0:
                return "Este"
            else:
                return "Oeste"
        else:
            if dy > 0:
                return "Sul"
            else:
                return "Norte"

    def observacao(self, obs):
        pass

    def avaliacao_estado_atual(self, recompensa):
        """Recebe a recompensa e atualiza o total"""
        self.recompensa_acumulada += recompensa
        print(f"Agente {self.id} recebeu {recompensa}. Total: {self.recompensa_acumulada}")


# --- Execução ---
if __name__ == "__main__":
    # 1. Criar Ambiente
    env = AmbienteFarol(largura=5, altura=5)

    # 2. Criar Agente e Instalar Sensor
    agente = AgenteFarol(id_agente=1)
    agente.instala(SensorDirecao())

    # Inicializar posição do agente
    env.iniciar_agente(agente)

    # 3. Criar Motor e adicionar agente
    motor = MotorDeSimulacao(env)
    motor.adicionar_agente(agente)

    # 4. Correr
    motor.executar()