from .IStyle import EstiloRolagem
from ..attributes import Atributos
from ..dice import Dado


class EstiloAventureiro(EstiloRolagem):
    """Estilo Aventureiro: Role 3d6 seis vezes e distribua como desejar"""

    def gerar_valores(self) -> list:
        """Gera os 6 valores de atributos para o estilo aventureiro."""
        return [Dado.rolar_3d6() for _ in range(6)]

    def gerar_atributos(
        self, distribuicao: list = None, valores: list = None
    ) -> Atributos:
        """
        Gera atributos no estilo aventureiro.
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
        return "Estilo Aventureiro"

    def get_descricao(self) -> str:
        return """Role 3d6 seis vezes e distribua como desejar os resultados 
nos seis atributos dos personagens. Mais maleável que o estilo clássico."""
