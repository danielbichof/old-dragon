from typing import List, Dict
from .base import Race, Size

class Human(Race):
    """Humanos são adaptáveis, ambiciosos e perseverantes."""

    def __init__(self, bonus_choices: List[str]):
        """
        Args:
            bonus_choices: Lista com dois atributos diferentes para receber +1
        """
        if len(bonus_choices) != 2 or len(set(bonus_choices)) != 2:
            raise ValueError("Humanos devem escolher dois atributos diferentes para +1")
        self._bonus_choices = bonus_choices

    @property
    def name(self) -> str:
        return "Humano"

    @property
    def size(self) -> Size:
        return Size.MEDIUM

    @property
    def speed(self) -> int:
        return 9

    @property
    def ability_bonuses(self) -> Dict[str, int]:
        return {attr: 1 for attr in self._bonus_choices}

    @property
    def special_features(self) -> List[str]:
        return ["Versatilidade Humana"]

    @property
    def description(self) -> str:
        return "Os humanos são adaptáveis, ambiciosos e perseverantes. Sua versatilidade os torna comuns em todas as partes do mundo, assumindo múltiplos papéis."
