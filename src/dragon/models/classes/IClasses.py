from abc import ABC, abstractmethod
from typing import List
from dragon.models.data.live_dice import LiveDice


class ICharacterClass(ABC):
    """Classe base para classes de personagem"""

    @property
    @abstractmethod
    def name(self) -> str:
        """Nome da classe"""
        pass

    @property
    @abstractmethod
    def hit_die(self) -> LiveDice:
        """Dado de vida da classe"""
        pass

    @property
    @abstractmethod
    def skills(self) -> List[str]:
        """Lista de perícias da classe"""
        pass

    @property
    @abstractmethod
    def features(self) -> List[str]:
        """Lista de características da classe"""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Descrição da classe"""
        pass
