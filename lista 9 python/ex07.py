"""
Escreva um algoritmo que leia uma matriz M[5][5] e que calcule e imprima
as somas:
a) da linha 4 de M.
b) da coluna 2 de M.
c) da diagonal principal (une o canto superior esquerdo ao canto inferior direito da
matriz quadrada).
d) todos os elementos da matriz M.
Escrever também a matriz.
Dica para calcular a diagonal principal
        if(i == j){
        soma += matrizM[i][j];
        }
"""

import random

linhas = 5
colunas = 5
somaColuna = 0
somaLinha = 0
somaDP = 0
somaT = 0
matriz = [0] * linhas
for i in range (linhas):
    for j in range(colunas):
        matriz[i] = [0] * colunas

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(1, 10)
        if i == 3:
            somaLinha += matriz[i][j]
        if j == 1:
            somaColuna += matriz[i][j]
        if i == j:
            somaDP += matriz[i][j]
        somaT += matriz[i][j]
        

for i in range(linhas):
    for j in range(colunas):
        print(f"{matriz[i][j]:2}", end=" ")
    print()

print(somaLinha)
print(somaColuna)
print(somaDP)
print(somaT)