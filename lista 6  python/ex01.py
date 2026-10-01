"""
Crie um programa em Python que peça ao usuário um número inicial
para uma contagem regressiva. O programa deve usar um laço 'for' para contar desse
número até 1, imprimindo cada valor. Após imprimir o número 1, o programa deve
imprimir a palavra "Fogo!". (Dica: Lembre-se de como o terceiro argumento da função
ange() funciona para fazer o passo negativo, conforme visto em aula).
"""

num = int(input("Digite um número inteiro: "))
i = 0
for i in range (num, i, -1):
    print(f"{i}, ")
print("Fogo!")