<img width="912" height="260" alt="image" src="https://github.com/user-attachments/assets/3a528713-e728-456d-98aa-b2cd17b5dacb" />

# Calculadora de IMC — Projeto Acadêmico com Flet

Este projeto é uma **Calculadora de IMC** desenvolvida em **Python** utilizando o framework **Flet**, como parte de um **trabalho acadêmico**. A aplicação foi criada com foco em aprendizado prático, trazendo recursos visuais modernos, facilidade de uso e funções adicionais como **modo escuro** e **histórico de cálculos**.

---

## O que é o projeto?

O **IMC (Índice de Massa Corporal)** é uma medida que avalia se o peso está adequado à altura. Essa aplicação:

* Calcula o **IMC** a partir do peso e altura.
* Mostra a **classificação** do IMC (peso normal, sobrepeso, obesidade etc.).
* Exibe a **faixa de peso ideal** para a altura informada.
* Possui um **modo escuro** para melhor conforto visual.
* Registra um **histórico dos cálculos realizados**.

Além de servir como exemplo prático para **aprendizado em programação mobile com Python**, também é um projeto funcional e visualmente agradável.

---

## Passo a passo de criação

### 1. Preparação do ambiente

* Instalar Python (3.8 ou superior).
* Criar um ambiente virtual (opcional, mas recomendado).
* Instalar a biblioteca principal:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install flet-desktop
```

### 2. Estrutura inicial do app

* Criar um arquivo Python (ex.: `imc_app.py`).
* Importar o Flet (`import flet as ft`).
* Definir a função principal `main(page: ft.Page)`.
* Configurar título, fundo e cores iniciais.

### 3. Criando os campos de entrada

* Adicionar dois `TextField` para **peso** e **altura**.
* Definir ícones, validações e bordas com a cor predominante (laranja).

### 4. Implementando o cálculo do IMC

* Criar uma função `calcular_imc()` para:

  * Converter valores de peso e altura.
  * Calcular o IMC.
  * Exibir classificação e mensagem personalizada.
  * Mostrar a faixa de **peso ideal** (IMC entre 18.5 e 24.9).

### 5. Adicionando botões de ação

* **Calcular IMC**: executa o cálculo.
* **Limpar**: apaga os campos e resultados.

### 6. Função extra: modo escuro

* Criar a função `toggle_tema()` para alternar entre **tema claro** e **escuro**.
* Ajustar as cores do texto e fundo de acordo com o tema.
* Adicionar um botão com ícone para alternar facilmente.

### 7. Função extra: histórico de cálculos

* Criar uma `ListView` para registrar os cálculos anteriores.
* Cada cálculo feito é adicionado ao histórico.
* Adicionar botão para **limpar histórico**.

### 8. Layout final

* Centralizar todos os elementos usando `Column` e `Row`.
* Colocar título, subtítulo, campos, botões, resultado, peso ideal e histórico.

### 9. Execução do app

* No final do arquivo, chamar:

```python
flet run --web imc.py
```

## Funcionalidades implementadas

* **Calcular IMC** com classificação.
* **Exibir faixa de peso ideal**.
* **Limpar** campos com um clique.
* **Modo escuro** (alternância de tema claro/escuro).
* **Histórico de cálculos** com botão para limpar.
* Layout responsivo que funciona em desktop e mobile.

---

## Exemplos visuais

### Tela inicial

<img width="739" height="988" alt="image" src="https://github.com/user-attachments/assets/4326f8f7-d087-4dea-85b4-224a1d6d9d48" />


### Resultado do cálculo

<img width="739" height="991" alt="image" src="https://github.com/user-attachments/assets/72c10e89-8ab8-482a-863f-390ac07d7854" />


### Modo escuro

<img width="736" height="984" alt="image" src="https://github.com/user-attachments/assets/96e15139-11ee-4323-9234-21e7de2e9dbc" />

---

## Conclusão

Este projeto acadêmico mostra como é possível criar um **aplicativo completo em Python** usando **Flet**, explorando desde a interface gráfica até funcionalidades extras como **modo escuro** e **histórico**. Ele serve tanto como exemplo prático de programação quanto como ferramenta útil para cálculos de saúde.

Ao final, você terá uma calculadora de IMC funcional, bonita e responsiva — pronta para uso, apresentação acadêmica e futuras melhorias. 🚀

# Segunda parte do projeto 
### *Testes de Software (Explorando Testes de Software em Projetos de Desenvolvimento)*

🧪 Tipos de Testes no seu código
- 1️⃣ Testes Unitários

👉 O que são:
Testam funções pequenas e isoladas, verificando se a lógica matemática funciona corretamente.

👉 No meu código:
A parte que calcula o IMC e a faixa de peso ideal.

📄 Exemplo (tests/test_unit.py):

```
import sys, os, pytest
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
```
🔎 Aqui só testamos a matemática, sem abrir interface.

- 2️⃣ Testes de Integração
  
👉 O que são:
Verificam se várias funções trabalham juntas corretamente.

👉 No meu código:
Testar se o cálculo do IMC (função calcular_imc) funciona em conjunto com a faixa de peso ideal (faixa_peso_ideal).

📄 Exemplo (tests/test_integration.py):

```
from imc_logic import calcular_imc, faixa_peso_ideal

def test_integration_imc_and_faixa():
    imc, classificacao = calcular_imc(80, 1.80)
    faixa = faixa_peso_ideal(1.80)

    assert round(imc, 2) == 24.69
    assert classificacao == "Peso normal"
    assert faixa == pytest.approx((59.9, 80.6), rel=1e-2)
```

- 3️⃣ Testes de Sistema
- 
👉 O que são:
Testam o fluxo completo do sistema, como se fosse um usuário usando.

👉 No meu código:
Simular alguém digitando peso e altura, clicando em calcular e vendo o resultado + histórico.

📄 Exemplo (tests/test_system.py):
```
from imc_logic import calcular_imc, faixa_peso_ideal

def test_system_flow():
    # Usuário entra com dados
    peso, altura = 90, 1.75
    imc, classificacao = calcular_imc(peso, altura)
    faixa = faixa_peso_ideal(altura)

    # Esperado pelo sistema
    assert round(imc, 2) == 29.39
    assert classificacao == "Sobrepeso"
    assert faixa == pytest.approx((56.6, 76.2), rel=1e-2)
```

- 4️⃣ Testes de Aceitação
  
👉 O que são:
Validam os critérios do cliente/usuário final (ex.: “com 70kg e 1.75m deve dar Peso normal”).

👉 No meu código:
Critério: um adulto de 70kg e 1.75m deve ter IMC ≈ 22.86 → “Peso normal”.

📄 Exemplo (tests/test_acceptance.py):
```
from imc_logic import calcular_imc, faixa_peso_ideal
import pytest

def test_acceptance_normal_case():
    imc, classificacao = calcular_imc(70, 1.75)
    faixa = faixa_peso_ideal(1.75)

    assert round(imc, 2) == 22.86
    assert classificacao == "Peso normal"
    assert faixa == pytest.approx((56.6, 76.2), rel=1e-2)
```

- 5️⃣ Testes Funcionais
  
👉 O que são:
Testam o que o sistema deve fazer (função esperada).

👉 No meu código:
Garantir que pesos abaixo de 18.5 sempre retornam “Abaixo do peso”.

📄 Exemplo (tests/test_functional.py):
```
from imc_logic import calcular_imc

def test_functional_underweight():
    imc, classificacao = calcular_imc(45, 1.75)
    assert round(imc, 2) < 18.5
    assert classificacao == "Abaixo do peso"
```

- 6️⃣ Testes Não Funcionais

👉 O que são:
Avaliam desempenho, segurança, usabilidade.

👉 No meu código:
Podemos medir se o cálculo roda rápido, sem travar a interface.

📄 Exemplo (tests/test_nonfunctional.py):
```
import time
from imc_logic import calcular_imc

def test_nonfunctional_performance():
    start = time.time()
    for _ in range(100000):
        calcular_imc(70, 1.75)
    end = time.time()
    assert (end - start) < 1.0  # deve rodar em menos de 1 segundo
```

- 👉 Resumindo:

Unitário → testa uma função isolada (calcular_imc).

Integração → testa duas funções juntas (calcular_imc + faixa_peso_ideal).

Sistema → simula o fluxo completo.

Aceitação → valida o critério do cliente (IMC correto para caso real).

Funcional → verifica se as funções cumprem os requisitos (“peso < 18.5 → abaixo do peso”).

Não funcional → avalia desempenho (velocidade).
