from typing import List
from .IClasses import ICharacterClass
from dragon.models.data.live_dice import LiveDice


class Barbarian(ICharacterClass):
    """Bárbaro é um combatente selvagem."""

    @property
    def name(self) -> str:
        return "Bárbaro"

    @property
    def hit_die(self) -> LiveDice:
        return LiveDice.D12

    @property
    def skills(self) -> List[str]:
        return ["Atletismo", "Sobrevivência", "Intimidação"]

    @property
    def features(self) -> List[str]:
        return ["Fúria", "Defesa Sem Armadura"]

    @property
    def description(self) -> str:
        return "Um combatente selvagem que canaliza sua fúria para aumentar força e resistência."
