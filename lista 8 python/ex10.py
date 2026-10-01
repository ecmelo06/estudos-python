"""
Escreva um programa que leia diversos números inteiros fornecidos pelo
usuário e distribua esses valores entre dois vetores: o vetor_impares e o vetor_pares. Cada
um terá o tamanho fixo de 10 posições. A repetição do algoritmo se dará até que o usuário

digite o número zero (0) ou até que um dos vetores tenha sido totalmente preenchido.
Mostre o conteúdo válido dos dois vetores no final.
"""

vetPar = [0] * 10
vetImpar = [0] * 10
contPar = 0
contImpar = 0
num = int(input("Digite um valor: "))
while num != 0:
    if num % 2 == 0:
        vetPar[contPar] = num
        contPar += 1
        if (contPar >= 10):
            break
        
    elif num % 2 == 1:
        vetImpar[contImpar] = num
        contImpar +=1
        if (contImpar >= 10):
            break
    num = int(input("Digite um valor: "))

print(vetImpar)
print(vetPar)