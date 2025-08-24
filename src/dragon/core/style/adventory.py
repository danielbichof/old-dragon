from .IStyle import EstiloRolagem
from ..attributes import Atributos
from ..dice import Dado


class EstiloAventureiro(EstiloRolagem):
    """Estilo Aventureiro: Role 3d6 seis vezes e distribua como desejar"""

    def gerar_atributos(self) -> Atributos:
        """Gera atributos no estilo aventureiro (usando InquirerPy)"""
        from InquirerPy import inquirer
        valores = [Dado.rolar_3d6() for _ in range(6)]
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
        return "Estilo Aventureiro"

    def get_descricao(self) -> str:
        return """Role 3d6 seis vezes e distribua como desejar os resultados 
nos seis atributos dos personagens. Mais maleável que o estilo clássico."""
