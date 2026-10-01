"""
Leia um número de um crachá (inteiro) e o setor de trabalho (texto).
• Se o número do crachá for menor que 100 E o setor for "Diretoria", escreva
"Acesso Livre".

• Se o número do crachá for maior ou igual a 100 E o setor for "TI", escreva "Acesso
Restrito aos Servidores".

• Para todos os outros casos, escreva "Acesso Negado". Use a estrutura `if-elif-
else`.
"""

name = input("Bem-Vindo empresa X. \n" \
"Digite seu nome: ")
card = int(input(f"Olá, {name}. \n"
"Digite o número do seu cartão: "))
sector = input("Digite o seu setor [TI / Diretoria]: ").upper()
verifySector = sector in ['TI', 'DIRETORIA']

if card < 100 and verifySector == True:
    print("Acesso Livre.")
elif card >= 100 and verifySector == True:
    print("Acesso Restrito aos Servidores.")
else:
    print("Acesso Negado.")