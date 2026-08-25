"""Calculo de media ponderada e classificacao da situacao.

Regras (fixas pela especificacao da disciplina):
- tres avaliacoes com pesos 3, 3 e 4.
- media ponderada arredondada em uma casa decimal.
- situacao: >= 7 aprovado, >= 5 e < 7 exame, < 5 reprovado.
"""

PESOS = (3, 3, 4)


def calcular_media(nota1, nota2, nota3, pesos=PESOS):
    """Calcular a media ponderada das tres notas (uma casa decimal).

    Parameters
    ----------
    nota1, nota2, nota3 : float
        Notas das tres avaliacoes.
    pesos : tuple[int, int, int], opcional
        Pesos das avaliacoes (3, 3, 4) por padrao.

    Returns
    -------
    float
        Media ponderada arredondada em uma casa decimal.
    """
    p1, p2, p3 = pesos
    numerador = nota1 * p1 + nota2 * p2 + nota3 * p3
    denominador = p1 + p2 + p3
    return round(numerador / denominador, 1)


def classificar_situacao(media):
    """Classificar a situacao do aluno a partir da media.

    Returns
    -------
    str
        'Aprovado' se media >= 7, 'Exame' se 5 <= media < 7, 'Reprovado' se < 5.
    """
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Exame"
    return "Reprovado"
