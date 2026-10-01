"""
 Escreva um programa em Python que funcione em um laço contínuo
obedecendo às seguintes regras:
(1) Solicite ao usuário um número inteiro positivo. Se o usuário digitar 0, encerre o
programa avisando o usuário sobre o encerramento.
(2) Para qualquer outro número digitado pelo usuário, gere uma 'tabuada' que
multiplique esse número de 1 até ele mesmo. Exemplo: Se o usuário digitar 4, o
programa deve imprimir:
1 x 4 = 4
2 x 4 = 8
3 x 4 = 12
4 x 4 = 16
"""
i = 1
num = int(input("Digite um número positivo: "))
if num == 0:
    print("O programa está encerrando.")
else:
    for i in range (i, num+1):
        result = i * num
        print(f"{i} x {num} = {result}")