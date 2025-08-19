"""
Classes de personagens para RPG Old School
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict
from .character import Character
from .attributes import AttributeType


class CharacterClass(ABC):
    """Classe base abstrata para classes de personagem"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Nome da classe"""
        pass
    
    @property
    @abstractmethod
    def hit_die(self) -> int:
        """Dado de vida da classe"""
        pass
    
    @property
    @abstractmethod
    def prime_attributes(self) -> List[AttributeType]:
        """Atributos principais da classe"""
        pass
    
    @abstractmethod
    def get_base_hit_points(self, constitution: int) -> int:
        """Calcula pontos de vida base"""
        pass
    
    @abstractmethod
    def get_class_abilities(self, level: int) -> List[str]:
        """Retorna habilidades da classe por nível"""
        pass


class Guerreiro(CharacterClass):
    """Classe Guerreiro"""
    
    @property
    def name(self) -> str:
        return "Guerreiro"
    
    @property
    def hit_die(self) -> int:
        return 8
    
    @property
    def prime_attributes(self) -> List[AttributeType]:
        return [AttributeType.FORCA]
    
    def get_base_hit_points(self, constitution: int) -> int:
        """Guerreiros têm d8 de vida + modificador de constituição"""
        import random
        base_hp = random.randint(1, self.hit_die)
        con_modifier = self._get_constitution_modifier(constitution)
        return max(1, base_hp + con_modifier)
    
    def get_class_abilities(self, level: int) -> List[str]:
        """Habilidades do guerreiro por nível"""
        abilities = ["Combate especializado", "Usar qualquer armadura"]
        
        if level >= 3:
            abilities.append("Liderança de tropas")
        if level >= 5:
            abilities.append("Ataques múltiplos")
        
        return abilities
    
    def _get_constitution_modifier(self, constitution: int) -> int:
        """Calcula modificador de constituição"""
        if constitution <= 3:
            return -3
        elif constitution <= 5:
            return -2
        elif constitution <= 8:
            return -1
        elif constitution <= 12:
            return 0
        elif constitution <= 15:
            return 1
        elif constitution <= 17:
            return 2
        else:
            return 3


class Ladrao(CharacterClass):
    """Classe Ladrão"""
    
    @property
    def name(self) -> str:
        return "Ladrão"
    
    @property
    def hit_die(self) -> int:
        return 4
    
    @property
    def prime_attributes(self) -> List[AttributeType]:
        return [AttributeType.DESTREZA]
    
    def get_base_hit_points(self, constitution: int) -> int:
        """Ladrões têm d4 de vida + modificador de constituição"""
        import random
        base_hp = random.randint(1, self.hit_die)
        con_modifier = self._get_constitution_modifier(constitution)
        return max(1, base_hp + con_modifier)
    
    def get_class_abilities(self, level: int) -> List[str]:
        """Habilidades do ladrão por nível"""
        abilities = [
            "Escalar paredes",
            "Desarmar armadilhas",
            "Abrir fechaduras",
            "Mover-se silenciosamente",
            "Esconder-se nas sombras"
        ]
        
        if level >= 2:
            abilities.append("Ataque pelas costas")
        if level >= 4:
            abilities.append("Ler linguagens")
        
        return abilities
    
    def _get_constitution_modifier(self, constitution: int) -> int:
        """Calcula modificador de constituição"""
        if constitution <= 3:
            return -3
        elif constitution <= 5:
            return -2
        elif constitution <= 8:
            return -1
        elif constitution <= 12:
            return 0
        elif constitution <= 15:
            return 1
        elif constitution <= 17:
            return 2
        else:
            return 3


class Clerigo(CharacterClass):
    """Classe Clérigo"""
    
    @property
    def name(self) -> str:
        return "Clérigo"
    
    @property
    def hit_die(self) -> int:
        return 6
    
    @property
    def prime_attributes(self) -> List[AttributeType]:
        return [AttributeType.SABEDORIA]
    
    def get_base_hit_points(self, constitution: int) -> int:
        """Clérigos têm d6 de vida + modificador de constituição"""
        import random
        base_hp = random.randint(1, self.hit_die)
        con_modifier = self._get_constitution_modifier(constitution)
        return max(1, base_hp + con_modifier)
    
    def get_class_abilities(self, level: int) -> List[str]:
        """Habilidades do clérigo por nível"""
        abilities = [
            "Conjurar magias divinas",
            "Expulsar mortos-vivos",
            "Usar armaduras médias"
        ]
        
        if level >= 2:
            abilities.append("Cura mágica")
        if level >= 3:
            abilities.append("Proteção contra mal")
        
        return abilities
    
    def _get_constitution_modifier(self, constitution: int) -> int:
        """Calcula modificador de constituição"""
        if constitution <= 3:
            return -3
        elif constitution <= 5:
            return -2
        elif constitution <= 8:
            return -1
        elif constitution <= 12:
            return 0
        elif constitution <= 15:
            return 1
        elif constitution <= 17:
            return 2
        else:
            return 3


class Mago(CharacterClass):
    """Classe Mago"""
    
    @property
    def name(self) -> str:
        return "Mago"
    
    @property
    def hit_die(self) -> int:
        return 4
    
    @property
    def prime_attributes(self) -> List[AttributeType]:
        return [AttributeType.INTELIGENCIA]
    
    def get_base_hit_points(self, constitution: int) -> int:
        """Magos têm d4 de vida + modificador de constituição"""
        import random
        base_hp = random.randint(1, self.hit_die)
        con_modifier = self._get_constitution_modifier(constitution)
        return max(1, base_hp + con_modifier)
    
    def get_class_abilities(self, level: int) -> List[str]:
        """Habilidades do mago por nível"""
        abilities = [
            "Conjurar magias arcanas",
            "Ler magias",
            "Pesquisar magias"
        ]
        
        if level >= 2:
            abilities.append("Identificar itens mágicos")
        if level >= 3:
            abilities.append("Criar pergaminhos")
        if level >= 5:
            abilities.append("Criar itens mágicos")
        
        return abilities
    
    def _get_constitution_modifier(self, constitution: int) -> int:
        """Calcula modificador de constituição"""
        if constitution <= 3:
            return -3
        elif constitution <= 5:
            return -2
        elif constitution <= 8:
            return -1
        elif constitution <= 12:
            return 0
        elif constitution <= 15:
            return 1
        elif constitution <= 17:
            return 2
        else:
            return 3


@dataclass
class PlayerCharacter(Character):
    """Personagem jogador com classe específica"""
    character_class: CharacterClass = None
    
    def __post_init__(self):
        """Inicialização após criação"""
        if self.character_class and self.hit_points == 0:
            self.hit_points = self.character_class.get_base_hit_points(
                self.attributes.constituicao
            )
    
    def get_class_abilities(self) -> List[str]:
        """Retorna habilidades da classe atual"""
        if self.character_class:
            return self.character_class.get_class_abilities(self.level)
        return []
    
    def display_character_sheet(self) -> str:
        """Exibe ficha completa do personagem"""
        sheet = super().display_character_sheet()
        
        if self.character_class:
            sheet += f"\nClasse: {self.character_class.name}\n"
            sheet += f"Dado de Vida: d{self.character_class.hit_die}\n"
            
            prime_attrs = ", ".join([attr.value for attr in self.character_class.prime_attributes])
            sheet += f"Atributos Principais: {prime_attrs}\n"
            
            abilities = self.get_class_abilities()
            if abilities:
                sheet += "\nHABILIDADES DE CLASSE:\n"
                for ability in abilities:
                    sheet += f"• {ability}\n"
        
        return sheet


class ClassRecommender:
    """Sistema para recomendar classes baseado nos atributos"""
    
    @staticmethod
    def recommend_classes(attributes: "AttributeSet") -> List[tuple]:
        """
        Recomenda classes baseado nos atributos do personagem
        
        Returns:
            Lista de tuplas (classe, pontuação, motivo)
        """
        recommendations = []
        
        # Guerreiro
        score = attributes.forca
        reason = f"Força {attributes.forca}"
        if attributes.constituicao >= 13:
            score += 2
            reason += f", Constituição alta ({attributes.constituicao})"
        recommendations.append((Guerreiro(), score, reason))
        
        # Ladrão
        score = attributes.destreza
        reason = f"Destreza {attributes.destreza}"
        if attributes.inteligencia >= 12:
            score += 1
            reason += f", Inteligência adequada ({attributes.inteligencia})"
        recommendations.append((Ladrao(), score, reason))
        
        # Clérigo
        score = attributes.sabedoria
        reason = f"Sabedoria {attributes.sabedoria}"
        if attributes.constituicao >= 12:
            score += 1
            reason += f", Constituição adequada ({attributes.constituicao})"
        recommendations.append((Clerigo(), score, reason))
        
        # Mago
        score = attributes.inteligencia
        reason = f"Inteligência {attributes.inteligencia}"
        if attributes.sabedoria >= 12:
            score += 1
            reason += f", Sabedoria adequada ({attributes.sabedoria})"
        recommendations.append((Mago(), score, reason))
        
        # Ordena por pontuação (maior primeiro)
        recommendations.sort(key=lambda x: x[1], reverse=True)
        
        return recommendations