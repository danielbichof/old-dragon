from dataclasses import dataclass
from typing import Dict


@dataclass
class CombatStyle:
    """Estilo de combate para guerreiros"""

    name: str
    description: str
    bonus: Dict[str, int]
