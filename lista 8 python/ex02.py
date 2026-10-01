"""
Preencher um vetor A de 10 posições (índices de 0 a 9) usando um laço de
repetição com os números inteiros 10, 20, 30, 40, 50, ..., 100. Escrever o vetor A após o
seu total preenchimento.
"""

x = [0] * 10
for i in range (len(x)):
    x[i] = (i + 1) * 10
    print(x[i])