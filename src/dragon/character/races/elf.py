from typing import List, Dict
from .base import Race, Size

class Elf(Race):
    """Elfos são altivos e longevos, com afinidade natural para magia."""

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
        return ["Visão na Penumbra", "Sentidos Élficos"]

    @property
    def description(self) -> str:
        return "Altivos e longevos, os elfos vivem em harmonia com a natureza e desenvolvem forte afinidade com magia."
