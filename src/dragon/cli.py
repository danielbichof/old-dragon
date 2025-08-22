from abc import ABC, abstractmethod
from typer import Typer
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

            # Perguntar se quer gerar outro personagem
            while True:
                continuar = (
                    input("\nDeseja gerar outro personagem? (s/n): ").lower().strip()
                )
                if continuar in ["s", "sim", "y", "yes"]:
                    print("\n" + "=" * 50 + "\n")
                    break
                elif continuar in ["n", "não", "nao", "no"]:
                    print("\nObrigado por usar o Gerador de Personagem!")
                    return
                else:
                    print("Resposta inválida! Digite 's' para sim ou 'n' para não.")

        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário. Até logo!")
            return
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            print("Tente novamente.")
