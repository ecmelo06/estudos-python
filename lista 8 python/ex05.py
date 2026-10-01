"""
Escreva um programa que possua dois vetores pré-preenchidos (A e B),
ambos de 10 posições. O programa deve fazer a multiplicação dos elementos de mesmo
índice em ambos os vetores e colocar o resultado no mesmo índice em um terceiro vetor
(C). Mostre o vetor C resultante.
"""

vetA = [8, 9 , 5, 3, 2, 11, 51, 9, 0, 3]
vetB = [9, 0, 5, 22, 31, 1, 2, 4, 12, 6]
vetC = [0] * 10


for i in range (len(vetA)):
    num = vetA[i]
    for j in range(len(vetB)):
        num2 = vetB[i]
    vetC[i] = num * num2
print(vetC)