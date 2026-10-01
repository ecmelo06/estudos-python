"""
Crie um programa em Python que, usando um único laço 'for', exiba a
sequência de números começando em 2, indo até 20 (incluindo o 20), pulando de 2 em 2.
Dentro do mesmo laço, some todos esses valores e, ao final da execução do laço, imprima
o resultado total da soma.
"""

total = 0
i = 2
for i in range (i, 21, 2):
    total += i
    print(i)
print(f"A soma total dos números é: {total}")