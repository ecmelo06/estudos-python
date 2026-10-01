"""
Escreva um programa em Python que simule a caixa de um
supermercado. O programa deve pedir continuamente o valor dos produtos comprados.
Se o usuário digitar o valor 0 (zero), o programa deve abortar o laço e mostrar o valor total
da compra. (Dica: Use uma variável acumuladora inicializada com zero, atualizando-a a
cada volta do laço).
"""

cont = 0
price = 0
value = float(input("Bem-Vindo ao SuperPreçoBaixoQueDependeDoQueVocêComprou" \
"Digite o valor da sua compra: "))

while value != 0:
    price += value
    cont += 1
    avgPrice = price / cont
    value = float(input("Digite o valor da sua compra: "))

print(f"O valor total da compra ficou em: R$ {avgPrice:.2f}")