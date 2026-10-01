"""
Escreva um programa que crie, em tempo de compilação, 2 vetores (A e B)
de 10 elementos inteiros cada. Após isso, o programa deverá criar um terceiro vetor (C),
de 20 posições, que seja a união dos dois primeiros, ou seja, as primeiras 10 posições de
C recebem o vetor A, e as últimas 10 recebem o vetor B. Mostre o vetor resultante.
"""
import random

tamanho = 10
vetA = [0] * tamanho
vetB = [0] * tamanho
vetC = [0] * 20

for i in range(tamanho):
    vetA[i] = random.randint(1, 20)
    vetB[i] = random.randint(1, 20)

vetC = vetA + vetB
print(vetC)