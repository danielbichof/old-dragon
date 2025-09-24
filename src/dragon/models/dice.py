from random import randint


class Dado:
    """Classe responsável por simular rolagens de dados"""

    @staticmethod
    def rolar_d6() -> int:
        """Rola um dado de 6 faces"""
        return randint(1, 6)

    @staticmethod
    def rolar_3d6() -> int:
        """Rola 3 dados de 6 faces e soma o resultado"""
        return sum(Dado.rolar_d6() for _ in range(3))

    @staticmethod
    def rolar_4d6_eliminar_menor() -> int:
        """Rola 4 dados de 6 faces e elimina o menor, somando os 3 maiores"""
        rolagens = [Dado.rolar_d6() for _ in range(4)]
        rolagens.remove(min(rolagens))  # Remove o menor valor
        return sum(rolagens)
