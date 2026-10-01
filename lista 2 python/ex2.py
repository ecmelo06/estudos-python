"""
Construa um programa em Python para ler um valor, verificar se é par ou
ímpar e mostrar essa informação. (DICA: Usar if/else e o operador aritmético % para
mostrar se valor é par ou ímpar. Ex. (valor % 2 == 0) é par...)
"""

n = int(input("Digite um valor e verifique se é par ou impar: "))

if n % 2 == 0:
    print(f"O valor {n} é par!")
else: 
    print(f"O valor {n} é impar!")