"""
Escreva um programa que declare e inicialize diretamente no código
(estaticamente) um vetor de 20 posições contendo números inteiros. A seguir, usando um
laço de repetição, conte e diga quantos valores pares existem dentro deste vetor.
"""
import random
tamanho = 20
vetor = [0] * tamanho
cont = 0
for i in range (len(vetor)):
    vetor[i] = random.randint(1, 50)
    num = vetor[i]
    if num % 2 == 0:
        cont += 1
        print(vetor[i])
        
print(f"A quantidade de números pares dentro do vetor, é: {cont}.")