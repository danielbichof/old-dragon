import pytest
from dragon.character.races import Human, Elf, Dwarf, Halfling, Size


def test_human_creation():
    human = Human(["Força", "Destreza"])
    assert human.name == "Humano"
    assert human.size == Size.MEDIUM
    assert human.speed == 9
    assert human.ability_bonuses == {"Força": 1, "Destreza": 1}
    assert "Versatilidade Humana" in human.special_features

def test_human_invalid_bonus():
    with pytest.raises(ValueError):
        # Tentando criar com mesmo atributo duas vezes
        Human(["Força", "Força"])

def test_elf_creation():
    elf = Elf()
    assert elf.name == "Elfo"
    assert elf.size == Size.MEDIUM
    assert elf.speed == 9
    assert elf.ability_bonuses == {"Destreza": 2, "Inteligência": 1}
    assert "Visão na Penumbra" in elf.special_features
    assert "Sentidos Élficos" in elf.special_features

def test_dwarf_creation():
    dwarf = Dwarf()
    assert dwarf.name == "Anão"
    assert dwarf.size == Size.MEDIUM
    assert dwarf.speed == 6
    assert dwarf.ability_bonuses == {"Constituição": 2, "Sabedoria": 1}
    assert "Visão no Escuro" in dwarf.special_features
    assert "Robustez Anã" in dwarf.special_features

def test_halfling_creation():
    halfling = Halfling()
    assert halfling.name == "Halfling"
    assert halfling.size == Size.SMALL
    assert halfling.speed == 6
    assert halfling.ability_bonuses == {"Destreza": 2, "Carisma": 1}
    assert "Sorte Halfling" in halfling.special_features
