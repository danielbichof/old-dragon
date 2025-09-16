from typing import List, Dict
from .base import Race, Size

class Halfling(Race):
    """Halflings são pequenos, sorridentes e surpreendentemente corajosos.

    Atributos: +2 Destreza, +1 Carisma.
    Tamanho: Pequeno. Deslocamento: 6m. Idiomas: Comum e Halfling.
    Características Especiais: Sorte dos Halflings, Agilidade Halfling, Destemor.
    """

    def __init__(self):
        self.darkvision = 0
        self.alignment = "Neutro"
        self.height_cm = 100
        self.traits = [
            "Sorte dos Halflings (rerrolar 1)",
            "Agilidade Halfling (mover através de espaços maiores)",
            "Destemor (vantagem contra medo)",
        ]

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
        return ["Sorte dos Halflings", "Agilidade Halfling", "Destemor"]

    @property
    def description(self) -> str:
        return (
            "Pequenos e discretos, halflings preferem conforto e paz, mas mostram "
            "coragem notável quando confrontados com perigo."
        )
