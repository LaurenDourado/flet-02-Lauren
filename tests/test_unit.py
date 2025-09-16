import sys
import os
import pytest

# Garantindo que a pasta raiz do projeto esteja no path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from imc_logic import calcular_imc, faixa_peso_ideal


def test_calculo_imc_normal():
    imc, classificacao = calcular_imc(70, 1.75)
    assert round(imc, 2) == 22.86
    assert classificacao == "Peso normal"


def test_faixa_peso_ideal():
    min_p, max_p = faixa_peso_ideal(1.75)
    assert min_p == pytest.approx(56.6, rel=1e-2)
    assert max_p == pytest.approx(76.2, rel=1e-2)
