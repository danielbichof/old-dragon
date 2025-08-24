from abc import ABC, abstractmethod
from typer import Typer
from InquirerPy import inquirer
from .character.generator import GeradorPersonagem

app = Typer()


@app.command()
def main():
    """Função principal do programa"""
    gerador = GeradorPersonagem()

    while True:
        try:
            personagem = gerador.gerar_personagem()

            print("\n" + "=" * 50)
            print("PERSONAGEM GERADO COM SUCESSO!")
            print("=" * 50)
            print(personagem)

            # Calcular e mostrar algumas estatísticas
            atributos_dict = personagem.get_atributos_dict()
            valores = list(atributos_dict.values())

            print(f"Soma total dos atributos: {sum(valores)}")
            print(f"Maior atributo: {max(valores)}")
            print(f"Menor atributo: {min(valores)}")
            print(f"Média dos atributos: {sum(valores)/6:.1f}")

            # Perguntar se quer gerar outro personagem (usando InquirerPy)
            continuar = inquirer.select(
                message="Deseja gerar outro personagem?",
                choices=[
                    {"name": "Sim", "value": "sim"},
                    {"name": "Não", "value": "nao"},
                ],
                default="sim",
            ).execute()
            if continuar == "sim":
                print("\n" + "=" * 50 + "\n")
                continue
            else:
                print("\nObrigado por usar o Gerador de Personagem!")
                return

        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário. Até logo!")
            return
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            print("Tente novamente.")
