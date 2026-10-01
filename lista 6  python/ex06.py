"""
Crie um programa em Python que peça ao usuário para digitar uma
palavra qualquer e um número inteiro N. Usando um laço 'for' com a função range()
contendo apenas UM argumento, imprima a palavra digitada N vezes na tela.
"""

i = 0
word = input("Digite uma palavra: ") 
num = int(input("Quantas vezes você quer que ela apareça? "))
print(f"A palavra: {word} irá aparecer {num} vezes.")
for i in range (i, num):
    print(f"{word}.")