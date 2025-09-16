from dragon.core.style.IStyle import EstiloRolagem
from dragon.core.attributes import Atributos
from dragon.core.dice import Dado



class EstiloHeroico(EstiloRolagem):
    """Estilo Heroico: Role 4d6 eliminando o menor, distribua como desejar"""

    def gerar_valores(self) -> list:
        """Gera os 6 valores de atributos para o estilo heroico."""
        return [Dado.rolar_4d6_eliminar_menor() for _ in range(6)]

    def gerar_atributos(self, distribuicao: list = None, valores: list = None) -> Atributos:
        """
        Gera atributos no estilo heroico.
        Se distribuicao for fornecida, usa a ordem dos valores nela;
        caso contrário, usa a ordem dos valores gerados.
        Se valores for fornecido, usa esses valores; senão, rola os dados.
        """
        if valores is None:
            valores = self.gerar_valores()
        if distribuicao is None:
            distribuicao = valores.copy()
        atributos = Atributos()
        atributos.definir_atributos_em_ordem(distribuicao)
        return atributos

    def get_nome_estilo(self) -> str:
        return "Estilo Heroico"

    def get_descricao(self) -> str:
        return """Role 4d6 eliminando o d6 mais baixo da soma. Faça isso seis vezes 
e distribua como desejar. Gera personagens superiores ao estilo aventureiro."""
