from notas.aluno import Aluno
from notas.armazenamento import carregar, salvar


def test_roundtrip_salva_e_carrega(tmp_path):
    caminho = tmp_path / "turma.csv"
    turma = [Aluno("1", "Joao", 7, 8, 9), Aluno("2", "Maria")]

    salvar(turma, caminho)
    carregada = carregar(caminho)

    assert len(carregada) == 2
    assert carregada[0].nome == "Joao"
    assert carregada[0].nota1 == 7
    assert carregada[1].nota2 is None
    assert carregada[1].tem_todas_as_notas() is False


def test_carregar_arquivo_inexistente_devolve_lista_vazia(tmp_path):
    assert carregar(tmp_path / "nao_existe.csv") == []


def test_nomes_com_acentos_sobrevivem_utf8(tmp_path):
    caminho = tmp_path / "turma.csv"
    salvar([Aluno("1", "Joao da Silva")], caminho)
    assert carregar(caminho)[0].nome == "Joao da Silva"


def test_csv_tem_cabecalho(tmp_path):
    caminho = tmp_path / "turma.csv"
    salvar([], caminho)
    with open(caminho, encoding="utf-8") as arquivo:
        assert arquivo.readline().strip() == "matricula,nome,nota1,nota2,nota3"
