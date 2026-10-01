"""
Produtos em uma mercearia possuem preços variados de acordo com o
tipo de produto e a quantidade a ser comprada. Implemente um programa em Python que
apresente a lista de produtos disponíveis juntamente com seus preços e solicite ao usuário
que escolha (1) o produto a ser comprado e (2) a quantidade escolhida do produto e informe
o valor da compra. Os produtos e seus preços são: banana (R$ 0,30 se forem compradas
menos que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze), laranja (R$ 0,40 se
forem compradas menos que uma dúzia, e R$ 0,35 se forem compradas pelo menos doze),
maçã (R$ 0,50 se forem compradas menos que uma dúzia, e R$ 0,45 se forem compradas pelo
menos doze), kiwi (R$ 0,40 se forem compradas menos que uma dúzia, e R$ 0,30 se forem
compradas pelo menos doze).
"""

print("--------- Lista de Produtos e Preços ---------")
print("1. Banana -> R$ 0,30 (preço granel) ou R$ 0,25 (preço duzia ou mais) ")
print("2. Laranja -> R$ 0,40 (preço granel) ou R$ 0,35 (preço duzia ou mais) ")
print("3. Maça -> R$ 0,50 (preço granel) ou R$ 0,45 (preço duzia ou mais) ")
print("4. Kiwi -> R$ 0,40 (preço granel) ou R$ 0,30 (preço duzia ou mais) ")

value = int(input("Digite o número correspondente ao item desejado: "))


match value:
    case 1:
        qtd = int(input("Digite o total de itens: "))
        if qtd < 12:
            total = qtd * 0.3
            print("Item selecionado: Banana")
            print(f"Quantidade: {qtd}. Valor total da compra: R$ {total:.2f}")
        else:
            total = qtd * 0.25
            print("Item selecionado: Banana")
            print(f"Quantidade: {qtd}. Valor total da compra: R$ {total:.2f} ")
    case 2:
        qtd = int(input("Digite o total de itens: "))
        if qtd < 12:
            total  = qtd * 0.4
            print(f"Item selecionado: Laranja")
            print(f"Quantidade: {qtd}. Valor total da compra: R$ {total:.2f}")
        else: 
            total = qtd * 0.35
            print(f"Item selecionado: Laranja")
            print(f"Quantidade: {qtd}. Valor total da compra: R$ {total:.2f}")
    case 3:
        qtd = int(input("Digite o total de itens: "))
        if qtd < 12:
            total = qtd * 0.5
            print("Item selecionado: Maça")
            print(f"Quantidade: {qtd}. Valor total da compra: R$ {total:.2f}")
        else:
            total = qtd * 0.45
            print("Item selecionado: Maça")
            print(f"Quantidade: {qtd}. Valor total da compra: R$ {total:.2f}")
    case 4:
        qtd = int(input("Digite o total de itens: "))
        if qtd < 12:
            total = qtd * 0.40
            print(f"Item selecionado: Kiwi")
            print(f"Quantidade: {qtd}. Valor total da compra: R$ {total:.2f}")
        else:
            total = qtd * 0.30
            print(f"Item selecionado: Kiwi")
            print(f"Quantidade: {qtd}. Valor total da compra: R$ {total:.2f}")
    case _:
        print("Valor inválido. Nenhum item selecionado.")
        
    
        
        
