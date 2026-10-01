"""
Leia o mês atual (texto) e o mês de nascimento do cliente (texto),
além do valor das compras dele (decimal). Verifique se o mês atual é igual ao
de nascimento (ignorando letras maiúsculas/minúsculas). Se for, aplique um
desconto de 20% e exiba o novo valor da compra. Senão, exiba o valor normal da
compra.
"""
import locale 
import datetime
locale.setlocale(locale.LC_TIME, 'portuguese')

name = input("Bem-Vindo ao seu e-commerce. \n" \
"Digite o seu nome: ")
monthAnni = input(f"Olá, {name}.\n"
"Digite o mês em que você faz aniversário: ").upper()
currentMonth = datetime.datetime.now().strftime('%B').capitalize().upper()
shopping = float(input("Digite o valor das tuas compras: "))

if monthAnni == currentMonth:
    print("Como este é o mês do teu aniversário, você tem descontos de 20%.")
    totalShpping = shopping - (shopping*0.2)
    print(f"O valor inicial das tuas compras: R$ {shopping:.2f}")
    print(f"O valor com os descontos aplicados fica: R$ {totalShpping:.2f}")
else:
    print(f"Este não é o mês do teu aniversário, valor final: {shopping}")