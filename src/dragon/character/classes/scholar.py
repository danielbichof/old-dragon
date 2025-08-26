
from typing import List
from IClasses import ICharacterClass
from dragon.character.data.live_dice import LiveDice


class Scholar(ICharacterClass):
    """Acadêmico é um estudioso versátil."""

    @property
    def name(self) -> str:
        return "Acadêmico"

    @property
    def hit_die(self) -> LiveDice:
        return LiveDice.D8

    @property
    def skills(self) -> List[str]:
        return ["Investigação", "História", "Diplomacia"]

    @property
    def features(self) -> List[str]:
        return ["Conhecimento Acadêmico", "Versatilidade"]

    @property
    def description(self) -> str:
        return "Estudioso e versátil, combina conhecimento com habilidades úteis fora e dentro do combate."
