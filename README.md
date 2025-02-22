[![author](https://img.shields.io/badge/author-Adilsong-red.svg)](https://www.linkedin.com/in/adilson-gustavo-marcondes-barreto-de-souza-a74b98133/) [![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-365/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

<h1 align="center">Calculadora de IMC</h1>

<sub>*Graduando em Ciência de Dados na Uninter e Cursando Mestres da Automação*</sub>

Este é um projeto simples de uma Calculadora de IMC (Índice de Massa Corporal) desenvolvida em Python utilizando a biblioteca PySimpleGUI para a interface gráfica.

<h2 align="left">Funções do Projeto:</h3>

<h3 align="left">Interface Gráfica:</h3>

A interface gráfica foi construída utilizando a biblioteca PySimpleGUI, permitindo uma experiência interativa e amigável para o usuário. Inclui campos para inserir o peso e a altura, onde o usuário pode digitar os valores e calcular o IMC com um clique no botão "Calcular IMC". Há validações para garantir que os campos não estejam em branco e que aceitem apenas números.

<h3 align="left">Cálculo do IMC:</h3>

O cálculo do IMC é realizado utilizando a fórmula padrão: IMC = peso / (altura * altura). Após calcular o IMC, o resultado é exibido na interface com duas casas decimais e colorido conforme a faixa de valores (gradiente de cores de acordo com o IMC).

<h3 align="left">Validações de Entrada:</h3>

Antes de calcular o IMC, o sistema verifica se os campos de peso e altura estão preenchidos. Valida também se os valores inseridos são numéricos e se a altura está dentro do intervalo aceitável (0.3 a 3.0 metros).

<h3 align="left">Imagem do Resultado:</h3>

![Exemplo da Interface Gráfica da Calculadora de IMC](demonstracao.png)