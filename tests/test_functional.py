import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from imc_logic import calcular_imc


def test_functional_underweight():
    imc, classificacao = calcular_imc(45, 1.70)
    assert classificacao == "Abaixo do peso"
    assert imc < 18.5
