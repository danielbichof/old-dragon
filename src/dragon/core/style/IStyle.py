class EstiloRolagem(ABC):
    """Classe abstrata para diferentes estilos de rolagem"""

    @abstractmethod
    def gerar_atributos(self) -> Atributos:
        """Método abstrato para gerar atributos"""
        pass

    @abstractmethod
    def get_nome_estilo(self) -> str:
        """Retorna o nome do estilo de rolagem"""
        pass

    @abstractmethod
    def get_descricao(self) -> str:
        """Retorna a descrição do estilo de rolagem"""
        pass
