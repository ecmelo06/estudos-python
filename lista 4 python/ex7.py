"""
Uma máquina de café aceita os códigos 1 (Expresso) e 2 (Capuccino)
durante a escolha do produto. Faça um programa que se passe pela máquina de café e
que leia o código do produto desejado (inteiro) e uma variável booleana indicando se o
usuário “inseriu_cartao”. Após isso, usando, usando ‘mach-case’, verifique para a opção
de café escolhida se o cartão foi inserido. Se não foi (usando o operador ‘not’), peça para
inserir (“Aviso: Por favor, aproxime o cartão de pagamento para liberar a bebida”). Se foi
inserido, libere a bebida (“Pagamento aprovado. Preparando seu {nome_bebida} bem
quentinho...”).
"""

print("Maquina NesCoffee. \n" \
"Opções de Cafés: \n" \
"1 - Café Expresso. \n" \
"2 - Capuccino.")
option = int(input("Digite a opção: "))

match option:
    case 1: 
        credit_card = input("Insira seu cartão. n" \
        "cartão inserido [S/N]? ").upper()
        card_inserted = credit_card in ['S', 'SIM']
        if card_inserted == True: 
            print("Pagamento aprovado. Preparando seu Café Expresso bem quentinho...")
        else:
            print("Aviso: Por favor, aproxime o cartão de pagamento para liberar a bebida")
    case 2: 
        credit_card = input("Insira seu cartão. n" \
        "cartão inserido [S/N]? ").upper()
        card_inserted = credit_card in ['S', 'SIM']
        if card_inserted == True: 
            print("Pagamento aprovado. Preparando seu Capuccino bem quentinho...")
        else:
            print("Aviso: Por favor, aproxime o cartão de pagamento para liberar a bebida")
    case _:
        print("Nenhuma opção de café escolhida.")
        exit()