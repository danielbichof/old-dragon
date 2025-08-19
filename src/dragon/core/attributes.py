"""
Sistema de atributos para jogo de RPG Old School
"""

import random
from enum import Enum
from typing import List, Dict
from dataclasses import dataclass


class AttributeType(Enum):
    """Tipos de atributos do personagem"""

    FORCA = "Força"
    DESTREZA = "Destreza"
    CONSTITUICAO = "Constituição"
    INTELIGENCIA = "Inteligência"
    SABEDORIA = "Sabedoria"
    CARISMA = "Carisma"


class GameStyle(Enum):
    """Estilos de jogo para rolagem de atributos"""

    CLASSICO = "clássico"
    AVENTUREIRO = "aventureiro"
    HEROICO = "heroico"


@dataclass
class AttributeSet:
    """Conjunto de atributos de um personagem"""

    forca: int = 10
    destreza: int = 10
    constituicao: int = 10
    inteligencia: int = 10
    sabedoria: int = 10
    carisma: int = 10

    def get_attribute(self, attr_type: AttributeType) -> int:
        """Retorna o valor de um atributo específico"""
        attr_map = {
            AttributeType.FORCA: self.forca,
            AttributeType.DESTREZA: self.destreza,
            AttributeType.CONSTITUICAO: self.constituicao,
            AttributeType.INTELIGENCIA: self.inteligencia,
            AttributeType.SABEDORIA: self.sabedoria,
            AttributeType.CARISMA: self.carisma,
        }
        return attr_map[attr_type]

    def set_attribute(self, attr_type: AttributeType, value: int) -> None:
        """Define o valor de um atributo específico"""
        if attr_type == AttributeType.FORCA:
            self.forca = value
        elif attr_type == AttributeType.DESTREZA:
            self.destreza = value
        elif attr_type == AttributeType.CONSTITUICAO:
            self.constituicao = value
        elif attr_type == AttributeType.INTELIGENCIA:
            self.inteligencia = value
        elif attr_type == AttributeType.SABEDORIA:
            self.sabedoria = value
        elif attr_type == AttributeType.CARISMA:
            self.carisma = value

    def to_dict(self) -> Dict[str, int]:
        """Converte para dicionário"""
        return {
            "Força": self.forca,
            "Destreza": self.destreza,
            "Constituição": self.constituicao,
            "Inteligência": self.inteligencia,
            "Sabedoria": self.sabedoria,
            "Carisma": self.carisma,
        }


class AttributeRoller:
    """Sistema de rolagem de atributos"""

    @staticmethod
    def roll_3d6() -> int:
        """Rola 3d6 e retorna a soma"""
        return sum(random.randint(1, 6) for _ in range(3))

    @staticmethod
    def roll_4d6_drop_lowest() -> int:
        """Rola 4d6, descarta o menor e retorna a soma dos 3 maiores"""
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.remove(min(rolls))
        return sum(rolls)

    @classmethod
    def generate_attribute_values(cls, style: GameStyle) -> List[int]:
        """Gera 6 valores de atributos baseado no estilo de jogo"""
        values = []

        if style in [GameStyle.CLASSICO, GameStyle.AVENTUREIRO]:
            for _ in range(6):
                values.append(cls.roll_3d6())
        elif style == GameStyle.HEROICO:
            for _ in range(6):
                values.append(cls.roll_4d6_drop_lowest())

        return values

    @classmethod
    def create_attributes_classic(cls) -> AttributeSet:
        """Cria atributos no estilo clássico (ordem fixa)"""
        values = cls.generate_attribute_values(GameStyle.CLASSICO)

        return AttributeSet(
            forca=values[0],
            destreza=values[1],
            constituicao=values[2],
            inteligencia=values[3],
            sabedoria=values[4],
            carisma=values[5],
        )

    @classmethod
    def create_attributes_adventurer(
        cls, distribution: Dict[AttributeType, int]
    ) -> AttributeSet:
        """
        Cria atributos no estilo aventureiro (distribuição livre)

        Args:
            distribution: Dicionário mapeando tipo de atributo para valor rolado
        """
        attributes = AttributeSet()

        for attr_type, value in distribution.items():
            attributes.set_attribute(attr_type, value)

        return attributes

    @classmethod
    def create_attributes_heroic(
        cls, distribution: Dict[AttributeType, int]
    ) -> AttributeSet:
        """
        Cria atributos no estilo heroico (4d6 drop lowest, distribuição livre)

        Args:
            distribution: Dicionário mapeando tipo de atributo para valor rolado
        """
        attributes = AttributeSet()

        for attr_type, value in distribution.items():
            attributes.set_attribute(attr_type, value)

        return attributes


class AttributeInterpreter:
    """Interpretador de valores de atributos"""

    @staticmethod
    def get_attribute_description(value: int) -> str:
        """Retorna descrição qualitativa do valor do atributo"""
        if value <= 3:
            return "Extremamente baixo"
        elif value <= 6:
            return "Muito baixo"
        elif value <= 8:
            return "Baixo"
        elif value <= 12:
            return "Médio"
        elif value <= 15:
            return "Alto"
        elif value <= 17:
            return "Muito alto"
        else:
            return "Excepcional"

    @staticmethod
    def is_notable_weakness(value: int) -> bool:
        """Verifica se o valor representa uma fraqueza notável para interpretação"""
        return value <= 6

    @staticmethod
    def is_exceptional_strength(value: int) -> bool:
        """Verifica se o valor representa uma força excepcional"""
        return value >= 16
