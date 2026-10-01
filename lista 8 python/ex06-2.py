"""
(ExeVetor06) Escreva um programa que declare e inicialize diretamente no código um
vetor de 10 posições contendo números inteiros (positivos e negativos). O programa deve
mostrar somente os números positivos acompanhados de suas respectivas posições
(índices).
"""
import random
vet = [0] * 10
posi = 0
for i in range(len(vet)):
    vet[i] = random.randint(-100, 100)
    posi = i
    if vet[i] > 0:
        
        print(f"O número positivo {vet[i]} se encontra no índice: {posi}")