import pytest
from dragon.core.style.classic import EstiloClassico
from dragon.core.style.adventory import EstiloAventureiro
from dragon.core.style.heroic import EstiloHeroico
from dragon.character.generator import GeradorPersonagem


def test_estilo_classico_gera_seis_atributos():
    estilo = EstiloClassico()
    valores = [10, 11, 12, 13, 14, 15]
    atributos = estilo.gerar_atributos(valores=valores)
    d = atributos.get_atributos_dict()
    assert len(d) == 6
    for v in d.values():
        assert 10 <= v <= 15

def test_estilo_aventureiro_gera_seis_atributos(monkeypatch):
    estilo = EstiloAventureiro()
    valores = [10, 11, 12, 13, 14, 15]
    distribuicao = [15, 14, 13, 12, 11, 10]
    atributos = estilo.gerar_atributos(distribuicao=distribuicao, valores=valores)
    d = atributos.get_atributos_dict()
    assert sorted(d.values()) == sorted([10, 11, 12, 13, 14, 15])

def test_estilo_heroico_gera_seis_atributos(monkeypatch):
    estilo = EstiloHeroico()
    valores = [14, 15, 16, 17, 18, 13]
    atributos = estilo.gerar_atributos(distribuicao=valores, valores=valores)
    d = atributos.get_atributos_dict()
    assert sorted(d.values()) == sorted([14, 15, 16, 17, 18, 13])

def test_gerador_personagem_escolher_estilo(monkeypatch):
    gerador = GeradorPersonagem()
    estilo = gerador.get_estilo(1)
    assert isinstance(estilo, EstiloClassico)
