"""
Elaborar um algoritmo que leia uma matriz M[6][6] e um valor A, e que após
a leitura multiplique a matriz M pelo valor A e coloque os valores da matriz multiplicados por
A em um vetor V(36). Escrever o vetor V no final.
"""
import random
linhas = 6
colunas = 6
tamanho = linhas * colunas
vet = [0] * tamanho

num = int(input("Digite um valor: "))
matriz = [0] * linhas
for i in range (linhas):
    for j in range (colunas):
        matriz[i] = [0] * colunas

for i in range (linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(1, 10)
        vet[i * colunas + j] = matriz[i][j] * num
print(vet)

        