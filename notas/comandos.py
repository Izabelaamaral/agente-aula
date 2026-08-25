"""Regras de negocio sobre a turma (sem acesso a arquivos).

Recebem a turma (lista de Aluno) em memoria e operam sobre ela.
Matricula duplicada ou aluno inexistente geram ValueError.
"""

from .aluno import Aluno


def existe_matricula(turma, matricula):
    """Verificar se uma matricula ja esta cadastrada na turma."""
    return any(a.matricula == matricula for a in turma)


def buscar_aluno(turma, matricula):
    """Buscar um aluno pela matricula; gerar erro se nao encontrado."""
    for aluno in turma:
        if aluno.matricula == matricula:
            return aluno
    raise ValueError(f"Aluno com matricula '{matricula}' nao encontrado.")


def cadastrar_aluno(turma, matricula, nome):
    """Cadastrar um novo aluno; erro se a matricula ja existir.

    Returns
    -------
    Aluno
        O aluno recem-cadastrado.
    """
    if existe_matricula(turma, matricula):
        raise ValueError(f"Matricula '{matricula}' ja cadastrada.")
    aluno = Aluno(matricula, nome)
    turma.append(aluno)
    return aluno


def lancar_notas(turma, matricula, nota1, nota2, nota3):
    """Lancar as tres notas de um aluno ja cadastrado.

    Returns
    -------
    Aluno
        O aluno com as notas atualizadas.
    """
    aluno = buscar_aluno(turma, matricula)
    aluno.nota1 = nota1
    aluno.nota2 = nota2
    aluno.nota3 = nota3
    return aluno


def remover_aluno(turma, matricula):
    """Remover um aluno da turma; gerar erro se nao encontrado.

    Returns
    -------
    Aluno
        O aluno removido.
    """
    aluno = buscar_aluno(turma, matricula)
    turma.remove(aluno)
    return aluno

