# Calculadora de IMC — Projeto Acadêmico com Flet (Mobile/Desktop)

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
pip install flet
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
