from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Personagem:
    atributos: Dict[str, int]
    raca: str
    raca_bonus: Dict[str, int]
    classe: str
    hit_die: int
    skills: List[str]
    features: List[str]

    @property
    def soma(self) -> int:
        return sum(self.atributos.values())

    @property
    def maior(self) -> int:
        return max(self.atributos.values())

    @property
    def menor(self) -> int:
        return min(self.atributos.values())

    @property
    def media(self) -> float:
        return round(self.soma / 6, 1)
