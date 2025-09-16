import sys, os, time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from imc_logic import calcular_imc


def test_nonfunctional_performance():
    """Teste não funcional: verificar tempo de execução (desempenho)"""
    start = time.time()
    for _ in range(100000):
        calcular_imc(70, 1.75)
    end = time.time()

    # O cálculo deve ser muito rápido (menos de 1 segundo para 100k execuções)
    assert (end - start) < 1
