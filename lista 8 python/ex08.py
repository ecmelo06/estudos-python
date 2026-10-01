"""
Ler um vetor M de 10 elementos (solicite ao usuário que digite os 10 valores
inteiros) e imprima a lista original. A seguir, troque fisicamente na memória o valor do 1o
elemento (índice 0) com o 6o (índice 5), o 2o com o 7o, e assim por diante até o 5o com
10o. Escreva o vetor M após a modificação.
"""

vetor = [0] * 10

for i in range(len(vetor)):
    num = int(input("Digite um valor inteiro: "))
    vetor[i] = num

print(f"{vetor}")

for j in range(5):
    temp = vetor[j]
    vetor[j] = vetor[j + 5] 
    vetor[j + 5] = temp
print(vetor)