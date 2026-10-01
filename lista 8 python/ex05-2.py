"""
Escreva um programa que possua dois vetores pré-preenchidos (A e B),
ambos de 10 posições. O programa deve fazer a multiplicação dos elementos de mesmo
índice em ambos os vetores e colocar o resultado no mesmo índice em um terceiro vetor
(C). Mostre o vetor C resultante.
"""
import random
tamanho = 10

vetA = [0] * tamanho
vetB = [0] * tamanho
vetC = [0] * tamanho

for i in range(tamanho):
    vetA[i] = random.randint(1, 10)
    vetB[i] = random.randint(1, 10)

    vetC[i] = vetA[i] * vetB[i]

print(vetC)