from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto

class Size(Enum):
    """Enumeração para tamanhos de personagem"""
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()

class Race(ABC):
    """Classe base para raças"""
    @property
    @abstractmethod
    def name(self) -> str:
        """Nome da raça"""
        pass

    @property
    @abstractmethod
    def size(self) -> Size:
        """Tamanho da raça"""
        pass

    @property
    @abstractmethod
    def speed(self) -> int:
        """Deslocamento em metros"""
        pass

    @property
    @abstractmethod
    def ability_bonuses(self) -> Dict[str, int]:
        """Bônus de atributos da raça"""
        pass

    @property
    @abstractmethod
    def special_features(self) -> List[str]:
        """Características especiais da raça"""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Descrição da raça"""
        pass


class Human(Race):
    """Humanos são adaptáveis, ambiciosos e perseverantes."""
    def __init__(self, bonus_choices: List[str]):
        """
        Args:
            bonus_choices: Lista com dois atributos diferentes para receber +1
        """
        if len(bonus_choices) != 2 or len(set(bonus_choices)) != 2:
            raise ValueError("Humanos devem escolher dois atributos diferentes para +1")
        self._bonus_choices = bonus_choices

    @property
    def name(self) -> str:
        return "Humano"

    @property
    def size(self) -> Size:
        return Size.MEDIUM

    @property
    def speed(self) -> int:
        return 9

    @property
    def ability_bonuses(self) -> Dict[str, int]:
        return {attr: 1 for attr in self._bonus_choices}

    @property
    def special_features(self) -> List[str]:
        return ["Versatilidade Humana"]

    @property
    def description(self) -> str:
        return "Os humanos são adaptáveis, ambiciosos e perseverantes. Sua versatilidade os torna comuns em todas as partes do mundo, assumindo múltiplos papéis."


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
        return {
            "Destreza": 2,
            "Inteligência": 1
        }

    @property
    def special_features(self) -> List[str]:
        return ["Visão na Penumbra", "Sentidos Élficos"]

    @property
    def description(self) -> str:
        return "Altivos e longevos, os elfos vivem em harmonia com a natureza e desenvolvem forte afinidade com magia."


class Dwarf(Race):
    """Anões são resilientes e disciplinados."""
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
        return {
            "Constituição": 2,
            "Sabedoria": 1
        }

    @property
    def special_features(self) -> List[str]:
        return ["Visão no Escuro", "Robustez Anã"]

    @property
    def description(self) -> str:
        return "Resilientes e disciplinados, os anões possuem grande força de vontade e tradição guerreira."


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
        return {
            "Destreza": 2,
            "Carisma": 1
        }

    @property
    def special_features(self) -> List[str]:
        return ["Sorte Halfling"]

    @property
    def description(self) -> str:
        return "Astutos e ágeis, halflings valorizam a comunidade e o conforto, mas também são surpreendentemente corajosos."
