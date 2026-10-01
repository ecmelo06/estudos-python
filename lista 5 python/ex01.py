"""
Crie um programa em Python que receba do usuário um número inteiro
positivo e informe os totais de números pares e ímpares encontrados entre 1 e o número
digitado + o somatório dos pares e ímpares separadamente.
"""
num = int(input("Digite um número: "))
n = num

contImp = 0
contPar = 0
i = 1
for i in range (i, n+1):
    if n % 2 == 0:
        contPar += 1
    if n % 2 == 1:
        contImp += 1
    n -= 1

print(f"De 1 a número {num}, existem {contPar} números pares e {contImp} números ímpares")