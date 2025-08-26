from dataclasses import dataclass
from typing import List


@dataclass
class ArcaneSchool:
    """Escola de magia para magos"""

    name: str
    description: str
    bonus_spells: List[str]
