"""
Crie um programa em Python que receba do usuário dois números
inteiros positivos A e B (e garantindo que A < B), encontre e imprima os números
divisíveis por 5 no intervalo de números entre A e B (incluindo A e B) e a soma
dos números encontrados (Dica: usar "numero % 5 == 0" para achar os números divisíveis
por 5).
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo valor: "))
for i in range (num1, num2 + 1):
    if i % 5 == 0:
        print(f"{i}, ")