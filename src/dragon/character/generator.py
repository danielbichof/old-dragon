# Interfaces
from ..core.style.IStyle import EstiloRolagem

# ---
from ..core.style.adventory import EstiloAventureiro
from ..core.style.classic import EstiloClassico
from ..core.style.heroic import EstiloHeroico
from ..core.attributes import Atributos



from InquirerPy import inquirer

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
        """Permite ao usuário escolher um estilo de rolagem (usando InquirerPy)"""
        choices = [
            {"name": f"{numero}. {estilo.get_nome_estilo()} - {estilo.get_descricao()}", "value": numero}
            for numero, estilo in self.estilos.items()
        ]
        escolha = inquirer.select(
            message="Escolha o estilo de rolagem:",
            choices=choices,
            default=1,
        ).execute()
        return self.estilos[escolha]

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
