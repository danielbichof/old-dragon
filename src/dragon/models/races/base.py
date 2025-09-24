from abc import ABC, abstractmethod
from typing import List, Dict
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
