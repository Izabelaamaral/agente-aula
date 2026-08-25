from notas.media import calcular_media, classificar_situacao


def test_media_ponderada_basica():
    assert calcular_media(7, 7, 7) == 7.0


def test_media_arredonda_uma_casa():
    assert calcular_media(7, 6, 5) == 5.9


def test_media_com_pesos_personalizados():
    assert calcular_media(10, 0, 0, pesos=(3, 0, 4)) == round(30 / 7, 1)


def test_situacao_aprovado_no_limite():
    assert classificar_situacao(7) == "Aprovado"
    assert classificar_situacao(7.0) == "Aprovado"


def test_situacao_exame():
    assert classificar_situacao(5) == "Exame"
    assert classificar_situacao(6.9) == "Exame"


def test_situacao_reprovado():
    assert classificar_situacao(4.9) == "Reprovado"
    assert classificar_situacao(4.0) == "Reprovado"
