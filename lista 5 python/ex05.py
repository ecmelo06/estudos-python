"""
Escreva um programa em Python que receba um número e faça a tabuada
desse número de 1 a 10. Parar o algoritmo quando o usuário digitar um número negativo.
"""

num = int(input("Digite um número e saiba sua tabuada: "))

if num < 0:
    print("Número inválido.")
else: 
     for i in range (1, 11):
            result = i * num
            print(f"{num} x {i} = {result}")

'''
while num >= 0:
    for i in range (1, 11):
           result = i * num
           print(f"{num} x {i} = {result}")
    if i == 10:
        break
'''
