from typing import Dict, List
from .base import Race, Size

class Gnome(Race):
    """Gnomos: sagazes e vigorosos.

    Metadados:
        speed: 6m
        darkvision: 18m
        alignment: "Neutro"
        height_cm: 100 (aprox.)
        traits: Mineradores, Vigoroso, Avaliadores, Sagazes e Vigorosos, Restrições
    """

    def __init__(self):
        self.darkvision = 18
        self.alignment = "Neutro"
        self.height_cm = 100
        self.traits = [
            "Mineradores",
            "Vigoroso",
            "Avaliadores",
            "Sagazes e Vigorosos",
            "Restrições",
        ]

    @property
    def name(self) -> str:
        return "Gnomo"

    @property
    def size(self) -> Size:
        return Size.SMALL

    @property
    def speed(self) -> int:
        return 6

    @property
    def ability_bonuses(self) -> Dict[str, int]:
        # Placeholder - ajustar se houver especificação
        return {"Inteligência": 1}

    @property
    def special_features(self) -> List[str]:
        return self.traits

    @property
    def description(self) -> str:
        return "Gnomos são curiosos e incansáveis, combinando engenhosidade e vigor."
