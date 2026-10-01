"""
1. (ExeSelecao01) Construa um programa em Python para ler um valor, verificar se é maior
do que 100 e mostrar essa informação. (DICA: Usar if/else para mostrar se valor é > ou <
100)
"""

n = int(input("Digite um valor: "))

if n > 100:
    print(f"O valor {n} é maior que 100.")
elif n == 100:
    print(f"O valor {n} é igual a 100.")
else:
    print(f"O valor {n} é menor que 100.")