from .IStyle import EstiloRolagem
from ..attributes import Atributos
from ..dice import Dado


class EstiloClassico(EstiloRolagem):
    """Estilo Clássico: Role 3d6 seis vezes na ordem fixa"""

    def gerar_atributos(self) -> Atributos:
        """Gera atributos no estilo clássico"""
        valores = [Dado.rolar_3d6() for _ in range(6)]
        atributos = Atributos()
        atributos.definir_atributos_em_ordem(valores)
        return atributos

    def get_nome_estilo(self) -> str:
        return "Estilo Clássico"

    def get_descricao(self) -> str:
        return """Role 3d6 seis vezes e distribua entre os atributos, seguindo a ordem: 
Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma.
Produz personagens desafiadoramente medianos."""
