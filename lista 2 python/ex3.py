"""
Construa um programa em Python para ler dois valores e mostrar o maior
deles. (DICA: Usar if/else para mostrar o maior dos valores digitados)
"""

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 > n2:
    print(f"O valor 1: {n1} é maior que o valor 2: {n2}")
elif n2 > n1:
    print(f"O valor 2: {n2} é maior que o valor 1: {n1}")
else:
    print(f"Os dois valores são iguais")