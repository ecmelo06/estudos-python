"""
Faça um algoritmo que calcule a média dos elementos da diagonal principal
de uma matriz 10X10 de inteiros.
"""
import random

linhas = 10
colunas = 10
somaD = 0
media = 0
matriz = [0] * linhas
for i in range(linhas):
    for j in range (colunas):
        matriz[i] = [0] * colunas

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(1, 10)
        if i == j:
            somaD += matriz[i][j]
            

for i in range(linhas):
    for j in range(colunas):
        print(f"{matriz[i][j]:2}", end=" ")
    print()

media = somaD / linhas
print(somaD)
print(media)