import pytest

from notas.aluno import Aluno
from notas.comandos import (
    buscar_aluno,
    cadastrar_aluno,
    existe_matricula,
    lancar_notas,
)


def test_cadastrar_aluno_adiciona_na_turma():
    turma = []
    aluno = cadastrar_aluno(turma, "1", "Ana")
    assert len(turma) == 1
    assert turma[0] is aluno


def test_matricula_duplicada_gera_erro():
    turma = [Aluno("1", "Ana")]
    with pytest.raises(ValueError):
        cadastrar_aluno(turma, "1", "Beto")


def test_existe_matricula():
    turma = [Aluno("1", "Ana")]
    assert existe_matricula(turma, "1") is True
    assert existe_matricula(turma, "2") is False


def test_buscar_aluno_encontrado():
    turma = [Aluno("1", "Ana"), Aluno("2", "Beto")]
    assert buscar_aluno(turma, "2").nome == "Beto"


def test_buscar_aluno_nao_encontrado():
    with pytest.raises(ValueError):
        buscar_aluno([], "x")


def test_lancar_notas_atualiza_e_classifica():
    turma = [Aluno("1", "Ana")]
    aluno = lancar_notas(turma, "1", 7, 8, 9)
    assert aluno.nota1 == 7
    assert aluno.media == 8.1
    assert aluno.situacao == "Aprovado"


def test_lancar_notas_aluno_inexistente():
    with pytest.raises(ValueError):
        lancar_notas([], "x", 1, 2, 3)
