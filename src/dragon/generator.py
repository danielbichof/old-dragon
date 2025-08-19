"""
Gerador de personagens para o jogo
"""
from typing import Dict, List, Optional
from .core.attributes import (
    AttributeSet, AttributeType, AttributeRoller, 
    GameStyle, AttributeInterpreter
)
from .core.character import Character
from .core.classes import (
    PlayerCharacter, Guerreiro, Ladrao, Clerigo, Mago,
    CharacterClass, ClassRecommender
)


class CharacterGenerator:
    """Gerador principal de personagens"""
    
    AVAILABLE_CLASSES = {
        "guerreiro": Guerreiro(),
        "ladrao": Ladrao(),
        "clerigo": Clerigo(),
        "mago": Mago()
    }
    
    @classmethod
    def generate_classic_character(cls, name: str, character_class_name: Optional[str] = None) -> PlayerCharacter:
        """
        Gera personagem no estilo clássico (atributos em ordem fixa)
        
        Args:
            name: Nome do personagem
            character_class_name: Nome da classe (opcional, será recomendada se não fornecida)
        """
        attributes = AttributeRoller.create_attributes_classic()
        
        if character_class_name:
            character_class = cls.AVAILABLE_CLASSES.get(character_class_name.lower())
        else:
            # Recomenda a melhor classe baseada nos atributos
            recommendations = ClassRecommender.recommend_classes(attributes)
            character_class = recommendations[0][0]  # Melhor recomendação
        
        return PlayerCharacter(
            name=name,
            attributes=attributes,
            character_class=character_class
        )
    
    @classmethod
    def generate_adventurer_character(
        cls, 
        name: str,
        attribute_distribution: Dict[AttributeType, int],
        character_class_name: str
    ) -> PlayerCharacter:
        """
        Gera personagem no estilo aventureiro (distribuição livre de atributos 3d6)
        
        Args:
            name: Nome do personagem
            attribute_distribution: Dicionário com distribuição de atributos
            character_class_name: Nome da classe
        """
        attributes = AttributeRoller.create_attributes_adventurer(attribute_distribution)
        character_class = cls.AVAILABLE_CLASSES.get(character_class_name.lower())
        
        return PlayerCharacter(
            name=name,
            attributes=attributes,
            character_class=character_class
        )
    
    @classmethod
    def generate_heroic_character(
        cls,
        name: str,
        attribute_distribution: Dict[AttributeType, int],
        character_class_name: str
    ) -> PlayerCharacter:
        """
        Gera personagem no estilo heroico (4d6 drop lowest, distribuição livre)
        
        Args:
            name: Nome do personagem
            attribute_distribution: Dicionário com distribuição de atributos
            character_class_name: Nome da classe
        """
        attributes = AttributeRoller.create_attributes_heroic(attribute_distribution)
        character_class = cls.AVAILABLE_CLASSES.get(character_class_name.lower())
        
        return PlayerCharacter(
            name=name,
            attributes=attributes,
            character_class=character_class
        )
    
    @classmethod
    def roll_attributes_for_style(cls, style: GameStyle) -> List[int]:
        """Rola valores de atributos para um estilo específico"""
        return AttributeRoller.generate_attribute_values(style)
    
    @classmethod
    def get_class_recommendations(cls, attributes: AttributeSet) -> List[str]:
        """Retorna recomendações de classe formatadas"""
        recommendations = ClassRecommender.recommend_classes(attributes)
        
        result = []
        for char_class, score, reason in recommendations:
            result.append(f"{char_class.name}: {score} pontos ({reason})")
        
        return result
    
    @classmethod
    def analyze_attributes(cls, attributes: AttributeSet) -> Dict[str, str]:
        """Analisa atributos e retorna interpretações"""
        analysis = {}
        
        for attr_name, value in attributes.to_dict().items():
            description = AttributeInterpreter.get_attribute_description(value)
            
            notes = []
            if AttributeInterpreter.is_notable_weakness(value):
                notes.append("⚠️ Fraqueza notável - ótima para interpretação!")
            if AttributeInterpreter.is_exceptional_strength(value):
                notes.append("⭐ Força excepcional!")
            
            full_description = f"{description} ({value})"
            if notes:
                full_description += " " + " ".join(notes)
            
            analysis[attr_name] = full_description
        
        return analysis


class InteractiveCharacterCreator:
    """Criador interativo de personagens"""
    
    def __init__(self):
        self.generator = CharacterGenerator()
    
    def create_character_interactive(self) -> PlayerCharacter:
        """Processo interativo de criação de personagem"""
        print("=== CRIADOR DE PERSONAGENS ===\n")
        
        # Nome do personagem
        name = input("Digite o nome do seu personagem: ").strip()
        if not name:
            name = "Aventureiro"
        
        # Escolha do estilo
        print("\nEscolha o estilo de jogo:")
        print("1. Clássico - 3d6 em ordem (Força, Destreza, Constituição, etc.)")
        print("2. Aventureiro - 3d6 com distribuição livre")
        print("3. Heroico - 4d6 (remove menor) com distribuição livre")
        
        while True:
            choice = input("\nDigite sua escolha (1-3): ").strip()
            if choice in ["1", "2", "3"]:
                break
            print("Escolha inválida! Digite 1, 2 ou 3.")
        
        if choice == "1":
            return self._create_classic_style(name)
        elif choice == "2":
            return self._create_adventurer_style(name)
        else:
            return self._create_heroic_style(name)
    
    def _create_classic_style(self, name: str) -> PlayerCharacter:
        """Cria personagem no estilo clássico"""
        print(f"\n--- Criando {name} no estilo CLÁSSICO ---")
        
        character = self.generator.generate_classic_character(name)
        
        print("\nAtributos gerados:")
        analysis = self.generator.analyze_attributes(character.attributes)
        for attr, desc in analysis.items():
            print(f"{attr}: {desc}")
        
        print(f"\nClasse recomendada: {character.character_class.name}")
        print("\nTodas as recomendações:")
        recommendations = self.generator.get_class_recommendations(character.attributes)
        for rec in recommendations:
            print(f"  {rec}")
        
        return character
    
    def _create_adventurer_style(self, name: str) -> PlayerCharacter:
        """Cria personagem no estilo aventureiro"""
        print(f"\n--- Criando {name} no estilo AVENTUREIRO ---")
        
        # Rola os valores
        values = self.generator.roll_attributes_for_style(GameStyle.AVENTUREIRO)
        print(f"\nValores rolados: {values}")
        
        # Distribui os atributos
        distribution = self._distribute_attributes(values)
        
        # Escolhe a classe
        temp_attrs = AttributeSet()
        for attr_type, value in distribution.items():
            temp_attrs.set_attribute(attr_type, value)
        
        char_class_name = self._choose_character_class(temp_attrs)
        
        return self.generator.generate_adventurer_character(name, distribution, char_class_name)
    
    def _create_heroic_style(self, name: str) -> PlayerCharacter:
        """Cria personagem no estilo heroico"""
        print(f"\n--- Criando {name} no estilo HEROICO ---")
        
        # Rola os valores
        values = self.generator.roll_attributes_for_style(GameStyle.HEROICO)
        print(f"\nValores rolados: {values}")
        
        # Distribui os atributos
        distribution = self._distribute_attributes(values)
        
        # Escolhe a classe
        temp_attrs = AttributeSet()
        for attr_type, value in distribution.items():
            temp_attrs.set_attribute(attr_type, value)
        
        char_class_name = self._choose_character_class(temp_attrs)
        
        return self.generator.generate_heroic_character(name, distribution, char_class_name)
    
    def _distribute_attributes(self, values: List[int]) -> Dict[AttributeType, int]:
        """Interface para distribuir atributos"""
        print("\nDistribua os valores pelos atributos:")
        
        attributes = list(AttributeType)
        distribution = {}
        available_values = values.copy()
        
        for i, attr_type in enumerate(attributes):
            print(f"\nValores disponíveis: {available_values}")
            print(f"Atributo: {attr_type.value}")
            
            while True:
                try:
                    choice = int(input("Escolha um valor: "))
                    if choice in available_values:
                        distribution[attr_type] = choice
                        available_values.remove(choice)
                        break
                    else:
                        print("Valor não disponível!")
                except ValueError:
                    print("Digite um número válido!")
        
        return distribution
    
    def _choose_character_class(self, attributes: AttributeSet) -> str:
        """Interface para escolher classe de personagem"""
        print("\nRecomendações de classe baseadas nos seus atributos:")
        recommendations = self.generator.get_class_recommendations(attributes)
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
        
        classes = list(self.generator.AVAILABLE_CLASSES.keys())
        
        while True:
            choice = input(f"\nEscolha uma classe (1-{len(classes)}): ").strip()
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(classes):
                    return classes[idx]
                else:
                    print("Escolha inválida!")
            except ValueError:
                print("Digite um número válido!")