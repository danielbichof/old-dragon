from .IStyle import EstiloRolagem
from ..attributes import Atributos
from ..dice import Dado


class EstiloHeroico(EstiloRolagem):
    """Estilo Heroico: Role 4d6 eliminando o menor, distribua como desejar"""

    def gerar_atributos(self) -> Atributos:
        """Gera atributos no estilo heroico (usando InquirerPy)"""
        from InquirerPy import inquirer
        valores = [Dado.rolar_4d6_eliminar_menor() for _ in range(6)]
        atributos = Atributos()

        print(f"Valores rolados: {valores}")
        print("Distribua os valores nos atributos:")
        nomes_atributos = [
            "Força",
            "Destreza",
            "Constituição",
            "Inteligência",
            "Sabedoria",
            "Carisma",
        ]
        atributos_ordenados = []
        valores_disponiveis = valores.copy()

        for nome_atributo in nomes_atributos:
            escolha = inquirer.select(
                message=f"Escolha o valor para {nome_atributo}:",
                choices=[str(v) for v in valores_disponiveis],
            ).execute()
            valor_escolhido = int(escolha)
            atributos_ordenados.append(valor_escolhido)
            valores_disponiveis.remove(valor_escolhido)

        atributos.definir_atributos_em_ordem(atributos_ordenados)
        return atributos

    def get_nome_estilo(self) -> str:
        return "Estilo Heroico"

    def get_descricao(self) -> str:
        return """Role 4d6 eliminando o d6 mais baixo da soma. Faça isso seis vezes 
e distribua como desejar. Gera personagens superiores ao estilo aventureiro."""
