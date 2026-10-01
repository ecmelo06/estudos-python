"""
Faça um programa que declare e preencha (via teclado ou código) dois
vetores (A e B) de 30 posições cada. Crie um terceiro vetor (C) também de 30 posições
com a intersecção dos dois primeiros, isto é, coloque em C apenas os elementos que
existem tanto no vetor A quanto no vetor B (sem repetições). Mostre o vetor C.
"""

import random
tamanho = 30
vetA = [0] * tamanho
vetB = [0] * tamanho
vetC = [0] * tamanho
cont = 0

for i in range(tamanho):
    vetA[i] = random.randint(1, 100)
for j in range(tamanho):
    vetB[j] = random.randint(1, 100)
        
for k in vetA:
    if k in vetB:
        if k != vetC:
           vetC[cont] = k
           cont += 1
           if k in vetC:
            continue
print(vetA)
print(vetB)
print(vetC)