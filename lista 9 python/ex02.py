"""
Dada uma matriz M[1..6][1..8] criada randomicamente, criar um vetor C que
contenha em cada posição a quantidade de elementos negativos da linha correspondente de
M. Tamanho de C igual ao número de linhas da matriz. Imprimir o vetor C ao final.
"""
import random

colunas = 6
linhas = 8
vetC = [0] * linhas

matriz = [0] * linhas
for i in range(linhas):
    for j in range(colunas):
        matriz[i] = [0] * colunas

num = 0
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(-30, 30)
        if matriz[i][j] < 0:
            num += 1

for i in range(linhas):
    for j in range(colunas):
        print(f"{matriz[i][j]:2}", end=" ")
    print()

print(f"A quantidade de numeros negativos dentro da matriz é: {num}")