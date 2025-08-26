from typing import List, Dict
from .base import Race, Size

class Halfling(Race):
    """Halflings são astutos e ágeis."""

    @property
    def name(self) -> str:
        return "Halfling"

    @property
    def size(self) -> Size:
        return Size.SMALL

    @property
    def speed(self) -> int:
        return 6

    @property
    def ability_bonuses(self) -> Dict[str, int]:
        return {"Destreza": 2, "Carisma": 1}

    @property
    def special_features(self) -> List[str]:
        return ["Sorte Halfling"]

    @property
    def description(self) -> str:
        return "Astutos e ágeis, halflings valorizam a comunidade e o conforto, mas também são surpreendentemente corajosos."
