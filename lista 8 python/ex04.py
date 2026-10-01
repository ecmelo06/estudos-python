"""
Escreva um programa que declare e inicialize diretamente no código
(estaticamente) um vetor de 20 posições contendo números inteiros. A seguir, usando um
laço de repetição, conte e diga quantos valores pares existem dentro deste vetor.
"""
vetor = [5, 12, 8, 23, 45, 6, 17, 32, 9, 11, 54, 2, 88, 14, 29, 77, 3, 21, 66, 40]
cont = 0
for i in range (len(vetor)):
    num = vetor[i]
    if num % 2 == 0:
        cont += 1
        print(vetor[i])
        
print(f"A quantidade de números pares dentro do vetor, é: {cont}.")