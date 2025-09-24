from typing import List, Dict
from .base import Race, Size

class Elf(Race):
    """Elfos são belos, graciosos e longevos, ligados à natureza e magia.

    Atributos: +2 Destreza, +1 Inteligência.
    Tamanho: Médio. Deslocamento: 9m. Idiomas: Comum e Élfico.
    Características Especiais: Visão na Penumbra (18m), Sentidos Aguçados, Ancestral Feérico, Transe.
    """

    def __init__(self):
        self.darkvision = 18
        self.alignment = "Neutro"
        self.height_cm = 180
        self.traits = [
            "Sentidos Aguçados (+2 Percepção)",
            "Ancestral Feérico (vantagem contra encantamento, imune a sono)",
            "Transe (4h de meditação)",
        ]

    @property
    def name(self) -> str:
        return "Elfo"

    @property
    def size(self) -> Size:
        return Size.MEDIUM

    @property
    def speed(self) -> int:
        return 9

    @property
    def ability_bonuses(self) -> Dict[str, int]:
        return {"Destreza": 2, "Inteligência": 1}

    @property
    def special_features(self) -> List[str]:
        return [
            "Visão na Penumbra",
            "Sentidos Aguçados",
            "Ancestral Feérico",
            "Transe",
        ]

    @property
    def description(self) -> str:
        return (
            "Elfos são graciosos e longevos, buscando harmonia e equilíbrio, "
            "com forte afinidade mágica e ligação ancestral com a natureza."
        )
