from typing import List, Dict
from .base import Race, Size

class Human(Race):
    """Humanos são os mais adaptáveis e ambiciosos entre os povos civilizados.

    Atributos: +1 em dois atributos à escolha.
    Tamanho: Médio. Deslocamento: 9m. Idiomas: Comum e outro à escolha.
    Características Especiais: Versatilidade Humana (talento extra no 1º nível).
    """

    def __init__(self, bonus_choices: List[str]):
        if len(bonus_choices) != 2 or len(set(bonus_choices)) != 2:
            raise ValueError("Humanos devem escolher dois atributos diferentes para +1")
    self._bonus_choices = bonus_choices
    # Metadados
    self.darkvision = 0
    self.alignment = "Qualquer"
    self.height_cm = 170
    self.traits = ["Versatilidade Humana"]
    self.languages_extra = 1  # outro idioma à escolha

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
        # Mantém string original para compatibilidade com testes
        return ["Versatilidade Humana"]

    @property
    def description(self) -> str:
        return (
            "Os humanos sobrevivem e prosperam em qualquer ambiente, exibindo vasta diversidade "
            "cultural e presença em todo o mundo."
        )
