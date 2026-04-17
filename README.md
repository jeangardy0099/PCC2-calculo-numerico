# PPC2 - Método de Bairstow

## Descrição

Este projeto implementa o método de Bairstow para determinação de raízes de polinômios de grau arbitrário, incluindo raízes reais e complexas.

O código também é aplicado ao polinômio característico obtido na APC2, permitindo a análise dos autovalores do sistema.

---

## Requisitos

- Python 3
- numpy
- matplotlib

Instalação das dependências:

pip install numpy matplotlib

---

## Como executar

1. Baixar ou clonar o repositório

git clone <link-do-repositorio>

2. Entrar na pasta do projeto

cd PPC2-Bairstow

3. Executar o código

python main.py

---

## O que o programa faz

Ao executar, o programa:

- Calcula as raízes de um polinômio de teste validação
- Calcula as raízes do polinômio da APC2
- Gera o fractal de convergência do método de Bairstow

Os resultados são exibidos no terminal e o gráfico do fractal é mostrado na tela.

---

## Reprodução dos resultados

Para reproduzir os resultados:

- Execute o arquivo main.py
- Utilize os coeficientes já definidos no código

Polinômio da APC2 utilizado:

P(λ) = λ⁴ + 4λ³ + 11λ² + 12λ + 12

---

## Observações

- O método foi implementado sem uso de bibliotecas prontas para cálculo de raízes
- O comportamento do método depende dos valores iniciais escolhidos




