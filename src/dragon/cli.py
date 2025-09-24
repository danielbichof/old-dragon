import typer
from InquirerPy import inquirer
from dragon.models.generator import GeradorPersonagem
from dragon.models.races.human import Human
from dragon.models.races.elf import Elf
from dragon.models.races.dwarf import Dwarf
from dragon.models.races.halfling import Halfling
from dragon.models.classes.figher import Fighter
from dragon.models.classes.barbarian import Barbarian
from dragon.models.classes.wizard import Wizard
from dragon.models.classes.scholar import Scholar
from dragon.models.data.combat_style import CombatStyle
from dragon.models.data.arcade_school import ArcaneSchool

app = typer.Typer()


@app.command()
def gerar():
    """Gera um personagem interativamente pelo CLI (atributos, raça e classe)."""
    gerador = GeradorPersonagem()
    estilos = gerador.get_estilos()

    choices = [
        {
            "name": f"{num}. {estilo.get_nome_estilo()} - {estilo.get_descricao()}",
            "value": num,
        }
        for num, estilo in estilos.items()
    ]

    escolha = inquirer.select(
        message="Escolha o estilo de rolagem:",
        choices=choices,
        default=1,
    ).execute()

    estilo = estilos[escolha]
    # Geração dos valores
    if hasattr(estilo, "gerar_valores"):
        valores = estilo.gerar_valores()
    else:
        valores = None
    # Se for estilo clássico, não precisa distribuir
    if estilo.__class__.__name__ == "EstiloClassico":
        atributos = estilo.gerar_atributos(valores=valores)
    else:
        nomes_atributos = [
            "Força",
            "Destreza",
            "Constituição",
            "Inteligência",
            "Sabedoria",
            "Carisma",
        ]
        print(f"Valores rolados: {valores}")
        distribuicao = []
        valores_disponiveis = valores.copy()
        for nome in nomes_atributos:
            escolha_valor = inquirer.select(
                message=f"Escolha o valor para {nome}:",
                choices=[str(v) for v in valores_disponiveis],
            ).execute()
            valor_escolhido = int(escolha_valor)
            distribuicao.append(valor_escolhido)
            valores_disponiveis.remove(valor_escolhido)
        atributos = estilo.gerar_atributos(distribuicao=distribuicao, valores=valores)
    # Escolha da raça
    racas_opts = [
        ("Humano", Human),
        ("Elfo", Elf),
        ("Anão", Dwarf),
        ("Halfling", Halfling),
    ]
    r_escolha = inquirer.select(
        message="Escolha a raça:",
        choices=[{"name": n, "value": cls} for n, cls in racas_opts],
    ).execute()
    if r_escolha is Human:
        # escolher dois atributos diferentes para +1
        atributos_nomes = list(atributos.get_atributos_dict().keys())
        bonus1 = inquirer.select(
            message="Escolha o primeiro bônus (+1):",
            choices=atributos_nomes,
        ).execute()
        atributos_nomes_sem1 = [a for a in atributos_nomes if a != bonus1]
        bonus2 = inquirer.select(
            message="Escolha o segundo bônus (+1):",
            choices=atributos_nomes_sem1,
        ).execute()
        raca = Human([bonus1, bonus2])
    else:
        raca = r_escolha()

    # (Bônus raciais não aplicados diretamente aos valores de atributos nesta versão.)

    # Escolha da classe
    classes_base = [
        ("Bárbaro", Barbarian),
        ("Guerreiro", Fighter),
        ("Mago", Wizard),
        ("Acadêmico", Scholar),
    ]
    classe_type = inquirer.select(
        message="Escolha a classe:",
        choices=[{"name": n, "value": cls} for n, cls in classes_base],
    ).execute()

    # Configurações adicionais por classe
    if classe_type is Fighter:
        estilos_combate = [
            CombatStyle("Defesa", "Aumenta a CA em +1", {"CA": 1}),
            CombatStyle("Armas Grandes", "+2 dano com armas de 2 mãos", {"Dano": 2}),
        ]
        esc_style = inquirer.select(
            message="Escolha estilo de combate:",
            choices=[{"name": f"{i+1}. {c.name} - {c.description}", "value": c} for i, c in enumerate(estilos_combate)],
        ).execute()
        classe = Fighter(esc_style)
    elif classe_type is Wizard:
        escolas = [
            ArcaneSchool("Evocação", "Especialista em dano", ["Mísseis Mágicos"]),
            ArcaneSchool("Abjuração", "Proteção e defesa", ["Armadura Arcana"]),
        ]
        esc_school = inquirer.select(
            message="Escolha a escola arcana:",
            choices=[{"name": f"{i+1}. {e.name} - {e.description}", "value": e} for i, e in enumerate(escolas)],
        ).execute()
        classe = Wizard(esc_school)
    else:
        classe = classe_type()

    print("\n" + "=" * 60)
    print("PERSONAGEM GERADO COM SUCESSO!")
    print("=" * 60)
    d = atributos.get_atributos_dict()
    for k, v in d.items():
        print(f"{k:<15}: {v}")
    print("-" * 60)
    print(f"Raça: {raca.name} | Bônus: {raca.ability_bonuses}")
    print(f"Classe: {classe.name} | PV dado: d{classe.hit_die.value}")
    print("Perícias:", ", ".join(classe.skills))
    print("Características:")
    for feat in classe.features:
        print(f"  - {feat}")
    print("-" * 60)
    print(f"Soma total dos atributos: {sum(d.values())}")
    print(f"Maior atributo: {max(d.values())}")
    print(f"Menor atributo: {min(d.values())}")
    print(f"Média dos atributos: {sum(d.values())/6:.1f}")


if __name__ == "__main__":
    app()
