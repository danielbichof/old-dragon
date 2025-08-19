"""
Sistema de personagens
"""

from dataclasses import dataclass
from typing import Optional
from .attributes import AttributeSet, AttributeType, GameStyle


@dataclass
class Character:
    """Classe base para personagens"""

    name: str
    attributes: AttributeSet
    level: int = 1
    experience: int = 0
    hit_points: int = 0

    def __post_init__(self):
        """Inicialização após criação do dataclass"""
        if self.hit_points == 0:
            self.hit_points = self.calculate_base_hit_points()

    def calculate_base_hit_points(self) -> int:
        """Calcula pontos de vida base (pode ser sobrescrito pelas classes)"""
        # Base simples: constituição + modificador de classe
        return max(1, self.attributes.constituicao // 2)

    def get_attribute_modifier(self, attr_type: AttributeType) -> int:
        """Calcula modificador do atributo (regra comum OSR)"""
        value = self.attributes.get_attribute(attr_type)

        if value <= 3:
            return -3
        elif value <= 5:
            return -2
        elif value <= 8:
            return -1
        elif value <= 12:
            return 0
        elif value <= 15:
            return 1
        elif value <= 17:
            return 2
        else:
            return 3

    def display_character_sheet(self) -> str:
        """Exibe ficha do personagem"""
        sheet = f"\n=== {self.name} ===\n"
        sheet += f"Nível: {self.level}\n"
        sheet += f"Experiência: {self.experience}\n"
        sheet += f"Pontos de Vida: {self.hit_points}\n\n"

        sheet += "ATRIBUTOS:\n"
        for attr_name, value in self.attributes.to_dict().items():
            attr_type = AttributeType(attr_name)
            modifier = self.get_attribute_modifier(attr_type)
            modifier_str = f"+{modifier}" if modifier >= 0 else str(modifier)
            sheet += f"{attr_name}: {value} ({modifier_str})\n"

        return sheet


class CharacterBuilder:
    """Construtor de personagens"""

    @staticmethod
    def create_character_classic(name: str) -> Character:
        """Cria personagem no estilo clássico"""
        from .attributes import AttributeRoller

        attributes = AttributeRoller.create_attributes_classic()
        return Character(name=name, attributes=attributes)

    @staticmethod
    def create_character_with_attributes(
        name: str, attributes: AttributeSet
    ) -> Character:
        """Cria personagem com atributos pré-definidos"""
        return Character(name=name, attributes=attributes)
