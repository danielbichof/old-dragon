from typing import Dict, List, Optional, Tuple
from dragon.character.generator import GeradorPersonagem
from dragon.character.races.human import Human
from dragon.character.races.elf import Elf
from dragon.character.races.dwarf import Dwarf
from dragon.character.races.halfling import Halfling
from dragon.character.classes.figher import Fighter
from dragon.character.classes.barbarian import Barbarian
from dragon.character.classes.wizard import Wizard
from dragon.character.classes.scholar import Scholar
from dragon.character.data.combat_style import CombatStyle
from dragon.character.data.arcade_school import ArcaneSchool
from dragon.domain.personagem import Personagem


class CharacterService:
    def __init__(self) -> None:
        self.gerador = GeradorPersonagem()

    def get_estilos(self) -> Dict[int, str]:
        return {
            1: self.gerador.get_estilo(1).get_nome_estilo(),
            2: self.gerador.get_estilo(2).get_nome_estilo(),
            3: self.gerador.get_estilo(3).get_nome_estilo(),
        }

    def get_racas(self) -> List[Tuple[str, str]]:
        return [
            ("Human", "Humano"),
            ("Elf", "Elfo"),
            ("Dwarf", "Anão"),
            ("Halfling", "Halfling"),
        ]

    def get_classes(self) -> List[Tuple[str, str]]:
        return [
            ("Barbarian", "Bárbaro"),
            ("Fighter", "Guerreiro"),
            ("Wizard", "Mago"),
            ("Scholar", "Acadêmico"),
        ]

    def get_fighter_estilos(self) -> List[CombatStyle]:
        return [
            CombatStyle("Defesa", "Aumenta a CA em +1", {"CA": 1}),
            CombatStyle("Armas Grandes", "+2 dano com armas de 2 mãos", {"Dano": 2}),
        ]

    def get_wizard_escolas(self) -> List[ArcaneSchool]:
        return [
            ArcaneSchool("Evocação", "Especialista em dano", ["Mísseis Mágicos"]),
            ArcaneSchool("Abjuração", "Proteção e defesa", ["Armadura Arcana"]),
        ]

    def gerar_valores(self, estilo_num: int) -> Optional[List[int]]:
        estilo = self.gerador.get_estilo(estilo_num)
        return estilo.gerar_valores() if hasattr(estilo, "gerar_valores") else None

    def gerar_atributos(
        self,
        estilo_num: int,
        distribuicao: Optional[List[int]],
        valores: Optional[List[int]],
    ):
        return self.gerador.gerar_personagem(
            estilo_num=estilo_num, distribuicao=distribuicao, valores=valores
        )

    def build_raca(
        self, key: str, bonus1: Optional[str] = None, bonus2: Optional[str] = None
    ):
        if key == "Human":
            return Human([bonus1, bonus2])
        if key == "Elf":
            return Elf()
        if key == "Dwarf":
            return Dwarf()
        return Halfling()

    def build_classe(
        self,
        key: str,
        fighter_estilos: List[CombatStyle],
        wizard_escolas: List[ArcaneSchool],
        fighter_style_name: Optional[str],
        wizard_school_name: Optional[str],
    ):
        if key == "Fighter":
            chosen = next(
                (c for c in fighter_estilos if c.name == fighter_style_name),
                fighter_estilos[0],
            )
            return Fighter(chosen)
        if key == "Wizard":
            chosen = next(
                (s for s in wizard_escolas if s.name == wizard_school_name),
                wizard_escolas[0],
            )
            return Wizard(chosen)
        if key == "Barbarian":
            return Barbarian()
        return Scholar()

    def montar_personagem(
        self,
        estilo_num: int,
        distribuicao: Optional[List[int]],
        valores: Optional[List[int]],
        raca_key: str,
        bonus1: Optional[str],
        bonus2: Optional[str],
        classe_key: str,
        fighter_style_name: Optional[str],
        wizard_school_name: Optional[str],
    ) -> Personagem:
        atributos = self.gerar_atributos(estilo_num, distribuicao, valores)
        d = atributos.get_atributos_dict()

        rac = self.build_raca(raca_key, bonus1, bonus2)
        classe = self.build_classe(
            classe_key,
            self.get_fighter_estilos(),
            self.get_wizard_escolas(),
            fighter_style_name,
            wizard_school_name,
        )

        return Personagem(
            atributos=d,
            raca=rac.name,
            raca_bonus=rac.ability_bonuses,
            classe=classe.name,
            hit_die=classe.hit_die.value,
            skills=classe.skills,
            features=classe.features,
        )
