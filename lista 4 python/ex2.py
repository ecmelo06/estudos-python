"""
Leia o nome de um cliente (texto) e a quantidade de pontos de
fidelidade dele (inteiro). Usando exclusivamente o Operador Ternário, crie uma
variável chamada `categoria` que receba o texto "Cliente VIP" se ele tiver mais
de 1000 pontos, ou "Cliente Padrão" caso contrário. Imprima uma mensagem de
boas-vindas mesclando o “nome” e a “categoria”.
"""

name = input("Bem-Vindo ao seu programa de fidelidade. \n" \
"Digite seu nome: ")
fidelity = int(input("Pontos de fidelidade: "))

catagory = "Cliente VIP" if fidelity > 1000 else "Cliente Padrão"
print(f"Bem-Vindo, {name}. Sua categoria é: {catagory}")