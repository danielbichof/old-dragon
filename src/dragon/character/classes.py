from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto


class DiceType(Enum):
    """Tipos de dados de vida"""
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12


class CharacterClass(ABC):
    """Classe base para classes de personagem"""
    @property
    @abstractmethod
    def name(self) -> str:
        """Nome da classe"""
        pass

    @property
    @abstractmethod
    def hit_die(self) -> DiceType:
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


@dataclass
class CombatStyle:
    """Estilo de combate para guerreiros"""
    name: str
    description: str
    bonus: Dict[str, int]


class Fighter(CharacterClass):
    """Guerreiro é um combatente versátil."""
    def __init__(self, combat_style: CombatStyle):
        self._combat_style = combat_style

    @property
    def name(self) -> str:
        return "Guerreiro"

    @property
    def hit_die(self) -> DiceType:
        return DiceType.D10

    @property
    def skills(self) -> List[str]:
        return ["Atletismo", "Intimidação", "Luta"]

    @property
    def features(self) -> List[str]:
        return [
            f"Estilo de Combate ({self._combat_style.name})",
            "Segundo Fôlego"
        ]

    @property
    def description(self) -> str:
        return "O guerreiro é um combatente versátil que domina diversas armas e armaduras."


class Barbarian(CharacterClass):
    """Bárbaro é um combatente selvagem."""
    @property
    def name(self) -> str:
        return "Bárbaro"

    @property
    def hit_die(self) -> DiceType:
        return DiceType.D12

    @property
    def skills(self) -> List[str]:
        return ["Atletismo", "Sobrevivência", "Intimidação"]

    @property
    def features(self) -> List[str]:
        return ["Fúria", "Defesa Sem Armadura"]

    @property
    def description(self) -> str:
        return "Um combatente selvagem que canaliza sua fúria para aumentar força e resistência."


@dataclass
class ArcaneSchool:
    """Escola de magia para magos"""
    name: str
    description: str
    bonus_spells: List[str]


class Wizard(CharacterClass):
    """Mago é um mestre da magia arcana."""
    def __init__(self, school: ArcaneSchool):
        self._school = school

    @property
    def name(self) -> str:
        return "Mago"

    @property
    def hit_die(self) -> DiceType:
        return DiceType.D6

    @property
    def skills(self) -> List[str]:
        return ["Arcana", "História", "Investigação"]

    @property
    def features(self) -> List[str]:
        return [
            f"Tradição Arcana ({self._school.name})",
            "Grimório"
        ]

    @property
    def description(self) -> str:
        return "Mestres da magia arcana, estudiosos que manipulam o tecido da realidade."


class Scholar(CharacterClass):
    """Acadêmico é um estudioso versátil."""
    @property
    def name(self) -> str:
        return "Acadêmico"

    @property
    def hit_die(self) -> DiceType:
        return DiceType.D8

    @property
    def skills(self) -> List[str]:
        return ["Investigação", "História", "Diplomacia"]

    @property
    def features(self) -> List[str]:
        return ["Conhecimento Acadêmico", "Versatilidade"]

    @property
    def description(self) -> str:
        return "Estudioso e versátil, combina conhecimento com habilidades úteis fora e dentro do combate."
