from flask import Flask, render_template, request
from dragon.character.generator import GeradorPersonagem
from dragon.character.races.human import Human
from dragon.character.races.elf import Elf
from dragon.character.races.dwarf import Dwarf
from dragon.character.races.halfling import Halfling
from dragon.character.classes.figher import Fighter
from dragon.character.classes.barbarian import Barbarian
from dragon.character.classes.wizard import Wizard
from dragon.character.classes.scholar import Scholar
from dragon.character.data.combat_style import CombatStyle
from dragon.character.data.arcade_school import ArcaneSchool

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("home.html")


def run():
    app.run(host="127.0.0.1", port=8000, debug=True)


@app.route("/criar", methods=["GET", "POST"])
def criar_personagem():
    gerador = GeradorPersonagem()
    estilos = {
        1: gerador.get_estilo(1).get_nome_estilo(),
        2: gerador.get_estilo(2).get_nome_estilo(),
        3: gerador.get_estilo(3).get_nome_estilo(),
    }

    racas = [
        ("Human", "Humano"),
        ("Elf", "Elfo"),
        ("Dwarf", "Anão"),
        ("Halfling", "Halfling"),
    ]

    classes = [
        ("Barbarian", "Bárbaro"),
        ("Fighter", "Guerreiro"),
        ("Wizard", "Mago"),
        ("Scholar", "Acadêmico"),
    ]

    fighter_estilos = [
        CombatStyle("Defesa", "Aumenta a CA em +1", {"CA": 1}),
        CombatStyle("Armas Grandes", "+2 dano com armas de 2 mãos", {"Dano": 2}),
    ]
    wizard_escolas = [
        ArcaneSchool("Evocação", "Especialista em dano", ["Mísseis Mágicos"]),
        ArcaneSchool("Abjuração", "Proteção e defesa", ["Armadura Arcana"]),
    ]

    if request.method == "GET":
        return render_template(
            "create.html",
            estilos=estilos,
            racas=racas,
            classes=classes,
            fighter_estilos=fighter_estilos,
            wizard_escolas=wizard_escolas,
        )

    step = request.form.get("step", "1")
    estilo_num = int(request.form.get("estilo", "1"))

    if step == "1":
        estilo = gerador.get_estilo(estilo_num)
        # gera valores de acordo com o estilo
        if hasattr(estilo, "gerar_valores"):
            valores = estilo.gerar_valores()
        else:
            valores = None
        return render_template(
            "create.html",
            estilos=estilos,
            racas=racas,
            classes=classes,
            fighter_estilos=fighter_estilos,
            wizard_escolas=wizard_escolas,
            step=2,
            estilo_num=estilo_num,
            valores=valores,
        )

    # step 2: receber distribuicao (se necessário), raça, classe e opções
    # recuperar valores rolados escondidos
    valores = request.form.getlist("valores[]")
    valores = [int(v) for v in valores] if valores else None

    distribuicao = None
    if estilo_num in (2, 3):
        distribuicao = [
            int(request.form.get("forca")),
            int(request.form.get("destreza")),
            int(request.form.get("constituicao")),
            int(request.form.get("inteligencia")),
            int(request.form.get("sabedoria")),
            int(request.form.get("carisma")),
        ]
        # valida que distribuicao é uma permutação dos valores
        if sorted(distribuicao) != sorted(valores):
            erro = "A distribuição deve usar exatamente os valores rolados."
            return render_template(
                "create.html",
                estilos=estilos,
                racas=racas,
                classes=classes,
                fighter_estilos=fighter_estilos,
                wizard_escolas=wizard_escolas,
                step=2,
                estilo_num=estilo_num,
                valores=valores,
                erro=erro,
            )

    atributos = gerador.gerar_personagem(
        estilo_num=estilo_num, distribuicao=distribuicao, valores=valores
    )

    # raça
    raca_key = request.form.get("raca")
    if raca_key == "Human":
        bonus1 = request.form.get("bonus1")
        bonus2 = request.form.get("bonus2")
        raca = Human([bonus1, bonus2])
    elif raca_key == "Elf":
        raca = Elf()
    elif raca_key == "Dwarf":
        raca = Dwarf()
    else:
        raca = Halfling()

    # classe
    classe_key = request.form.get("classe")
    if classe_key == "Fighter":
        cs_name = request.form.get("fighter_style", fighter_estilos[0].name)
        chosen = next(
            (c for c in fighter_estilos if c.name == cs_name), fighter_estilos[0]
        )
        classe = Fighter(chosen)
    elif classe_key == "Wizard":
        sc_name = request.form.get("wizard_school", wizard_escolas[0].name)
        chosen = next(
            (s for s in wizard_escolas if s.name == sc_name), wizard_escolas[0]
        )
        classe = Wizard(chosen)
    elif classe_key == "Barbarian":
        classe = Barbarian()
    else:
        classe = Scholar()

    d = atributos.get_atributos_dict()

    return render_template(
        "create.html",
        estilos=estilos,
        racas=racas,
        classes=classes,
        fighter_estilos=fighter_estilos,
        wizard_escolas=wizard_escolas,
        resultado={
            "atributos": d,
            "raca": raca.name,
            "raca_bonus": raca.ability_bonuses,
            "classe": classe.name,
            "hit_die": classe.hit_die.value,
            "skills": classe.skills,
            "features": classe.features,
            "soma": sum(d.values()),
            "maior": max(d.values()),
            "menor": min(d.values()),
            "media": round(sum(d.values()) / 6, 1),
        },
    )
