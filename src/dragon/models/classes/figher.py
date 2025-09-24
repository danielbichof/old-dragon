from typing import List
from .IClasses import ICharacterClass
from dragon.models.data.live_dice import LiveDice
from dragon.models.data.combat_style import CombatStyle


class Fighter(ICharacterClass):
    """Guerreiro é um combatente versátil."""

    def __init__(self, combat_style: CombatStyle):
        self._combat_style = combat_style

    @property
    def name(self) -> str:
        return "Guerreiro"

    @property
    def hit_die(self) -> LiveDice:
        return LiveDice.D10

    @property
    def skills(self) -> List[str]:
        return ["Atletismo", "Intimidação", "Luta"]

    @property
    def features(self) -> List[str]:
        return [f"Estilo de Combate ({self._combat_style.name})", "Segundo Fôlego"]

    @property
    def description(self) -> str:
        return "O guerreiro é um combatente versátil que domina diversas armas e armaduras."
