# Interfaces
from dragon.core.style.IStyle import EstiloRolagem
from .races import Human, Elf, Dwarf, Halfling  # noqa: F401
# ---
from dragon.core.style.adventory import EstiloAventureiro
from dragon.core.style.classic import EstiloClassico
from dragon.core.style.heroic import EstiloHeroico
from dragon.core.attributes import Atributos


from InquirerPy import inquirer


class GeradorPersonagem:
    """Classe principal para geração de personagens (sem interação CLI)"""

    def __init__(self):
        self.estilos = {1: EstiloClassico(), 2: EstiloAventureiro(), 3: EstiloHeroico()}

    def get_estilos(self):
        """Retorna um dicionário dos estilos disponíveis."""
        return self.estilos

    def get_estilo(self, numero: int) -> EstiloRolagem:
        """Retorna o estilo de rolagem pelo número."""
        return self.estilos[numero]

    def gerar_personagem(
        self, estilo_num: int, distribuicao: list = None, valores: list = None
    ) -> Atributos:
        """
        Gera um personagem completo a partir do número do estilo e parâmetros opcionais.
        """
        estilo = self.get_estilo(estilo_num)
        if hasattr(estilo, "gerar_atributos"):
            # Para estilos que aceitam distribuicao e valores
            try:
                return estilo.gerar_atributos(
                    distribuicao=distribuicao, valores=valores
                )
            except TypeError:
                # Para estilos que só aceitam valores
                return estilo.gerar_atributos(valores=valores)
        raise ValueError(
            "Estilo inválido ou não implementa gerar_atributos corretamente."
        )
