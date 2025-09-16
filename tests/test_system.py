import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from imc_logic import calcular_imc, faixa_peso_ideal


def test_system_flow():
    # Simulação do fluxo completo
    peso = 95
    altura = 1.70

    imc, classificacao = calcular_imc(peso, altura)
    min_p, max_p = faixa_peso_ideal(altura)

    assert isinstance(imc, float)
    assert isinstance(classificacao, str)
    assert isinstance(min_p, float)
    assert isinstance(max_p, float)
    assert imc > 0
