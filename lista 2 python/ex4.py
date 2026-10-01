"""
Construa um programa em Python para ler dois valores e mostrar o
menor deles. (DICA: Usar if/else para mostrar o menor dos valores digitados)
"""

n1 = int(input("Digite o valor 1: "))
n2 = int(input("Digite o valor 2: "))

if n1 < n2:
    print(f"O valor numero 1: {n1}, é menor que o valor 2: {n2}")
elif n2 < n1:
    print(f"O valor numero 2: {n2}, é menor que o valor 1: {n1}")
else: 
    print(f"Os dois valores são iguais")