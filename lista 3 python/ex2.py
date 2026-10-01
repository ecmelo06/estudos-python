"""
Um site de e-commerce precisa definir o valor do frete. Compras a partir de
R$ 200,00 têm frete grátis; caso contrário, o frete custa R$ 30,00. Crie um programa que
solicite ao usuário o valor da compra e que, usando o Operador Ternário do Python,
armazene o valor do frete em uma variável chamada 'valor_frete' e depois imprima o
resultado.
"""

valor_frete = 30
compra = float(input("Digite o valor da compra: "))

totalValue = "Frete Grátis" if compra >= 200 else (compra + valor_frete)
print(totalValue)