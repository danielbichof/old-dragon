from typing import List, Dict
from .base import Race, Size

class Dwarf(Race):
    """Anões são resilientes e disciplinados."""

    @property
    def name(self) -> str:
        return "Anão"

    @property
    def size(self) -> Size:
        return Size.MEDIUM

    @property
    def speed(self) -> int:
        return 6

    @property
    def ability_bonuses(self) -> Dict[str, int]:
        return {"Constituição": 2, "Sabedoria": 1}

    @property
    def special_features(self) -> List[str]:
        return ["Visão no Escuro", "Robustez Anã"]

    @property
    def description(self) -> str:
        return "Resilientes e disciplinados, os anões possuem grande força de vontade e tradição guerreira."
