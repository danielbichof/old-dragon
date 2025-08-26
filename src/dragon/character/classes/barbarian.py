from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional
from IClasses import * 
from dragon.character.data.live_dice import LiveDice

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
