import sys
import os
import pytest

# Garantindo que a pasta raiz do projeto esteja no path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from imc_logic import calcular_imc, faixa_peso_ideal


def test_acceptance_normal_case():
    """
    Critério do cliente:
    Para um adulto de 70kg e 1.75m, o sistema deve retornar IMC ≈ 22.86
    e classificação "Peso normal", além de exibir a faixa de peso ideal.
    """
    imc, classificacao = calcular_imc(70, 1.75)
    faixa = faixa_peso_ideal(1.75)

    assert round(imc, 2) == 22.86
    assert classificacao == "Peso normal"
    assert faixa == pytest.approx((56.6, 76.2), rel=1e-2)
