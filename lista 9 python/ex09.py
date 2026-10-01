"""
Faça um algoritmo que leia uma matriz 3x3 e após a leitura multiplique cada
elemento da diagonal principal pela média do valor de todos os elementos.
"""

import random

linhas = 3
colunas = 3
soma = 0
media = 0
somaD = 0
numD = 0
total = 0
matriz = [0] * linhas
for i in range(linhas):
    for j in range(colunas):
        matriz[i] = [0] * colunas

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(1, 10)
        soma += matriz[i][j]

media = float(soma) / linhas
for i in range(linhas):
    for j in range(colunas):
        if i == j:
            numD = matriz[i][j]
            print(f"{numD * media:.1f}")

for i in range(linhas):
    for j in range(colunas):
        print(f"{matriz[i][j]:2}", end=" ")
    print()

print(f"Media da matriz: {media:.1f}")