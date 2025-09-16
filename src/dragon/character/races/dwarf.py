from typing import List, Dict
from .base import Race, Size

class Dwarf(Race):
    """Anões são robustos, disciplinados e de grande força de vontade.

    Atributos: +2 Constituição, +1 Sabedoria.
    Tamanho: Médio. Deslocamento: 6m. Idiomas: Comum e Anão.
    Visão no Escuro: até 18m.
    Características Especiais: Visão no Escuro, Robustez Anã, Treinamento Anão em Armas.
    """

    def __init__(self):
        self.darkvision = 18
        self.alignment = "Ordem"
        self.height_cm = 150
        self.traits = [
            "Mineradores",
            "Vigoroso",
            "Armas Grandes",
            "Inimigos",
            "Avaliadores",
            "Sagazes e Vigorosos",
            "Restrições",
        ]

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
        return [
            "Visão no Escuro",
            "Robustez Anã",
            "Treinamento Anão em Armas",
        ]

    @property
    def description(self) -> str:
        return (
            "Os anões são robustos, disciplinados e focados em tradição, família e honra. "
            "Excelentes metalurgistas, habitam fortalezas subterrâneas."
        )
