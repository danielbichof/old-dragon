# SPDX-FileCopyrightText: 2024-present RPG Developer
# SPDX-License-Identifier: MIT
"""
Sistema de geração de personagens para RPG Old School

Este pacote implementa um sistema completo de criação de personagens
seguindo as regras clássicas de RPG Old School, incluindo diferentes
estilos de rolagem de atributos e classes de personagem.
"""

from .core.attributes import AttributeSet, AttributeType, GameStyle
from .core.character import Character
from .core.classes import PlayerCharacter, Guerreiro, Ladrao, Clerigo, Mago
from .generator import CharacterGenerator, InteractiveCharacterCreator

__all__ = [
    "AttributeSet",
    "AttributeType",
    "GameStyle",
    "Character",
    "PlayerCharacter",
    "Guerreiro",
    "Ladrao",
    "Clerigo",
    "Mago",
    "CharacterGenerator",
    "InteractiveCharacterCreator",
]
