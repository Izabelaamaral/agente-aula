import builtins

import pytest

from notas import comandos
from notas.aluno import Aluno
from notas.interface import (
    despachar,
    formatar_aluno,
    formatar_tabela,
    menu,
    mostrar_menu,
)


def test_formatar_aluno_com_notas():
    linha = formatar_aluno(Aluno("1", "Ana", 7, 8, 9))
    assert "Ana" in linha
    assert "8.1" in linha
    assert "Aprovado" in linha


def test_formatar_aluno_sem_notas():
    linha = formatar_aluno(Aluno("1", "Ana"))
    assert "Ana" in linha
    assert "-" in linha


def test_formatar_tabela_vazia():
    assert "nenhum aluno" in formatar_tabela([]).lower()


def test_formatar_tabela_com_aluno():
    tabela = formatar_tabela([Aluno("1", "Ana", 7, 7, 7)])
    assert "Ana" in tabela
    assert "Aprovado" in tabela


def test_mostrar_menu(capsys):
    mostrar_menu()
    out = capsys.readouterr().out
    assert "Cadastrar" in out
    assert "Listar" in out
    assert "Salvar e sair" in out


def test_despachar_listar():
    turma = [Aluno("1", "Ana", 7, 7, 7)]
    assert "Ana" in despachar("2", turma)


def test_despachar_cadastrar():
    turma = []
    msg = despachar("1", turma, ("1", "Ana"))
    assert len(turma) == 1
    assert "cadastrado" in msg.lower()


def test_despachar_lancar_notas():
    turma = [Aluno("1", "Ana")]
    msg = despachar("3", turma, ("1", 7, 8, 9))
    assert comandos.buscar_aluno(turma, "1").nota1 == 7
    assert "8.1" in msg
    assert "Aprovado" in msg


def test_despachar_buscar():
    turma = [Aluno("1", "Ana", 7, 7, 7)]
    assert "Ana" in despachar("4", turma, ("1",))


def test_despachar_saida():
    assert despachar("5", [Aluno("1", "Ana")]) is None


def test_despachar_invalida():
    assert "invalida" in despachar("9", []).lower()


def test_despachar_duplicata_propaga_erro():
    turma = []
    despachar("1", turma, ("1", "Ana"))
    with pytest.raises(ValueError):
        despachar("1", turma, ("1", "Beto"))


def test_menu_fluxo_completo(monkeypatch, capsys, tmp_path):
    entradas = iter(["1", "1", "Ana", "2", "5"])
    monkeypatch.setattr(builtins, "input", lambda *a: next(entradas))
    turma = []
    menu(turma, caminho=tmp_path / "saida.csv")
    out = capsys.readouterr().out
    assert "cadastrado" in out.lower()
    assert "Ana" in out
    assert "Ate" in out
    assert "Ana" in (tmp_path / "saida.csv").read_text(encoding="utf-8")


def test_menu_fluxo_lancar_notas(monkeypatch, capsys, tmp_path):
    entradas = iter(["1", "1", "Ana", "3", "1", "7", "8", "9", "2", "5"])
    monkeypatch.setattr(builtins, "input", lambda *a: next(entradas))
    turma = []
    menu(turma, caminho=tmp_path / "saida.csv")
    out = capsys.readouterr().out
    assert "8.1" in out
    assert "Aprovado" in out


def test_main_inicia_e_sai(monkeypatch, capsys):
    import notas.__main__ as app
    import notas.interface as iface

    monkeypatch.setattr(app, "carregar", lambda: [])
    chamado = []
    monkeypatch.setattr(iface, "salvar", lambda turma, caminho=None: chamado.append(caminho))
    monkeypatch.setattr(builtins, "input", lambda *a: "5")

    app.main()

    out = capsys.readouterr().out
    assert "Ate" in out
    assert chamado
