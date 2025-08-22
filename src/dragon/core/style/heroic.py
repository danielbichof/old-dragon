from .IStyle import EstiloRolagem
from ..attributes import Atributos
from ..dice import Dado


class EstiloHeroico(EstiloRolagem):
    """Estilo Heroico: Role 4d6 eliminando o menor, distribua como desejar"""

    def gerar_atributos(self) -> Atributos:
        """Gera atributos no estilo heroico"""
        valores = [Dado.rolar_4d6_eliminar_menor() for _ in range(6)]
        atributos = Atributos()

        print(f"Valores rolados: {valores}")
        print("Distribua os valores nos atributos:")
        print("1. Força")
        print("2. Destreza")
        print("3. Constituição")
        print("4. Inteligência")
        print("5. Sabedoria")
        print("6. Carisma")

        atributos_ordenados = []
        valores_disponiveis = valores.copy()

        for i, nome_atributo in enumerate(
            [
                "Força",
                "Destreza",
                "Constituição",
                "Inteligência",
                "Sabedoria",
                "Carisma",
            ]
        ):
            while True:
                try:
                    print(f"\nValores disponíveis: {valores_disponiveis}")
                    escolha = int(input(f"Escolha o valor para {nome_atributo}: "))
                    if escolha in valores_disponiveis:
                        atributos_ordenados.append(escolha)
                        valores_disponiveis.remove(escolha)
                        break
                    else:
                        print("Valor inválido ou já utilizado!")
                except ValueError:
                    print("Digite um número válido!")

        atributos.definir_atributos_em_ordem(atributos_ordenados)
        return atributos

    def get_nome_estilo(self) -> str:
        return "Estilo Heroico"

    def get_descricao(self) -> str:
        return """Role 4d6 eliminando o d6 mais baixo da soma. Faça isso seis vezes 
e distribua como desejar. Gera personagens superiores ao estilo aventureiro."""
