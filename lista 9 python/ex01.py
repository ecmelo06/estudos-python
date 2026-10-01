"""
Faça um algoritmo que gere aleatoriamente uma matriz de inteiros 7 x 9,
imprima a matriz e calcule e imprima a soma dos seus elementos.
"""
import random

colunas = 7
linhas = 9
soma = 0
matriz = [0] * linhas
for i in range(linhas):
    for j in range(colunas):
        matriz[i] = [0] * colunas

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(1, 25)
        soma += matriz[i][j]


for i in range(linhas):
    for j in range(colunas):
        print(f"{matriz[i][j]:2}", end=" ")
    print()

print(f"A soma dos valores da matriz é: {soma}")
