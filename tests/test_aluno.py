from notas.aluno import Aluno


def test_aluno_sem_notas_inicia_com_none():
    aluno = Aluno("1", "Ana")
    assert aluno.nota1 is None
    assert aluno.nota2 is None
    assert aluno.nota3 is None


def test_media_e_situacao_sao_nulas_sem_notas():
    aluno = Aluno("1", "Ana")
    assert aluno.media is None
    assert aluno.situacao is None
    assert aluno.tem_todas_as_notas() is False


def test_media_e_situacao_com_notas():
    aluno = Aluno("1", "Ana", 7, 8, 9)
    assert aluno.media == 8.1
    assert aluno.situacao == "Aprovado"
    assert aluno.tem_todas_as_notas() is True
