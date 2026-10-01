"""
(ExeVetor06) Escreva um programa que declare e inicialize diretamente no código um
vetor de 10 posições contendo números inteiros (positivos e negativos). O programa deve
mostrar somente os números positivos acompanhados de suas respectivas posições
(índices).
"""

vet = [-99, -4, 88, 23, 0, 1, -8, -1, 12, 100]
posi = 0
for i in range(len(vet)):
    posi = i
    num = vet[i]
    if num > 0:
        
        print(f"O número positivo {num} se encontra no índice: {posi}")