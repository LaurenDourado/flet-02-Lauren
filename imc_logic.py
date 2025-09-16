# imc_logic.py

def calcular_imc(peso: float, altura: float):
    """Retorna o IMC e a classificação correspondente."""
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero")

    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 24.9:
        classificacao = "Peso normal"
    elif imc < 29.9:
        classificacao = "Sobrepeso"
    elif imc < 34.9:
        classificacao = "Obesidade grau I"
    elif imc < 39.9:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"

    return imc, classificacao


def faixa_peso_ideal(altura: float):
    """Retorna a faixa de peso ideal (mínimo, máximo) para a altura fornecida."""
    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero")

    min_peso = 18.5 * (altura ** 2)
    max_peso = 24.9 * (altura ** 2)
    return round(min_peso, 1), round(max_peso, 1)
