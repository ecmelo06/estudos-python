"""
Faça um algoritmo que gere randomicamente uma matriz de 10 X 10 de
inteiros. Calcule e mostre a soma das linhas pares da matriz.
"""
import random
linhas = 10
colunas = 10

matriz = [0] * linhas
for i in range (linhas):
    for j in range(colunas):
        matriz[i] = [0] * colunas

soma = 0
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(1, 10)
        if i % 2 == 0:
            soma += matriz[i][j]


for i in range(linhas):
    for j in range(colunas):
        print(f"{matriz[i][j]:2}", end=" ")
    print()
print(f"Soma total de todas as linhas pares da matriz é: {soma}")