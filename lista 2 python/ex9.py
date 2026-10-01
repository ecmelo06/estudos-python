"""
Laranjas em um mercado de produtos orgânicos custam R$ 0,30 se forem
compradas menos que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Construa
um programa em Python que leia o número de laranjas compradas, calcule e escreva o valor
total da compra. Implementar uma validação da quantidade de frutas a serem compradas
para evitar que seja lido um número de laranjas menor (negativo) ou igual a zero.
"""

oranges = int(input("Digite a quantidade de laranjas: "))

if oranges <= 0:
    print("Nenhum item comprado.")
else: 
    if oranges < 12:
        total = float(oranges) * 0.30
        print(f"{oranges} unidade de laranjas compradas a R$ 0,30. Valor Total: R$ {total:.2f}")
    else:
        total = float(oranges) * 0.25
        print(f"{oranges} unidade de laranjas compradas a R$ 0,25. Valor Total: R$ {total:.2f}")

