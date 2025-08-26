from typing import List, Dict


class Atributos:
    """Classe para representar os seis atributos de um personagem"""

    def __init__(self):
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0

    def definir_atributos_em_ordem(self, valores: List[int]) -> None:
        """Define os atributos na ordem: Força, Destreza, Constituição, Inteligência, Sabedoria, Carisma"""
        if len(valores) != 6:
            raise ValueError("É necessário fornecer exatamente 6 valores")

        self.forca = valores[0]
        self.destreza = valores[1]
        self.constituicao = valores[2]
        self.inteligencia = valores[3]
        self.sabedoria = valores[4]
        self.carisma = valores[5]

    def definir_atributos_manual(
        self,
        forca: int,
        destreza: int,
        constituicao: int,
        inteligencia: int,
        sabedoria: int,
        carisma: int,
    ) -> None:
        """Define os atributos manualmente"""
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

    def get_atributos_dict(self) -> Dict[str, int]:
        """Retorna os atributos como dicionário"""
        return {
            "Força": self.forca,
            "Destreza": self.destreza,
            "Constituição": self.constituicao,
            "Inteligência": self.inteligencia,
            "Sabedoria": self.sabedoria,
            "Carisma": self.carisma,
        }

    def alterar_atributo(self, nome: str, delta: int):
        """Altera um atributo pelo nome adicionando delta (pode ser negativo).

        Ignora nomes inválidos silenciosamente.
        """
        mapping = {
            "Força": "forca",
            "Destreza": "destreza",
            "Constituição": "constituicao",
            "Inteligência": "inteligencia",
            "Sabedoria": "sabedoria",
            "Carisma": "carisma",
        }
        attr = mapping.get(nome)
        if attr and hasattr(self, attr):
            setattr(self, attr, getattr(self, attr) + delta)

    def __str__(self) -> str:
        """Representação em string dos atributos"""
        return f"""
Atributos do Personagem:
Força: {self.forca}
Destreza: {self.destreza}
Constituição: {self.constituicao}
Inteligência: {self.inteligencia}
Sabedoria: {self.sabedoria}
Carisma: {self.carisma}
"""
