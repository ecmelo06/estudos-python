"""
Preencher um vetor B de 10 posições usando um laço de repetição com o
número 10 se o índice do elemento for ímpar, e com o número 20 se o índice for par.
Escrever o vetor B após o seu total preenchimento.
"""

vetor = [0] * 10

for i in range (len(vetor)):
    if i % 2 == 0:
        vetor[i] = 20
        print(vetor[i])
    else:
        vetor[i] = 10
        print(vetor[i])