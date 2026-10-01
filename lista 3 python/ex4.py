"""
Crie o menu de atendimento automatizado de uma operadora de internet. O
sistema deve ler um número digitado pelo usuário.
● Se digitar 1 ou 2, exiba: "Redirecionando para o Suporte Técnico".
● Se digitar 3, exiba: "Redirecionando para o Financeiro".
● Se digitar 4, exiba: "Redirecionando para o Cancelamento".
● Para qualquer outro valor, exiba: "Opção inválida. Tente novamente.".
"""

print("Bem-Vindo ao seu atendente virtual\n " \
"Digite 1 ou 2 para ser Redirecionado para o Suporte Técnico.\n" \
"Digite 3 para ser Redirecionado para o setor Financeiro.\n" \
"Digite 4 para ser Redirecionado para o setor de Cancelamento.")
value = int(input("Digite a opção: "))
match value:
    case 1 | 2:
        print("Redirecionando para o Suporte Técnico.")
    case 3:
        print("Redirecionando para o Financeiro.")
    case 4: 
        print("Redirecionando para o Cancelamento.")
    case _:
        print("Opção inválida. Tente novamente.")