from abc import ABC, abstractmethod
# Se precisares de tipos do agente, podes importar,
# mas cuidado com importações circulares. Usamos 'typing' para evitar isso.
from typing import Any

class Ambiente(ABC):
    @abstractmethod
    def observacao_para(self, agente) -> Any:
        """Gera a percepção para um agente específico [cite: 24]"""
        pass

    @abstractmethod
    def atualizacao(self):
        """Atualiza elementos dinâmicos do ambiente [cite: 25]"""
        pass

    @abstractmethod
    def agir(self, accao, agente) -> float:
        """Executa a ação e devolve recompensa [cite: 26]"""
        pass