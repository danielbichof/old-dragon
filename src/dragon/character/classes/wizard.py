from typing import List
from .IClasses import ICharacterClass
from dragon.character.data.live_dice import LiveDice
from dragon.character.data.arcade_school import ArcaneSchool

class Wizard(ICharacterClass):
    """Mago é um mestre da magia arcana."""

    def __init__(self, school: ArcaneSchool):
        self._school = school

    @property
    def name(self) -> str:
        return "Mago"

    @property
    def hit_die(self) -> LiveDice:
        return LiveDice.D6

    @property
    def skills(self) -> List[str]:
        return ["Arcana", "História", "Investigação"]

    @property
    def features(self) -> List[str]:
        return [f"Tradição Arcana ({self._school.name})", "Grimório"]

    @property
    def description(self) -> str:
        return (
            "Mestres da magia arcana, estudiosos que manipulam o tecido da realidade."
        )
