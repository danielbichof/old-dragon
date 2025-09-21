from flask import Blueprint, render_template, request
from typing import List
from dragon.services.character_service import CharacterService

character_bp = Blueprint("character", __name__)
service = CharacterService()


@character_bp.get("/")
def home():
    return render_template("home.html")


@character_bp.get("/criar")
def criar_personagem_form():
    estilos = service.get_estilos()
    racas = service.get_racas()
    classes = service.get_classes()
    fighter_estilos = service.get_fighter_estilos()
    wizard_escolas = service.get_wizard_escolas()

    return render_template(
        "create.html",
        estilos=estilos,
        racas=racas,
        classes=classes,
        fighter_estilos=fighter_estilos,
        wizard_escolas=wizard_escolas,
    )


@character_bp.post("/criar")
def criar_personagem_submit():
    estilos = service.get_estilos()
    racas = service.get_racas()
    classes = service.get_classes()
    fighter_estilos = service.get_fighter_estilos()
    wizard_escolas = service.get_wizard_escolas()

    step = request.form.get("step", "1")
    estilo_num = int(request.form.get("estilo", "1"))

    if step == "1":
        valores = service.gerar_valores(estilo_num)
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

    valores: List[int] | None = request.form.getlist("valores[]")
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

    personagem = service.montar_personagem(
        estilo_num=estilo_num,
        distribuicao=distribuicao,
        valores=valores,
        raca_key=request.form.get("raca"),
        bonus1=request.form.get("bonus1"),
        bonus2=request.form.get("bonus2"),
        classe_key=request.form.get("classe"),
        fighter_style_name=request.form.get("fighter_style"),
        wizard_school_name=request.form.get("wizard_school"),
    )

    return render_template(
        "create.html",
        estilos=estilos,
        racas=racas,
        classes=classes,
        fighter_estilos=fighter_estilos,
        wizard_escolas=wizard_escolas,
        resultado={
            "atributos": personagem.atributos,
            "raca": personagem.raca,
            "raca_bonus": personagem.raca_bonus,
            "classe": personagem.classe,
            "hit_die": personagem.hit_die,
            "skills": personagem.skills,
            "features": personagem.features,
            "soma": personagem.soma,
            "maior": personagem.maior,
            "menor": personagem.menor,
            "media": personagem.media,
        },
    )
