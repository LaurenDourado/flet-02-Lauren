import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from imc_logic import calcular_imc, faixa_peso_ideal


def test_integration_imc_and_faixa():
    peso = 80
    altura = 1.80
    imc, classificacao = calcular_imc(peso, altura)
    min_p, max_p = faixa_peso_ideal(altura)

    assert imc > 0
    assert classificacao in ["Peso normal", "Sobrepeso", "Obesidade grau I", "Abaixo do peso", "Obesidade grau II", "Obesidade grau III"]
    assert min_p < peso < max_p or classificacao != "Peso normal"
