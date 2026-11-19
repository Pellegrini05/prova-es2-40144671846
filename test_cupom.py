from cupom import desconto_valido


def test_aceita_percentual_no_limite():
    percentual = 26
    resultado = desconto_valido(percentual)
    assert resultado is True


def test_rejeita_percentual_acima_do_limite():
    percentual = 27
    resultado = desconto_valido(percentual)
    assert resultado is False


def test_rejeita_percentual_zero():
    percentual = 0
    resultado = desconto_valido(percentual)
    assert resultado is False
