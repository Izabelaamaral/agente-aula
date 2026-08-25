"""Persistencia dos dados da turma em CSV local.

Conventions (veja AGENTS.md): encoding="utf-8", newline="", arquivo na raiz.
Notas ainda nao lancadas (None) ficam como campos vazios no CSV.
"""

import csv
from pathlib import Path

from .aluno import Aluno

CAMINHO_PADRAO = Path("alunos.csv")
CABECALHO = ["matricula", "nome", "nota1", "nota2", "nota3"]


def _nota_para_str(nota):
    """Converter uma nota (float|None) para o texto gravado no CSV."""
    return "" if nota is None else str(nota)


def _str_para_nota(texto):
    """Converter o texto do CSV de volta para float|None."""
    return None if texto == "" else float(texto)


def salvar(turma, caminho=CAMINHO_PADRAO):
    """Gravar a turma inteira no CSV (sobrescrevendo o arquivo)."""
    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CABECALHO)
        escritor.writeheader()
        for aluno in turma:
            escritor.writerow(
                {
                    "matricula": aluno.matricula,
                    "nome": aluno.nome,
                    "nota1": _nota_para_str(aluno.nota1),
                    "nota2": _nota_para_str(aluno.nota2),
                    "nota3": _nota_para_str(aluno.nota3),
                }
            )


def carregar(caminho=CAMINHO_PADRAO):
    """Carregar a turma a partir do CSV; retornar lista vazia se nao existir."""
    if not caminho.exists():
        return []
    turma = []
    with open(caminho, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            turma.append(
                Aluno(
                    linha["matricula"],
                    linha["nome"],
                    _str_para_nota(linha["nota1"]),
                    _str_para_nota(linha["nota2"]),
                    _str_para_nota(linha["nota3"]),
                )
            )
    return turma
