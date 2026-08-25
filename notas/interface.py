"""Interface textual (CLI).

Menu e formatacao de saida. A logica de negocio esta em `comandos` e a
persistencia em `armazenamento`. `despachar` recebe a opcao ja lida e devolve a
mensagem da acao; ela nao le entrada alguma, o que a torna testavel sem
simular input(). O loop com input() fica isolado e minimo em `menu`.
"""

from . import comandos
from .armazenamento import CAMINHO_PADRAO, salvar


def mostrar_menu():
    """Exibir o menu de opcoes disponiveis ao usuario."""
    print(" MENU DE NOTAS ".center(40, "="))
    print(" 1. Cadastrar aluno")
    print(" 2. Listar turma")
    print(" 3. Lancar notas")
    print(" 4. Buscar aluno")
    print(" 5. Salvar e sair")
    print(" 6. Remover aluno")
    print("=" * 40)


def _fmt_nota(nota):
    """Formatar uma nota para exibicao; trava vazia quando a nota e None."""
    return "-" if nota is None else f"{nota:.1f}"


def formatar_aluno(aluno):
    """Formatar um unico aluno como uma linha de texto."""
    media = "-" if aluno.media is None else f"{aluno.media:.1f}"
    situacao = "-" if aluno.situacao is None else aluno.situacao
    return (
        f"{aluno.matricula:<10} {aluno.nome:<25} "
        f"N1={_fmt_nota(aluno.nota1)} N2={_fmt_nota(aluno.nota2)} "
        f"N3={_fmt_nota(aluno.nota3)} | Media: {media} | {situacao}"
    )


def formatar_tabela(turma):
    """Montar a tabela textual da turma inteira."""
    borda = "=" * 78
    linhas = [borda, "TABELA DA TURMA", borda]
    if not turma:
        linhas.append("(nenhum aluno cadastrado)")
    for aluno in turma:
        linhas.append(formatar_aluno(aluno))
    linhas.append(borda)
    return "\n".join(linhas)


def despachar(opcao, turma, entrada=None):
    """Executar a acao da opcao ja lida e devolver a mensagem para o usuario.

    Parameters
    ----------
    opcao : str
        Opcao digitada ('1' a '6').
    turma : list[Aluno]
        Turma em memoria.
    entrada : tuple, opcional
        Dados ja coletados (matricula/nome/notas), quando necessario.

    Returns
    -------
    str | None
        Mensagem a exibir; None encerra o programa.
    """
    opcao = opcao.strip()
    if opcao == "1":
        matricula, nome = entrada
        aluno = comandos.cadastrar_aluno(turma, matricula, nome)
        return f"Aluno '{aluno.nome}' (matricula {aluno.matricula}) cadastrado."
    if opcao == "2":
        return formatar_tabela(turma)
    if opcao == "3":
        matricula, n1, n2, n3 = entrada
        aluno = comandos.lancar_notas(turma, matricula, n1, n2, n3)
        return (
            f"Notas lancadas para '{aluno.nome}' ({aluno.matricula}). "
            f"Media: {aluno.media}. Situacao: {aluno.situacao}"
        )
    if opcao == "4":
        (matricula,) = entrada
        return formatar_aluno(comandos.buscar_aluno(turma, matricula))
    if opcao == "5":
        return None
    if opcao == "6":
        (matricula,) = entrada
        aluno = comandos.remover_aluno(turma, matricula)
        return f"Aluno '{aluno.nome}' (matricula {aluno.matricula}) removido."
    return "Opcao invalida. Tente novamente."


def _coletar(opcao):
    """Coletar, via input(), os dados necessarios para a opcao informada."""
    if opcao == "1":
        return (input("Matricula: ").strip(), input("Nome: ").strip())
    if opcao == "3":
        matricula = input("Matricula: ").strip()
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        n3 = float(input("Nota 3: "))
        return (matricula, n1, n2, n3)
    if opcao == "4":
        return (input("Matricula: ").strip(),)
    if opcao == "6":
        return (input("Matricula: ").strip(),)
    return None


def menu(turma, caminho=None):
    """Loop principal: exibir menu, ler a opcao e despachar, ate sair.

    Parameters
    ----------
    turma : list[Aluno]
        Turma carregada em memoria.
    caminho : Path, opcional
        Onde salvar (padrao: alunos.csv).
    """
    destino = caminho or CAMINHO_PADRAO
    while True:
        mostrar_menu()
        try:
            opcao = input("Opcao: ").strip()
            entrada = _coletar(opcao)
            msg = despachar(opcao, turma, entrada)
        except ValueError as erro:
            print(f"Erro: {erro}")
            continue
        if msg is not None:
            print(msg)
        if opcao == "5":
            salvar(turma, destino)
            print("Dados salvos. Ate logo!")
            break
        if opcao in ("1", "3", "6"):
            salvar(turma, destino)
