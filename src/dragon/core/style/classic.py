from dragon.core.style.IStyle import EstiloRolagem
from dragon.core.attributes import Atributos
from dragon.core.dice import Dado



class EstiloClassico(EstiloRolagem):
    """Estilo Clássico: Role 3d6 seis vezes na ordem fixa"""

    def gerar_valores(self) -> list:
        """Gera os 6 valores de atributos para o estilo clássico."""
        return [Dado.rolar_3d6() for _ in range(6)]

    def gerar_atributos(self, valores: list = None) -> Atributos:
        """
        Gera atributos no estilo clássico.
        Se valores for fornecido, usa esses valores; senão, rola os dados.
        """
        if valores is None:
            valores = self.gerar_valores()
        atributos = Atributos()
        atributos.definir_atributos_em_ordem(valores)
        return atributos

    def get_nome_estilo(self) -> str:
        return "Estilo Clássico"

    def get_descricao(self) -> str:
        return """Role 3d6 seis vezes e distribua entre os atributos, seguindo a ordem: 
Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma.
Produz personagens desafiadoramente medianos."""
