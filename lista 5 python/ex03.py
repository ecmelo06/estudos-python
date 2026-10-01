"""
Crie um programa em Python que receba do usuário um número inteiro
positivo e determine se ele é um 'número perfeito'. Um número perfeito é aquele cuja soma
de todos os seus divisores (excluindo ele mesmo) é igual ao próprio número. Lembre-se: um
divisor é qualquer valor que divida o número original de forma exata, ou seja, deixando resto
zero. Exemplo: O número 6 é perfeito, pois seus divisores são 1, 2 e 3 (todos dividem o 6
deixando resto zero), e a soma deles (1 + 2 + 3) é igual a 6. (Dica 1: os divisores a serem testados
devem ser todos os inteiros no intervalo que começa em 1 e vai até o número digitado -1
(exclui-se o número digitado). (Dica 2: usar “for i in range(1, numero_lido)” para navegar no
intervalor de valores a serem testados como divisores). Existem apenas 3 números perfeitos
no intervalo entre 0 e 1000, que são: 6, 28 e 496.
"""

cont = 0
i = 1
num = int(input("Digite um valor: "))
for i in range (i, num):
   
    if num % i == 0:
        cont += i

if cont == num:
    print(f"{num} é um número perfeito.")
else:
     print(f"{num} não é um número perfeito.")