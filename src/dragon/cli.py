"""
Interface de linha de comando para o gerador de personagens
"""

import sys
from .generator import InteractiveCharacterCreator


def main():
    """Função principal da CLI"""
    try:
        creator = InteractiveCharacterCreator()
        character = creator.create_character_interactive()

        print("\n" + "=" * 50)
        print("PERSONAGEM CRIADO COM SUCESSO!")
        print("=" * 50)
        print(character.display_character_sheet())

    except KeyboardInterrupt:
        print("\n\nCriação de personagem cancelada.")
        sys.exit(0)
    except Exception as e:
        print(f"\nErro durante a criação do personagem: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
