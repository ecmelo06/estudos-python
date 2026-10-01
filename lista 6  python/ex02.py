"""
Escreva um programa em Python que imprima a seguinte sequência de
números: 44, 33, 22, 11, 0. REGRA: Você DEVE usar um laço 'while' e controlar a variável
manualmente (inicialização, teste de condição e atualização de -11). Não utilize o laço 'for'.
"""

result = -1
num = 44
decrement = 11

while result != 0:
    result = num - decrement
    num = result
    print(result)