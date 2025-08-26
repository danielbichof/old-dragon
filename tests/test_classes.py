import pytest
from dragon.character.classes import (
    Fighter, Barbarian, Wizard, Scholar,
    CombatStyle, ArcaneSchool, LiveDice
)

def test_fighter_creation():
    style = CombatStyle(
        name="Defesa",
        description="Aumenta a CA em +1",
        bonus={"CA": 1}
    )
    fighter = Fighter(combat_style=style)
    assert fighter.name == "Guerreiro"
    assert fighter.hit_die == LiveDice.D10
    assert set(fighter.skills) == {"Atletismo", "Intimidação", "Luta"}
    assert "Estilo de Combate (Defesa)" in fighter.features
    assert "Segundo Fôlego" in fighter.features

def test_barbarian_creation():
    barbarian = Barbarian()
    assert barbarian.name == "Bárbaro"
    assert barbarian.hit_die == LiveDice.D12
    assert set(barbarian.skills) == {"Atletismo", "Sobrevivência", "Intimidação"}
    assert "Fúria" in barbarian.features
    assert "Defesa Sem Armadura" in barbarian.features

def test_wizard_creation():
    school = ArcaneSchool(
        name="Evocação",
        description="Especialista em magias de dano",
        bonus_spells=["Mísseis Mágicos", "Bola de Fogo"]
    )
    wizard = Wizard(school=school)
    assert wizard.name == "Mago"
    assert wizard.hit_die == LiveDice.D6
    assert set(wizard.skills) == {"Arcana", "História", "Investigação"}
    assert "Tradição Arcana (Evocação)" in wizard.features
    assert "Grimório" in wizard.features

def test_scholar_creation():
    scholar = Scholar()
    assert scholar.name == "Acadêmico"
    assert scholar.hit_die == LiveDice.D8
    assert set(scholar.skills) == {"Investigação", "História", "Diplomacia"}
    assert "Conhecimento Acadêmico" in scholar.features
    assert "Versatilidade" in scholar.features
