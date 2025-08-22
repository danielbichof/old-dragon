# Interfaces
from ..core.style.IStyle import EstiloRolagem

# ---
from ..core.style.adventory import EstiloAventureiro
from ..core.style.classic import EstiloClassico
from ..core.style.heroic import EstiloHeroico


class GeradorPersonagem:
    """Classe principal para geração de personagens"""

    def __init__(self):
        self.estilos = {1: EstiloClassico(), 2: EstiloAventureiro(), 3: EstiloHeroico()}

    def mostrar_estilos(self) -> None:
        """Mostra os estilos disponíveis"""
        print("=== ESTILOS DE ROLAGEM DISPONÍVEIS ===\n")
        for numero, estilo in self.estilos.items():
            print(f"{numero}. {estilo.get_nome_estilo()}")
            print(f"   {estilo.get_descricao()}\n")

    def escolher_estilo(self) -> EstiloRolagem:
        """Permite ao usuário escolher um estilo de rolagem"""
        self.mostrar_estilos()

        while True:
            try:
                escolha = int(input("Escolha o estilo de rolagem (1-3): "))
                if escolha in self.estilos:
                    return self.estilos[escolha]
                else:
                    print("Opção inválida! Escolha entre 1, 2 ou 3.")
            except ValueError:
                print("Digite um número válido!")

    def gerar_personagem(self) -> Atributos:
        """Gera um personagem completo"""
        print("=== GERADOR DE PERSONAGEM RPG OLD SCHOOL ===\n")

        estilo_escolhido = self.escolher_estilo()

        print(
            f"\n=== GERANDO PERSONAGEM - {estilo_escolhido.get_nome_estilo().upper()} ==="
        )
        print(estilo_escolhido.get_descricao())
        print()

        atributos = estilo_escolhido.gerar_atributos()

        return atributos
