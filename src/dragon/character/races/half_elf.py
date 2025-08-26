from typing import Dict, List
from .base import Race, Size

class HalfElf(Race):
    """Meio-Elfos combinam a adaptabilidade humana e a graça élfica.

    Metadados:
        speed: 9m
        darkvision: 9m (interpretação: visão em baixa luz moderada)
        alignment: "Caos" (da especificação)
        height_cm: 170
        traits: Aprendizado, Gracioso e Vigoroso, Idioma Extra, Imunidades
    """

    def __init__(self):
        self.darkvision = 9
        self.alignment = "Caos"
        self.height_cm = 170
        self.traits = [
            "Aprendizado",
            "Gracioso e Vigoroso",
            "Idioma Extra",
            "Imunidades",
        ]

    @property
    def name(self) -> str:
        return "Meio-Elfo"

    @property
    def size(self) -> Size:
        return Size.MEDIUM

    @property
    def speed(self) -> int:
        return 9

    @property
    def ability_bonuses(self) -> Dict[str, int]:
        # Placeholder - ajuste caso regras específicas
        return {"Carisma": 1, "Destreza": 1}

    @property
    def special_features(self) -> List[str]:
        return self.traits

    @property
    def description(self) -> str:
        return "Meio-elfos caminham entre dois mundos, equilibrando adaptabilidade e graça."
