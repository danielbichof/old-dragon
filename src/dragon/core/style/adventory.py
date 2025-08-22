from .IStyle import EstiloRolagem
from ..attributes import Atributos
from ..dice import Dado


class EstiloAventureiro(EstiloRolagem):
    """Estilo Aventureiro: Role 3d6 seis vezes e distribua como desejar"""

    def gerar_atributos(self) -> Atributos:
        """Gera atributos no estilo aventureiro"""
        valores = [Dado.rolar_3d6() for _ in range(6)]
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
        return "Estilo Aventureiro"

    def get_descricao(self) -> str:
        return """Role 3d6 seis vezes e distribua como desejar os resultados 
nos seis atributos dos personagens. Mais maleável que o estilo clássico."""
