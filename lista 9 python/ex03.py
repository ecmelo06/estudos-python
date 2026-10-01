"""
Faça um algoritmo que gere randomicamente uma matriz de 5 X 5 de inteiros
positivos e mostre a soma de cada coluna separadamente.
"""
import random

linhas = 5
colunas = 5

matriz = [0] * linhas
for i in range(linhas):
    for j in range(colunas):
        matriz[i] = [0] * colunas

soma = 0
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(1, 15)
        soma += matriz[i][j]
    print(f"soma da linha {i+1} da matriz é {soma}")

for i in range(linhas):
    for j in range(colunas):
        print(f"{matriz[i][j]:2}", end=" ")
    print()