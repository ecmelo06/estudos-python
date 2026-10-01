"""
Python não possui o comando 'do-while', que executa o código
primeiro e testa depois. Simule essa estrutura de repetição criando um "Menu Interativo".
O programa deve exibir as opções: "Menu: 1 - Jogar | 2 - Salvar | 3 - Sair" e ler a escolha
do usuário em um loop infinito.
Regras:
• Se ele digitar 1 ou 2, o programa informa qual opção foi escolhida e volta ao menu.
• Se ele digitar 3, o programa avisa que está saindo e encerra usando o comando
break.
• Se ele digitar qualquer valor diferente de 1, 2 ou 3, o programa deve exibir uma
mensagem de "Opção inválida" e voltar ao menu.
"""

while True:
    print("Menu: \n" \
    "1. Jogar\n" \
    "2. Salvar\n" \
    "3. Sair")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        print("Opção: Jogar foi selecionada.")
    elif opcao == 2:
        print("Opção: Salvar foi selecionada.")
    elif opcao == 3:
        print("Opção: Sair foi selecionada. " \
        "Saindo...")
        break
    else:
        print("Opção inválida.")